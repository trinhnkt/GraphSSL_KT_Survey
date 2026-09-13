# PowerShell Gate Check for F1‑F9 Audits

# Paths
$RepoRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$AuditDir = Join-Path $RepoRoot "..\audit"
$StatusFile = Join-Path $RepoRoot "..\status\ready_for_A15.md"
$GateFile = Join-Path $AuditDir "F9_PRE_A15_GATE.md"

# Collect statuses
$results = @{}
Get-ChildItem -Path $AuditDir -Filter "*.md" | ForEach-Object {
    $content = Get-Content $_.FullName -Raw
    if ($content -match "\*\*Status:\*\*\s*(\w+)") {
        $status = $matches[1].ToUpper()
        $results[$_.Name] = $status
    } else {
        $results[$_.Name] = "UNKNOWN"
    }
}

$allPass = $results.Values -notcontains "FAIL" -and $results.Values -notcontains "UNKNOWN"

# Ensure status directory exists
$statusDir = Split-Path $StatusFile -Parent
if (-not (Test-Path $statusDir)) { New-Item -ItemType Directory -Path $statusDir -Force | Out-Null }

# Write readiness flag
if ($allPass) {
    Set-Content -Path $StatusFile -Value "READY_FOR_FINAL_A15 = YES`n"
} else {
    $lines = @("READY_FOR_FINAL_A15 = NO", "Failing tasks:")
    foreach ($kv in $results.GetEnumerator()) {
        if ($kv.Value -ne "PASS") {
            $lines += "- $($kv.Key): $($kv.Value)"
        }
    }
    Set-Content -Path $StatusFile -Value ($lines -join "`n")
}

# Update gate audit file status line
if (Test-Path $GateFile) {
    $gateContent = Get-Content $GateFile
    $newGate = $gateContent -replace "\*\*Status:\*\*\s*\w+", "**Status:** " + (if ($allPass) { "PASS" } else { "FAIL" })
    Set-Content -Path $GateFile -Value $newGate
}

Write-Host "Gate check completed. READY_FOR_FINAL_A15 =" (if ($allPass) { "YES" } else { "NO" })
