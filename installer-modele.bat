@echo off
chcp 65001 > nul
cd /d "%~dp0"
rem Installe le petit modele local du compagnon (environ 2 milliards de parametres).
rem Usage : installer-modele.bat            -^> qwen3.5:2b (conseille)
rem         installer-modele.bat leger      -^> qwen3.5:0.8b (PC tres modeste)
rem         installer-modele.bat qwen3:1.7b -^> un autre modele au choix
where ollama > nul 2>&1
if errorlevel 1 (
  echo Ollama est introuvable sur ce PC. Telecharge-le ici : https://ollama.com/download
  echo Installe-le, puis relance ce fichier.
  start https://ollama.com/download
  pause
  exit /b 1
)
set MODELE=qwen3.5:2b
if /i "%~1"=="leger" set MODELE=qwen3.5:0.8b
if not "%~1"=="" if /i not "%~1"=="leger" set MODELE=%~1
echo Telechargement de %MODELE% (une seule fois)...
ollama pull %MODELE%
if errorlevel 1 (echo Echec du telechargement. & pause & exit /b 1)
echo.
echo Modele %MODELE% installe. Lance interface.bat : il le prendra automatiquement.
pause
