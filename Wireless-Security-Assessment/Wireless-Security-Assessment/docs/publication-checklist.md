# Checklist before publishing this project

- [ ] README accurately identifies all synthetic demonstration data.
- [ ] No unfinished project is described as completed in the CV.
- [ ] No client details, unreleased findings, Bugcrowd private programme info, secrets or credentials.
- [ ] No real IP addresses, MACs, SSIDs, serial numbers or identifying screenshots unless expressly approved.
- [ ] Only owned/authorised networks are tested; scope and stop conditions are written down.
- [ ] Unit tests pass and report generator works.
- [ ] Real lab tests, if performed, include dates, context, baseline and reproducible evidence.
- [ ] Risks are not given invented CVSS scores; uncertainty is acknowledged.
- [ ] Author knows how to explain each file, control, limitation and result independently.
- [ ] GitHub profile links to the README and shows a clear project summary.

## Suggested GitHub repository description

"Authorised Wi-Fi security assessment portfolio: offline AP configuration reviewer, safe guest isolation test, reporting templates and clearly labelled demo data."

## Suggested Git commands (run inside extracted project directory)

```bash
git init
git add .
git commit -m "Initial wireless assurance lab framework"
# Then create a blank GitHub repo under your own account and add its remote URL:
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/Wireless-Security-Assessment.git
git push -u origin main
```

If Git asks for authentication, follow GitHub's documented token/SSH guidance. Do not put tokens in a committed file.
