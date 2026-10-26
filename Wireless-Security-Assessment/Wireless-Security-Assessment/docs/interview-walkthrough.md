# Explain your Wi-Fi security project in a Division 5 interview

## Honest 60-second pitch — applicable **before live lab testing**

> "I created a wireless security assessment framework to link configuration evidence with practical verification and remediation. It covers WPA2/WPA3, PMF, WPS, guest segregation, AP management and firmware maintenance. I wrote a Python tool that reviews manually collected settings and produces a structured findings register, and a tightly scoped connectivity check for one authorised private host/port. The included data is clearly labelled synthetic; I don't treat an offline configuration concern as a proven exploit. My next step is validating actual settings and traffic in a network I own, capturing baseline and firewall evidence, and retesting after hardening."

## 90-second pitch — fill in ONLY after real authorised testing

- **Context:** "I assessed my [owned lab/client-approved wireless environment] on [date], with [specific authorised scope]."
- **Method:** "I reviewed [actual relevant settings] and checked [specific approved guest-to-trusted service] while capturing [actual logs/evidence]."
- **Outcome:** "I observed [specific verified result]." If no issue found: "I confirmed [specific control], and couldn't validate any security issue in the tested scope."
- **Risk:** "The impact was [realistic consequence], subject to [assumptions]."
- **Remediation:** "I recommended/implemented [specific mitigation] and retested [exact steps]."
- **Quality assurance:** "I checked that every finding was reproducible, correctly scoped and understandable to a nontechnical stakeholder."

## Technical questions you should be ready for

1. Why is a private target IP insufficient to establish permission? (Ownership/written authorisation still required.)
2. What separates a **configuration concern** from a **confirmed vulnerability**?
3. Why do you test a known-listening service from a trusted client before testing from a guest client?
4. What other control could isolate a guest SSID if the AP has guest isolation disabled?
5. Why does PMF matter? What changes with WPA3?
6. How do client compatibility and device lifecycle affect a WPA3 migration?
7. How would you handle false positives from a vulnerability scanner?
8. What is your process for writing an executive finding and retesting it?
9. Which work was performed in freelance client engagements, and which work is solely from your personal lab? Answer this precisely.

## CV wording, based on actual completion stage

- **Now (framework built, testing not yet performed):** "Developed a Python-based wireless configuration assurance and reporting framework with controlled guest-isolation validation and synthetic demonstration data."
- **Later, only after lab evidence exists:** "Conducted an authorised lab wireless security assessment covering authentication, PMF, WPS and guest segmentation; recorded evidence, documented [actual result] and performed [actual retest]."

Never use client names, case details or private Bugcrowd findings without express permission.
