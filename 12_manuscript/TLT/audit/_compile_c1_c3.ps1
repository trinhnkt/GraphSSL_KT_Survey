$ErrorActionPreference = "Continue"
$root = Split-Path -Parent $PSScriptRoot
$log = Join-Path $PSScriptRoot "_compile_c1_c3.log"
Set-Content -Path $log -Value "start $(Get-Date -Format o)" -Encoding utf8

function Run-Latex([string]$dir, [string]$job) {
  Push-Location $dir
  cmd /c "pdflatex -interaction=nonstopmode $job.tex > _pdflatex_$job.txt 2>&1 < nul"
  $code = $LASTEXITCODE
  Pop-Location
  $out = Select-String -Path (Join-Path $dir "_pdflatex_$job.txt") -Pattern "Output written|^!" | Select-Object -Last 4
  Add-Content $log "$job exit=$code"
  foreach ($line in $out) { Add-Content $log $line.Line }
  return $code
}

$figDir = Join-Path $root "figures"
Push-Location $figDir
cmd /c "pdflatex -interaction=nonstopmode -halt-on-error fig_prisma_flow.tex > fig_prisma_flow_c1c3.txt 2>&1 < nul"
$figCode = $LASTEXITCODE
Pop-Location
Add-Content $log "FIG prisma exit=$figCode"
Select-String -Path (Join-Path $figDir "fig_prisma_flow_c1c3.txt") -Pattern "Output written|^!" | ForEach-Object { Add-Content $log $_.Line }

foreach ($job in @("main_tlt_anonymous", "main_tlt_full", "manuscript_TLT_FORMATTED_v1.3")) {
  Run-Latex $root $job | Out-Null
  Run-Latex $root $job | Out-Null
}

$parent = Split-Path -Parent $root
Run-Latex $root "COVER_LETTER" | Out-Null
Run-Latex $parent "COVER_LETTER" | Out-Null

Add-Content $log "end $(Get-Date -Format o)"
Get-Content $log
