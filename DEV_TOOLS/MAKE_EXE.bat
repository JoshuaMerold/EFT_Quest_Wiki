pyinstaller.exe --onefile --console -w -i "%~dp0..\qw_logo.ico" %~dp0..\main.py
copy %~dp0dist\main.exe ..\
copy %~dp0main.spec ..\
Xcopy /E %~dp0build %~dp0..\
rmdir /Q/S dist
rmdir /Q/S build
del /f/Q main.spec
pause