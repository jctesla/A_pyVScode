# This program allow us to use excel as a DB an show in our visual form.
# Note: to run this program.
# py -3.7-64 pyguiexcel_01.py                   // run this program w py -3.7-64

# if you run this program w py ver-3.8-64 :.
# py -3.7-64 pyguiexcel_01.py                   // Da Error = import PySimpleGUI as sg  # ModuleNotFoundError: No module named 'PySimpleGUI'    :.
# p que corra instalamos el pckg : 
# py -3.8-64 -m pip install PySimpleGUI         // Corregido.


import PySimpleGUI as sg
import sys                                      # p sber la version de mi python
print(f"Version de Python={sys.version} \n")

sg.theme('DarkTeal9')                           #add some color to window
layout =[
    [sg.Text('Please fill this fields:')],
    [sg.Text('Name', size=(15,1)), sg.InputText(key='Name')],
    [sg.Submit(), sg.Exit()]
]

window = sg.Window('Data Input Form',layout)

while True:
    event, values = window.read()
    if event== sg.WIN_CLOSED or event=='Exit':
        break
    if event == 'Submit':
        print(event,values)

window.close()
