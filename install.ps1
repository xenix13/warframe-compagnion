# Installation du Compagnon Warframe depuis GitHub (Windows 10/11).
# Dans PowerShell :
#   irm https://raw.githubusercontent.com/xenix13/warframe-compagnion/main/install.ps1 | iex
# Relancer la même commande met l'outil à jour sans toucher aux loadouts, aux données ni au modèle déjà téléchargés.
#
# Ce que ça fait :
#  1. installe Python 3.12 (pour l'utilisateur, via winget) s'il manque ;
#  2. télécharge l'outil dans %LOCALAPPDATA%\CompagnonWarframe ;
#  3. installe le modèle intégré (llama.cpp + Qwen3 1.7B, ~1,8 Go) : pas besoin d'Ollama ;
#  4. construit les données du jeu et crée un raccourci « Compagnon Warframe » sur le bureau.

$ErrorActionPreference = 'Stop'
$Repo    = 'xenix13/warframe-compagnion'
$Branche = 'main'
$Dossier = if ($env:COMPAGNON_DOSSIER) { $env:COMPAGNON_DOSSIER } else { Join-Path $env:LOCALAPPDATA 'CompagnonWarframe' }
$Options = if ($env:COMPAGNON_OPTIONS) { $env:COMPAGNON_OPTIONS -split ' ' } else { @() }   # ex. --leger, --gpu, --sans-ia

function Trouver-Python {
    foreach ($c in @(@('py', '-3'), @('python'))) {
        try {
            $v = & $c[0] @($c[1..9] + @('-c', 'import sys;print(sys.version_info[:2]>=(3,10))')) 2>$null
            if ($v -match 'True') { return ,$c }
        } catch {}
    }
    return $null
}

Write-Host "== Compagnon Warframe : installation dans $Dossier" -ForegroundColor Yellow

# 1. Python
$py = Trouver-Python
if (-not $py) {
    Write-Host "Python 3.10+ introuvable : installation de Python 3.12 (winget)..."
    winget install -e --id Python.Python.3.12 --scope user --accept-package-agreements --accept-source-agreements
    $env:Path = [Environment]::GetEnvironmentVariable('Path', 'User') + ';' + [Environment]::GetEnvironmentVariable('Path', 'Machine')
    $py = Trouver-Python
    if (-not $py) { throw "Python n'a pas pu être installé. Installe-le depuis https://www.python.org (coche « Add to PATH ») puis relance." }
}
$pyArgs = if ($py.Count -gt 1) { $py[1..9] } else { @() }

# 2. Téléchargement de l'outil (les dossiers de données ne sont pas dans l'archive : ils ne sont jamais écrasés)
$tmp = Join-Path $env:TEMP "compagnon-warframe-$(Get-Random)"
New-Item -ItemType Directory -Path $tmp | Out-Null
$zip = Join-Path $tmp 'outil.zip'
Write-Host "Téléchargement de l'outil ($Repo)..."
Invoke-WebRequest -UseBasicParsing "https://github.com/$Repo/archive/refs/heads/$Branche.zip" -OutFile $zip
Expand-Archive $zip -DestinationPath $tmp
$src = Get-ChildItem $tmp -Directory | Select-Object -First 1
New-Item -ItemType Directory -Force -Path $Dossier | Out-Null
robocopy $src.FullName $Dossier /E /NFL /NDL /NJH /NJS /NP | Out-Null
Remove-Item $tmp -Recurse -Force

# 3 et 4. Dépendances Python, modèle intégré, données du jeu, raccourci
Set-Location $Dossier
& $py[0] @($pyArgs + @('-m', 'pip', 'install', '--user', '-q', '-r', 'requirements.txt'))
& $py[0] @($pyArgs + @('-m', 'wfcompanion.installer') + $Options)
Write-Host "`nC'est prêt : double-clique sur « Compagnon Warframe » sur le bureau." -ForegroundColor Green
