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
rem Compagnon Warframe avec le modele integre (llama.cpp + Qwen3 1.7B), sans Ollama
if not exist "%BASE%\..\companion-data\warframe.sqlite" (
  echo Premier lancement : preparation des donnees du jeu ^(1 a 3 minutes^)...
  %PY% -m wfcompanion.update --base "%BASE%"
) else (
  %PY% -m wfcompanion.update --base "%BASE%" --no-wiki > nul 2>&1
)
%PY% -m wfcompanion.web --base "%BASE%" --local %*
if errorlevel 1 pause
