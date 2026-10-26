# DEMO ONLY — fictional finding (not tested)

**DEMO-WS01 — Guest Wi-Fi isolation misconfiguration**  
**Verification status:** SYNTHETIC EXAMPLE, UNVERIFIED  
**Severity:** Illustrative, provisional — NOT a CVSS result

## Hypothetical observation

An invented AP setting shows `guest_isolation_configured=false` for fictional `GuestLab-DEMO`. That setting **does not prove** guests can access the trusted network: downstream firewall rules may still block access. It creates a test hypothesis.

## How this would be verified *if performed*

An approved guest client would attempt a single TCP connection to a known-listening owned trusted server after confirming a successful trusted-client baseline. The tester would correlate the outcome with firewall rules and logs. Only successful unwanted connectivity could support a claim of segmentation failure.

## Potential business impact (conditional)

If unauthorised guest devices can communicate with trusted services, internal systems may be unnecessarily exposed to untrusted users.

## Recommended action

Separate guest and trusted zones and enforce a deny-by-default guest-to-trusted firewall rule with explicit documented exceptions. Restrict AP management access. Retest from the guest client, not just by inspecting a setting.

## How to convert to a real finding

Replace this document with authorised test artefacts and actual results; do not present this synthetic text as a discovered vulnerability.
