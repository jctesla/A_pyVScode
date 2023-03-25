import PySimpleGUI as sg
import pandas as pd
import datetime as dt

sg.theme('DarkTeal9')        # add some color to window
EXCEL_FILE = 'MisDatos_Entry.xlsx'
df = pd.read_excel(EXCEL_FILE)               # Create a DataFrame of panda
layout =[
    [sg.Text('Please fill this fields:')],
    [sg.Text('Name', size=(15,1)), sg.InputText(key='Name')],
    [sg.Text('Tu Color', size=(15,1)), sg.Combo(['Green','Blue','Red'], key='tuColor')],
    [sg.Text('I Speak', size=(15,1)),
                                      sg.Checkbox('German',key='German'),
                                      sg.Checkbox('Spanish',key='Spanish'),
                                      sg.Checkbox('English',key='English')                
    ],
    [sg.Text('No People', size=(15,1)), sg.Spin([i  for i in range(16)], initial_value=0,key='People')],
    [sg.Submit(), sg.Exit()]
]

window = sg.Window('Data Input Form',layout)

while True:
    event, values = window.read()
    if event== sg.WIN_CLOSED or event=='Exit':
        break
    if event == 'Submit':
        # actualizo el Dict con el nuevo valor segun la posicion como se creo en el Excel.
        fecha = dt.datetime.now()
        print(f'event= {event}  / dictVal= {values}  /  Fecha = {fecha.strftime("%d/%m/%Y %H:%M:%S")}')  # Time = 26/06/2022 13:37:12
        values.update({'Fecha': fecha.strftime("%d/%m/%Y %H:%M:%S")}) 
                
        df = df.append(values, ignore_index=True)   # esto solo los nombres de los Keys, coiciden con los titulos de tu sheet de excel.
        df.to_excel(EXCEL_FILE,index=False)
        sg.popup('Data Gaurardado')

window.close()
