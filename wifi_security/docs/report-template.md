# Wireless Security Assessment — Report Template

**Report ID:** [LAB-...]  
**Assessment scope:** [owned devices / SSIDs / authorized hosts]  
**Assessment dates:** [dates]  
**Assessment type:** [Owned lab / authorised client assessment]  
**Status:** [Draft / QA reviewed / Final]

## 1. Executive summary

[In 3–5 lines: why the wireless network was assessed, what was actually tested, confirmed results, business impact and recommended next actions. If no issues confirmed, say so.]

## 2. Scope and exclusions

| Scope | Details |
| --- | --- |
| Owner and authorisation | [Recorded privately] |
| In-scope SSIDs and APs | [Sanitised] |
| Test hosts | [Owned private lab destinations] |
| Exclusions | [Nearby networks, out-of-scope clients, attacks not authorised] |
| Assessment window | [date and timezone] |

## 3. Methodology

1. Obtain authorisation and document rules of engagement.
2. Review AP authentication, WPS, PMF, management and guest segmentation settings.
3. Establish trusted-to-trusted baseline for approved test service.
4. Validate authorised guest-to-trusted connectivity; correlate with router/AP logs.
5. Confirm findings, rank practical business impact, recommend controls and retest.

## 4. Findings register

| ID | Finding | Verification | Suggested risk | Status |
| --- | --- | --- | --- | --- |
| [WS-F01] | [specific issue] | [Observed / confirmed + evidence ID] | [Context-based rating] | [Open / remediated] |

### Finding [ID] — [descriptive title]

- **Affected asset(s):** [sanitised]
- **Control objective:** [required policy behaviour]
- **Technical evidence:** [what observation/test/log shows, when, exact method]
- **Independent validation:** [trusted baseline, authorised guest test, firewall log correlation]
- **Business impact:** [plausible effect, based on proven access, not speculation]
- **Risk and rationale:** [severity basis; CVSS only if defensible]
- **Remediation recommendation:** [precise, feasible action]
- **Retest evidence:** [actual outcome after fix]
- **Limitations:** [any exceptions or untested paths]

## 5. Management recommendations

[Prioritised, plain-English actions, accountable owner and desired timeframes if agreed.]

## 6. Evidence inventory and QA

| Evidence ID | Date | Source | Sanitised location | Supports |
| --- | --- | --- | --- | --- |
| [E01] | [date] | [redacted config screenshot] | [private artifact] | [WS-F01] |

**QA:** [spell-check / technical validation / sensitive-data review / peer review if obtained]

## 7. Limitations and legal notice

Only the authorised scope and methods above were assessed. A point-in-time assessment cannot guarantee absence of vulnerabilities. No third-party systems or unrelated SSIDs were assessed.
