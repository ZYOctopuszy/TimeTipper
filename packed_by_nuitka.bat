@echo off
echo Please run this bat file in the root directory of the project.
echo run enter_venv.bat first to activate the virtual environment.
echo and then run this bat file in the virtual environment.
echo Ctrl-C to exit or any key to continue.
pause
nuitka main.py --jobs=6 --mode=onefile --onefile-no-compression --include-data-dir=icons=icons --output-filename=TimeTipper-latest --output-dir=dist --msvc=latest --remove-output --windows-console-mode=disable --windows-icon-from-ico=icons\active.ico --windows-uac-admin --enable-plugin=pyside6 --plugin-enable=upx --lto=yes --show-progress
pause
echo on
@REM
