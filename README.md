Setup instructions
- u can download the zip or use this command to clone it:
+ git clone https://github.com/zdemon2002/Rocs-Interview.git
Dependencies
- there are seperated requirements file directly in the desktop and webapp folder
How to run the desktop test
- you will need to download WinAppDriver and run it using admin cmd 
- activate the venv in the desktop test folder -> pip install -r desktop_requirements.txt
- run the scripts in the test folder using cli or the Run function in Visual Studio Code 
How to run the web test
- activate the venv in the webapp test folder -> pip install -r desktop_requirements.txt
- run the scripts using the cli or the testing tab in Visual studio code (need to config pytest_> ctrl+shift+p-> Python: configure test-> Pytest-> Select the test folder )
