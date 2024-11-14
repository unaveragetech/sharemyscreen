@echo off
echo Setting up the Screen Streaming Application environment...you've run setup.bat

REM Step 1: Check if Python and pip are installed
where python >nul 2>&1
if %errorlevel% neq 0 (
    echo Python is not installed. Please install Python and rerun this script.
    exit /b
)

where pip >nul 2>&1
if %errorlevel% neq 0 (
    echo pip is not installed. Please install pip and rerun this script.
    exit /b
)

REM Step 2: Install virtual environment tools
echo Installing virtual environment tools...
pip install virtualenv

REM Step 3: Create and activate a virtual environment
echo Creating virtual environment...
python -m venv venv
call venv\Scripts\activate

REM Step 4: Install required Python packages
echo Installing required Python packages...
pip install -r requirements.txt

REM Step 5: Install PyVirtualDisplay for headless environments (if not already in requirements.txt)
pip install pyvirtualdisplay

REM Step 6: Install OpenCV dependencies (for Windows, we install opencv-python-headless)
echo Installing OpenCV dependencies...
pip install opencv-python-headless

REM Step 7: Install Flask (for serving the Streamlit app in a web server)
pip install flask

REM Step 8: Create necessary directories and files
echo Setting up necessary files...
if not exist "verified_users.txt" type nul > verified_users.txt
if not exist "unverified_users.txt" type nul > unverified_users.txt

REM Step 9: Generate documentation (README.md)
echo Generating documentation...

(
echo # Screen Streaming Application
echo.
echo This application allows users to stream their PC screen in real-time through a Streamlit web interface. It includes user authentication, settings management, and adjustable screen streaming.
echo.
echo ## How to Use
echo ### Registration
echo - Users register with email, username, and password.
echo - To verify, manually add usernames to ^`verified_users.txt^` file.
echo.
echo ### Starting the Application
echo - Activate the virtual environment with:
echo   ^```
echo   venv\Scripts\activate
echo   ^```
echo - Then, start the application by running:
echo   ^```
echo   streamlit run app.py
echo   ^```
echo - The app will open in your browser at the provided URL.
echo.
echo ## Dependencies
echo - **Streamlit**
echo - **Werkzeug**
echo - **PyAutoGUI**
echo - **OpenCV**
echo - **PyVirtualDisplay** (for headless environments)
echo - **Flask** (to serve the Streamlit app via Flask)
echo.
echo ## Important Notes
echo - If deploying on a server or headless environment, a virtual display will be started automatically.
) > README.md

echo Setup complete. Run the application with: streamlit run app.py and navigate to the provided URL.
pause
