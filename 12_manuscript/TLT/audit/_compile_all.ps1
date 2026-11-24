Set-Location (Split-Path -Parent $PSScriptRoot)
foreach ($f in 'main_tlt_anonymous','main_tlt_full','manuscript_TLT_FORMATTED_v1.3') {
  foreach ($i in 1,2) { cmd /c "pdflatex -interaction=nonstopmode -file-line-error $f.tex < nul > _pdflatex_out.txt 2>&1" }
  "== $f"
  Select-String -Path _pdflatex_out.txt -Pattern '^\S+:\d+:|^!|Output written|undefined' | ForEach-Object { $_.Line }
  "overfull: " + (Select-String -Path "$f.log" -Pattern 'Overfull \\hbox').Count
}
