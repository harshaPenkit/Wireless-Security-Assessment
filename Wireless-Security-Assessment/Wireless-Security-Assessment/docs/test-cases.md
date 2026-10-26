# Test cases and evidence matrix

| ID | Activity | Preconditions | Evidence | Pass / concern criteria |
| --- | --- | --- | --- | --- |
| WS-01 | Inspect authentication and cipher suites | Admin access to owned AP | Redacted settings/config | Strong mode aligned with asset policy; WPA3 preferred where compatible; legacy modes flagged |
| WS-02 | Inspect PMF/802.11w | Owned AP | Screenshot of PMF setting | Enabled; required for WPA3; check clients before mandatory-on-WPA2 |
| WS-03 | Inspect WPS | Owned AP | Screenshot/config | Disabled or formally accepted exception |
| WS-04 | Check guest vs trusted network boundaries | Owned guest test client and known-listening owned target; permission recorded | Trusted baseline, guest test stdout, firewall allow/deny logs | Guest connectivity follows intended policy; interpret timeouts cautiously |
| WS-05 | Verify wireless/guest management access | Owned AP, explicit test address | Approved controlled attempt and access logs | Admin portal restricted to authorised management network |
| WS-06 | Check firmware advisories | Vendor/model/version available privately | Timestamped vendor advisory and remediation record | Supported firmware or documented mitigation |
| WS-07 | Report QA | Evidence and scope docs | Traceable finding to tests, business impact, retest | No unverified claims and no sensitive data in published report |

## Findings: verification categories

- **Observation:** A configuration or log entry verified by reviewer.
- **Potential finding:** An observation that may lead to risk but needs validation.
- **Confirmed finding:** A reproducible, authorised test demonstrated a policy/security issue.
- **Remediated:** Fix implemented and retest shows resolution.
- **Not applicable:** Control excluded with explicit rationale.

Never assign a CVSS vector without identifying a concrete vulnerability and defensible attack conditions. Configuration concerns can instead have provisional priority labels.
