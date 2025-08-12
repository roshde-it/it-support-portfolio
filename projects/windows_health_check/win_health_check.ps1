#Requires -Version 5.1
<#
.SYNOPSIS
 Quick Windows triage for L1 support: OS, uptime, C: free space, Windows Update svc, Defender status/signature age.
#>

function Try-Get($script) { try { & $script } catch { $null } }

$os      = Get-CimInstance Win32_OperatingSystem
$wu      = Try-Get { Get-Service wuauserv }
$mpStat  = Try-Get { Get-MpComputerStatus }
$mpSig   = Try-Get { Get-MpSignature }
$cdrive  = Get-CimInstance Win32_LogicalDisk -Filter "DeviceID='C:'"

$report = [ordered]@{
  Hostname          = $env:COMPUTERNAME
  OS                = $os.Caption
  BuildNumber       = (Get-ItemProperty "HKLM:\SOFTWARE\Microsoft\Windows NT\CurrentVersion").CurrentBuild
  LastBoot          = $os.LastBootUpTime
  UptimeHours       = ((New-TimeSpan $os.LastBootUpTime (Get-Date)).TotalHours).ToString("0.0")
  CDriveFreeGB      = [math]::Round(($cdrive.FreeSpace/1GB),1)
  WindowsUpdateSvc  = if ($wu) { $wu.Status } else { "Unknown" }
  DefenderEnabled   = if ($mpStat) { $mpStat.AMServiceEnabled } else { "Unknown" }
  DefenderSigAgeHrs = if ($mpSig) { ((New-TimeSpan $mpSig.TimeStamp (Get-Date)).TotalHours).ToString("0") } else { "Unknown" }
}

$report | ConvertTo-Json | Out-File ".\win_health_report.json" -Encoding UTF8
$report.GetEnumerator() | Sort-Object Name | Format-Table -Auto
