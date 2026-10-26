# Wireless Security Assessment — Configuration Review

**Assessment ID:** DEMO-WIFI-001
**Assessment type:** SYNTHETIC DEMONSTRATION - NO LIVE TEST CONDUCTED
**Date:** 2026-10-26
**Environment:** Fictional Lab Example

> **Important:** These are configuration observations requiring independent validation, NOT verified vulnerabilities. The sample input is entirely synthetic. Never use it to claim a real client engagement.

## Executive summary

Reviewed 2 manually documented access point record(s). Identified 6 potential controls to validate or improve. No active wireless tests or exploit attempts were performed by this script.

## Review register

| ID | Asset | Control | Suggested priority* | Observation | Validation and remediation |
| --- | --- | --- | --- | --- | --- |
| OBS-01 | Lab-AP-01 | Wireless authentication | Advisory | WPA2-Personal configured | Review suitability for WPA3 migration; WPA2 itself does not establish a vulnerability. |
| OBS-02 | Lab-AP-01 | PMF / 802.11w | Medium | Protected Management Frames disabled | Enable PMF; it is a WPA3 requirement. Check compatibility for WPA2 clients. |
| OBS-03 | Lab-AP-01 | WPS | Medium | Wi-Fi Protected Setup enabled | Disable WPS unless an approved business need exists. |
| OBS-04 | Lab-AP-01 | Guest segmentation | High | Guest isolation not configured in AP observations | Check routed/firewall isolation; validate from an authorised guest client against an owned trusted test host. |
| OBS-05 | Lab-AP-01 | Management access | Medium | AP management available over wireless per AP observations | Restrict AP management to an approved administrative network; confirm management plane exposure. |
| OBS-06 | Lab-AP-01 | Firmware maintenance | Review | Firmware advisory review not recorded | Record model, firmware version privately and compare with vendor advisories; absence of review is not proof of a vulnerability. |

*Suggested priority is a **preliminary triage label**, not a CVSS rating or proof of exploitability.*

## Verification and retest notes

- Record actual AP policy evidence with permission and without secrets.
- Confirm scope and run the single-port guest isolation check from an approved guest client against a known-listening private test service.
- Review access control and firewall logs; a blocked/failed connection alone does not prove adequate segmentation.
- Document resulting confirmed observations, business impact, recommended fix and post-remediation retest.

## Limitations

Offline configuration review only. No rogue-AP discovery, RF testing, Wi-Fi password testing, client negotiations, network scanning, traffic interception, exploitation, or compliance attestation.

## Reference

ASD Information Security Manual — Guidelines for networking: https://www.cyber.gov.au/ism/2026-09/guidelines-for-networking
