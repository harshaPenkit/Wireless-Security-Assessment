#!/usr/bin/env python3
"""Offline, non-invasive AP configuration reviewer.

Reads MANUALLY populated JSON and generates a preliminary Markdown report.
No radio interface, packet capture, attack, scan, authentication or network
communication is performed. Findings are REVIEW ITEMS, not confirmed exploits.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

REQUIRED_FIELDS = {
    "asset", "ssid", "security_mode", "pmf", "wps_enabled",
    "guest_network", "guest_isolation_configured",
    "management_access_from_wireless", "firmware_reviewed"
}


def assess_ap(ap: dict) -> list[dict]:
    missing = REQUIRED_FIELDS - set(ap)
    if missing:
        raise ValueError(f"{ap.get('asset', '(unknown asset)')}: missing: {', '.join(sorted(missing))}")
    for name in ("wps_enabled", "guest_network", "management_access_from_wireless", "firmware_reviewed"):
        if not isinstance(ap[name], bool):
            raise ValueError(f"{ap['asset']}: {name} must be true or false")
    if ap["guest_isolation_configured"] is not None and not isinstance(ap["guest_isolation_configured"], bool):
        raise ValueError(f"{ap['asset']}: guest_isolation_configured must be true, false, or null")
    findings: list[dict] = []

    def flag(control: str, observation: str, priority: str, action: str, basis: str = "Configuration review"):
        findings.append({"asset": ap["asset"], "ssid": ap["ssid"], "control": control,
                         "observation": observation, "priority": priority,
                         "action": action, "basis": basis, "status": "Needs validation"})

    mode = ap["security_mode"].lower().strip()
    if mode in {"open", "wep", "wpa", "wpa1"}:
        flag("Wireless authentication", f"Insecure security mode recorded: {ap['security_mode']}", "High",
             "Use an appropriately configured WPA3 mode where supported; assess device compatibility and transition controls.")
    elif mode not in {"wpa2-personal", "wpa2-enterprise", "wpa3-personal", "wpa3-enterprise", "wpa2/wpa3-transition"}:
        flag("Wireless authentication", f"Unrecognised/unknown security mode: {ap['security_mode']}", "Review",
             "Inspect exact AP security configuration and cipher suites; manually classify the mode.")
    elif mode.startswith("wpa2"):
        flag("Wireless authentication", f"{ap['security_mode']} configured", "Advisory",
             "Review suitability for WPA3 migration; WPA2 itself does not establish a vulnerability.")

    pmf = str(ap["pmf"]).lower().strip()
    if pmf not in {"disabled", "optional", "required"}:
        flag("PMF / 802.11w", f"Unknown PMF setting: {ap['pmf']}", "Review", "Verify PMF setting on the AP and associated clients.")
    elif pmf == "disabled":
        flag("PMF / 802.11w", "Protected Management Frames disabled", "High" if mode.startswith("wpa3") else "Medium",
             "Enable PMF; it is a WPA3 requirement. Check compatibility for WPA2 clients.")
    elif pmf == "optional":
        flag("PMF / 802.11w", "PMF optional; protection may not be negotiated by all clients", "Advisory",
             "Consider requiring PMF where devices support it, and verify real client negotiation.")

    if ap["wps_enabled"]:
        flag("WPS", "Wi-Fi Protected Setup enabled", "Medium", "Disable WPS unless an approved business need exists.")
    if ap["guest_network"] and ap["guest_isolation_configured"] is False:
        flag("Guest segmentation", "Guest isolation not configured in AP observations", "High",
             "Check routed/firewall isolation; validate from an authorised guest client against an owned trusted test host.")
    if ap["management_access_from_wireless"]:
        flag("Management access", "AP management available over wireless per AP observations", "Medium",
             "Restrict AP management to an approved administrative network; confirm management plane exposure.")
    if not ap["firmware_reviewed"]:
        flag("Firmware maintenance", "Firmware advisory review not recorded", "Review",
             "Record model, firmware version privately and compare with vendor advisories; absence of review is not proof of a vulnerability.")
    return findings


def build_report(payload: dict) -> str:
    if not isinstance(payload.get("access_points"), list) or not payload["access_points"]:
        raise ValueError("Input must include a non-empty 'access_points' array")
    assessment_type = str(payload.get("assessment_type", "UNSPECIFIED"))
    items = [finding for ap in payload["access_points"] for finding in assess_ap(ap)]
    lines = [
        "# Wireless Security Assessment — Configuration Review",
        "",
        f"**Assessment ID:** {payload.get('assessment_id', 'n/a')}",
        f"**Assessment type:** {assessment_type}",
        f"**Date:** {payload.get('observation_date', 'n/a')}",
        f"**Environment:** {payload.get('organisation', 'n/a')}",
        "",
        "> **Important:** These are configuration observations requiring independent validation, NOT verified vulnerabilities. The sample input is entirely synthetic. Never use it to claim a real client engagement.",
        "",
        "## Executive summary",
        "",
        f"Reviewed {len(payload['access_points'])} manually documented access point record(s). Identified {len(items)} potential controls to validate or improve. No active wireless tests or exploit attempts were performed by this script.",
        "",
        "## Review register",
        "",
        "| ID | Asset | Control | Suggested priority* | Observation | Validation and remediation |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    def escape_md(value: object) -> str:
        return str(value).replace("|", "\\|").replace("\n", " ").replace("\r", " ")
    for idx, item in enumerate(items, 1):
        lines.append("| " + " | ".join(escape_md(x) for x in [
            f"OBS-{idx:02d}", item["asset"], item["control"], item["priority"],
            item["observation"], item["action"]]) + " |")
    if not items:
        lines.append("| — | — | — | — | No concerns identified in provided configuration fields | Independent validation and testing still required |")
    lines += [
        "",
        "*Suggested priority is a **preliminary triage label**, not a CVSS rating or proof of exploitability.*",
        "",
        "## Verification and retest notes",
        "",
        "- Record actual AP policy evidence with permission and without secrets.",
        "- Confirm scope and run the single-port guest isolation check from an approved guest client against a known-listening private test service.",
        "- Review access control and firewall logs; a blocked/failed connection alone does not prove adequate segmentation.",
        "- Document resulting confirmed observations, business impact, recommended fix and post-remediation retest.",
        "",
        "## Limitations",
        "",
        "Offline configuration review only. No rogue-AP discovery, RF testing, Wi-Fi password testing, client negotiations, network scanning, traffic interception, exploitation, or compliance attestation.",
        "",
        "## Reference",
        "",
        "ASD Information Security Manual — Guidelines for networking: https://www.cyber.gov.au/ism/2026-09/guidelines-for-networking",
        "",
    ]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True, help="Manual AP observation JSON")
    parser.add_argument("--output", type=Path, required=True, help="Markdown report path")
    args = parser.parse_args()
    payload = json.loads(args.input.read_text(encoding="utf-8"))
    report = build_report(payload)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(report, encoding="utf-8")
    print(f"Wrote {args.output} (OFFLINE review, not a penetration test).")


if __name__ == "__main__":
    main()
