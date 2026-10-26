# Authorisation and rules of engagement — lab template

**Assessment ID:** [LAB-YYYYMMDD-01]  
**Owner / authorising party:** [You, or client with written permission]  
**Authorisation recorded:** [date and evidence location, kept private]  
**Testing window and timezone:** [start, end, Australia/Melbourne]  
**Tester:** [name]

## In scope

- [ ] AP/device(s): [owned model/hostname; redact serial and MAC in public report]
- [ ] Approved SSIDs: [CorpLab, GuestLab]
- [ ] Guest test client: [owned device]
- [ ] Target test service: [one owned private IPv4 address + port]
- [ ] Config-review data: [manual screenshots/exports approved for assessment]

## Out of scope

- All neighbours, public hotspots and other organisations' networks
- Password guessing, credential harvesting, deauthentication, RF interference, evil twins and phishing
- Anything not explicitly listed above

## Handling and safeguards

1. Verify written permission *before* all active tests; the sample report does not grant permission.
2. Back up AP configuration and schedule change window if altering settings.
3. Limit connectivity testing to one manually chosen private IP/port at a time.
4. Stop on unexpected impact; record incident and restore settings.
5. Store sensitive client evidence privately, apply retention/deletion requirements.
6. Obtain explicit approval before publishing any finding or screenshot.

## Success criteria

- Guest clients cannot access the known-listening trusted service unless explicitly approved.
- AP management interface is inaccessible to guest/wireless clients according to policy.
- Authentication, WPS and PMF settings meet the organisation's policy.
- Findings include reproducible evidence and verified remediation.
