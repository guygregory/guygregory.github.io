# publish.ps1

# Run Pelican to generate the site with the publish configuration
pelican content -s publishconf.py

# Ensure docs/CNAME exists with the correct domain
$CnamePath = "docs/CNAME"
$Domain = "pedanticjournal.com"

if (-not (Test-Path $CnamePath)) {
    $Domain | Out-File -FilePath $CnamePath -Encoding utf8
}