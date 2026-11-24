$ErrorActionPreference = "Continue"
Set-Location "D:\TRINH\GraphSSL_KT_Survey\12_manuscript\TLT"
$jobs = @(
  "main_tlt_anonymous",
  "main_tlt_full",
  "manuscript_TLT_FORMATTED_v1.3"
)
foreach ($name in $jobs) {
  cmd /c "pdflatex -interaction=nonstopmode $name.tex > _pdflatex_$name.txt 2>&1 < nul"
  cmd /c "bibtex $name > _bibtex_$name.txt 2>&1 < nul"
  cmd /c "pdflatex -interaction=nonstopmode $name.tex > _pdflatex_${name}_2.txt 2>&1 < nul"
  cmd /c "pdflatex -interaction=nonstopmode $name.tex > _pdflatex_${name}_3.txt 2>&1 < nul"
  Write-Output "DONE $name"
}
cmd /c "pdflatex -interaction=nonstopmode COVER_LETTER.tex > _pdflatex_COVER_LETTER.txt 2>&1 < nul"
Set-Location "D:\TRINH\GraphSSL_KT_Survey\12_manuscript"
cmd /c "pdflatex -interaction=nonstopmode COVER_LETTER.tex > _pdflatex_COVER_LETTER.txt 2>&1 < nul"
Write-Output "COVERS DONE"
