$ErrorActionPreference = "Continue"
$root = Split-Path -Parent $PSScriptRoot
$log = Join-Path $PSScriptRoot "_compile_tlt_2026-11-18.log"
Set-Content -Path $log -Value "start $(Get-Date -Format o)" -Encoding utf8

function Run-Latex([string]$dir, [string]$cmd) {
  Push-Location $dir
  cmd /c "$cmd < nul" | Out-Null
  $code = $LASTEXITCODE
  Pop-Location
  return $code
}

$figDir = Join-Path $root "figures"
$figs = @(
  "fig_graph_construction_pipeline",
  "fig_meta_analysis_charts",
  "fig_prisma_flow",
  "fig_ssl_framework",
  "fig_taxonomy_2d"
)
foreach ($f in $figs) {
  $code = Run-Latex $figDir "pdflatex -interaction=nonstopmode -halt-on-error $f.tex > $($f)_build.txt 2>&1"
  Add-Content $log "FIG $f exit=$code"
  if ($code -ne 0) {
    Add-Content $log "FIG FAIL $f"
    Get-Content (Join-Path $figDir "$($f)_build.txt") -Tail 30 | Add-Content $log
  }
}

$docs = @("main_tlt_anonymous", "main_tlt_full", "manuscript_TLT_FORMATTED_v1.3")
foreach ($f in $docs) {
  $c1 = Run-Latex $root "pdflatex -interaction=nonstopmode $f.tex > _pdflatex_$f.txt 2>&1"
  Add-Content $log "PDF1 $f exit=$c1"
  $cb = Run-Latex $root "bibtex $f > _bibtex_$f.txt 2>&1"
  Add-Content $log "BIB $f exit=$cb"
  $c2 = Run-Latex $root "pdflatex -interaction=nonstopmode $f.tex > _pdflatex_$f.txt 2>&1"
  $c3 = Run-Latex $root "pdflatex -interaction=nonstopmode $f.tex > _pdflatex_$f.txt 2>&1"
  Add-Content $log "PDF3 $f exit=$c3"
  Select-String -Path (Join-Path $root "$f.log") -Pattern "^! |Output written|undefined citations|Warning--I didn't find" |
    ForEach-Object { Add-Content $log $_.Line }
}

Add-Content $log "end $(Get-Date -Format o)"
Get-Content $log
