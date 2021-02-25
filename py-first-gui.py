import PySimpleGUI as interface
import sys

layout=[[interface.Text("Write your name: ")],
        [interface.Input(key="-INPUT-")],
        [interface.Text(size=(40,1),key="-OUTPUT-")],
        [interface.Button("Send"), interface.Button("Quit")] ]

window = interface.Window("MyFirstGUIinPython",layout)


while True:
    event, values = window.read()

    if(event == interface.WINDOW_CLOSED or event == "Quit"):
        window.close()
        sys.exit()
    
    window["-OUTPUT-"].update("This is the input: " + values["-INPUT-"])

