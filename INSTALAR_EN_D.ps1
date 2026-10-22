$ErrorActionPreference = 'Stop'
$destination = 'D:\PAGINA_WEB_TELECO'
if (-not (Test-Path 'D:\')) { throw 'No existe la unidad D en este equipo.' }
if (Test-Path $destination) { throw 'La carpeta D:\PAGINA_WEB_TELECO ya existe. Para proteger su trabajo, copie los archivos manualmente.' }
New-Item -ItemType Directory -Path $destination | Out-Null
Get-ChildItem -LiteralPath $PSScriptRoot -Force | Copy-Item -Destination $destination -Recurse
Write-Host 'Archivos copiados a D:\PAGINA_WEB_TELECO. Abra ABRIR_PAGINA.bat.'
