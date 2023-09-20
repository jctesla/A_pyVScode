# To convert a Python script (.py file) to a standalone executable (.exe file) using pyinstaller, follow these steps:

#-------------------------
'''
0.- Install pyinstaller:
If you haven't installed pyinstaller yet, you can do so using pip. Open a terminal or command prompt and run the following command:

$ pip install C
'''


#-------------------------
'''
1.- Navigate to the directory containing your Python script:
Using the terminal or command prompt, navigate to the directory where your Python script is located. For example:

cd /path/to/your/python/script
'''


#-------------------------
'''
2.- convert the Python script to an executable:
Run the pyinstaller command to convert your Python script to a standalone executable. Replace your_script.py with the name of your Python script:

pyinstaller --onefile your_script.py
'''


#-------------------------
'''
The --onefile option tells pyinstaller to bundle everything into a single executable file.

Locate the executable:
After running the pyinstaller command, it will create a new dist directory in your current working directory. Inside the dist directory, you will find the standalone executable file with the same name as your Python script, but with a .exe extension.
That's it! You now have a standalone .exe file that you can distribute and run on a Windows machine without requiring Python or any dependencies installed.

Keep in mind that pyinstaller may include some additional files and libraries in the generated executable to ensure it runs correctly. Make sure to distribute the entire contents of the dist directory when sharing the executable with others.
'''


#-------------------------
'''
MIO: revise que version y si esta Instaldo el pyIstaller:
miclab@Corei7-PC MINGW64 /d/phytonSpace/miBasic/A_pyVSCode/convert_pyToExe (main)
$ conda list pyinstaller
# packages in environment at C:\ProgramData\Anaconda3:
#
# Name                    Version                   Build  Channel
pyinstaller               5.6.2            py37h2bbff1b_0
pyinstaller-hooks-contrib 2023.6             pyhd8ed1ab_0    conda-forge
(base)
'''
