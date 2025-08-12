# Windows Health Check (PowerShell)
Quick Windows triage for L1: OS/build, uptime, C: free, Windows Update service, Defender status/signature age.

## Run
PowerShell (as user is fine):
1) `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass`
2) `.\win_health_check.ps1`

## Output
- Table to console
- `win_health_report.json` in this folder

```sql
Name               Value
----               -----
Hostname           RDS-LAPTOP
OS                 Microsoft Windows 11 Pro
BuildNumber        22631
UptimeHours        5.6
CDriveFreeGB       112.4
WindowsUpdateSvc   Running
DefenderEnabled    True
DefenderSigAgeHrs  3
```
