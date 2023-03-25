import PySimpleGUI as sg

sg.theme('DarkTeal9')               #add some color to window
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
        print(event,values)

window.close()
