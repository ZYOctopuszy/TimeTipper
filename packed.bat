@echo off
echo "Please run this .bat script in the project's root directory."
echo "First run enter_venv.bat to activate the virtual environment."
echo "Ctrl-C to exit or press any key to continue."
pause
nuitka main.py
echo "Compilation completed."
pause
echo on
