if not "%1"=="am_admin" (powershell start -verb runas '%0' am_admin & exit /b)
mklink "%USERPROFILE%\Desktop\EFT Quest Wiki" %~dp0main.exe
mklink "%appdata%\Microsoft\Windows\Start Menu\Programs\EFT Quest Wiki" %~dp0main.exe