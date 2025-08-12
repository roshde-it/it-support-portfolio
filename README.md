# IT Support Portfolio

## Why This Repo

Built to show practical L1 problem-solving, tidy documentation, and simple automation.

Small, practical tools and checklists that reflect real Level 1-2 support tasks. Everything here is simple, safe, and focused on showing problem solving, documentation, and tidy code.

## Projects

- **Network Quick Check** - run a few simple diagnostics to help determine if a user's issue is local machine, DNS, or external connectivity.
- **File Organiser** - move files from the Downloads folder into tidy subfolders by extension.
- **Log Scanner** - scan .log and .txt files for common error markers and produce a quick summary.
- **Windows Health Check** — quick machine triage (PowerShell). Output: table + JSON.
- **Network Quick Check** — now includes a simple /24 ping sweep (`ping_sweep.py`).

Each project folder has its own README with usage examples.

## Docs

- Windows Wi-Fi troubleshooting checklist
- Printer issues quick guide
- New starter onboarding checklist

## How to run

These scripts are written for Python 3.10+. They only use the standard library.

```bash
python projects/network_quick_check/netcheck.py
python projects/file_organiser/organise_downloads.py --path "C:/Users/Name/Downloads"
python projects/log_scanner/scan_logs.py --path "C:/Temp/logs"
```
```bash
PowerShell health check:
  cd projects/windows_health_check
  .\win_health_check.ps1

Network ping sweep:
  cd projects/network_quick_check
  python ping_sweep.py 192.168.1.0/24
```

## Notes

- Do not run scripts on production systems without permission.
- Scripts read-only unless clearly stated otherwise. The organiser moves files, so use the `--dry-run` flag first.
- No sensitive data should be added to this repo. Redact names, IPs, and anything confidential.
