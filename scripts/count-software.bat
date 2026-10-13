@echo off
setlocal
chcp 65001 >nul
where.exe pwsh.exe >nul 2>nul
if errorlevel 1 (
    "%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -NonInteractive -ExecutionPolicy Bypass -File "%~dp0count-software.ps1" %*
) else (
    pwsh.exe -NoProfile -NonInteractive -ExecutionPolicy Bypass -File "%~dp0count-software.ps1" %*
)
set "counterExit=%ERRORLEVEL%"
if "%~1"=="" pause
exit /b %counterExit%
