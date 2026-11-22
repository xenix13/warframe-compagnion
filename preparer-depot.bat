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
rem Prepare le depot GitHub (sans cles, loadouts ni donnees generees) dans ..\depot-github
rem   preparer-depot.bat                                        : prepare et commit seulement
rem   preparer-depot.bat --publier xenix13/compagnon-warframe   : cree le depot prive et l'envoie (outil gh requis)
rem   ajouter --public pour un depot public (necessaire pour l'installation en une commande)
%PY% -m wfcompanion.depot --sortie "%~dp0..\depot-github" %*
pause
