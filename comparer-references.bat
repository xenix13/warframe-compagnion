@echo off
chcp 65001 > nul
set PYTHONIOENCODING=utf-8
cd /d "%~dp0"
rem base : dans le dossier de l'outil (installation GitHub) ou a cote (installation d'origine)
set "BASE=%~dp0base-warframe"
if not exist "%BASE%" set "BASE=%~dp0..\base-warframe"
set PY=python
where py > nul 2>&1 && set PY=py -3
rem version installee (setup) : Python embarque dans le dossier de l'outil
if exist "%~dp0python\python.exe" set PY="%~dp0python\python.exe"
rem Compare le robot aux builds de reference du joueur (04-retours-experience\builds-reference) et ecrit le rapport
%PY% -m wfcompanion.reference --base "%BASE%" --data "%BASE%\..\companion-data" %* > rapport-references.txt
type rapport-references.txt
pause
