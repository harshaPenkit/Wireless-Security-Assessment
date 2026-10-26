# Build & test: wireless assessment lab

Estimated hands-on effort: 3–6 hours depending on available equipment. Only use devices you own or that are explicitly authorised.

## Requirements

- One configurable access point (or a router with separate main/guest SSIDs), **owned by you**.
- One trusted test host capable of listening on a TCP port (optional: second laptop/VM).
- One client on your guest SSID running Python 3.10+.
- Access to your AP/router settings and firewall logs.
- An isolated lab or home-network maintenance window; avoid sensitive traffic.

## Procedure

### 1. Define scope and capture starting state

Copy [assessment-scope.md](assessment-scope.md), complete authorisation, AP identities and test IP/port. Take a backup before changing any AP/router configuration. Verify existing production or household clients will not be affected.

### 2. Configure isolated test networks

Create `CorpLab` (trusted) and `GuestLab` (guest). If supported, place them on different VLANs/subnets, such as `192.168.20.0/24` and `192.168.30.0/24`. Use a firewall/router rule to **deny new guest-to-trusted connections**. Exact configuration steps vary by model; inspect the router documentation.

### 3. Create a controlled test service

On your owned trusted test host `192.168.20.10` (change to your actual assigned private IP), launch a harmless listener:

```bash
# Python on the trusted host; test service listens on TCP/8000
python3 -m http.server 8000 --bind 192.168.20.10
```

Only use the host address assigned to that machine. Confirm access to the server **from a trusted client** first using `curl http://192.168.20.10:8000/`. The directory listing is lab-only and should not contain secrets.

### 4. Collect AP settings manually

Record actual WPA security mode, PMF, WPS, guest isolation configuration, AP management access path and firmware advisory review. Redact credentials and real identifiers. Duplicate `data/demo_observations.json` into `private/lab_observations.json` and replace every synthetic value with a value you actually verified. Set the assessment type to `OWNED LAB - CONFIGURATION REVIEW`. The script is not connected to the AP and cannot infer these values for you.

### 5. Run offline controls review

```bash
python3 src/wifi_audit.py --input private/lab_observations.json --output private/lab-review.md
```

Treat the output as **potential configuration concerns** pending review. It is not a pentest report on its own.

### 6. Validate guest isolation

Connect the testing client to `GuestLab`, not `CorpLab` or cellular internet. Run:

```bash
python3 src/guest_isolation_check.py --target 192.168.20.10 --port 8000 \
  --confirm-authorised --confirm-on-guest
```

Interpretation: a successful TCP handshake demonstrates that the guest client reached the known-listening trusted test service. An error/timeout does **not** prove segmentation; confirm service availability via the trusted baseline and inspect firewall logs for dropped packets. The guest client may otherwise be affected by wrong routing or an offline host.

### 7. Remediate and retest

If you find an actual policy violation, fix the relevant rule/management exposure, rerun the same controlled test, preserve sanitised before/after evidence, and update the findings report. Avoid creating an exposed state on production networks just to demonstrate a flaw.

### 8. Write and publish

Use `docs/report-template.md` to record evidence and findings. Before publication, redact sensitive information and clearly distinguish synthetic demonstrations from completed lab tests. If nothing is vulnerable, report the **validated positive controls** rather than inventing a finding.
