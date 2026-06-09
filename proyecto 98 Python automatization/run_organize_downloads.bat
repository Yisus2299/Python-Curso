@echo off
setlocal enabledelayedexpansion

rem Try python first
where python >nul 2>&1
if %ERRORLEVEL%==0 (
    python "%~dp0organize_downloads.py" %*
    exit /b %ERRORLEVEL%
)

rem Then try py launcher
where py >nul 2>&1
if %ERRORLEVEL%==0 (
    py "%~dp0organize_downloads.py" %*
    exit /b %ERRORLEVEL%
)

rem Search common Python install locations using recursive where search
set "PYTHON_EXE="
for %%P in (
    "%LOCALAPPDATA%\Programs\Python"
    "%LOCALAPPDATA%\Python"
    "%ProgramFiles%\Python"
    "%ProgramFiles(x86)%\Python"
) do (
    if exist "%%~P" (
        for /f "delims=" %%Q in ('where /r "%%~P" python.exe 2^>nul') do (
            set "PYTHON_EXE=%%Q"
            goto :found_python
        )
    )
)

:found_python
if defined PYTHON_EXE (
    "%PYTHON_EXE%" "%~dp0organize_downloads.py" %*
    exit /b %ERRORLEVEL%
)

echo No se encontró Python en el PATH ni en las ubicaciones habituales.
echo Instala Python desde https://www.python.org/downloads/ y marca "Add Python to PATH".
echo También puedes ejecutar el script usando la ruta completa a python.exe.
pause
