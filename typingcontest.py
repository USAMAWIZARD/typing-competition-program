import csv
import PySimpleGUI as sg
from pynput.keyboard import Key, Listener
layout = [ [sg.Text('Name',size=(30, 1),font=("Helvetica", 15), text_color='blue'),sg.InputText(key="name" )],
            [sg.Text('Enrollment no',size=(30, 1), font=("Helvetica", 15), text_color='blue'),sg.InputText(key="enrollmentno" )],
            [sg.Text('type this paragraph',size=(20, 1), font=("Helvetica", 15), text_color='blue'),sg.Text('usama',size=(30, 1), font=("Helvetica", 15), text_color='blue')],

           [sg.Text('type paragraph here',size=(20, 1), font=("Helvetica", 15), text_color='blue'),sg.Text('', size=(1, 1)), sg.Multiline('',key="usertyped",size=(11,31),font=("Helvetica", -1),enter_submits=False,text_color="black",background_color="black")],
           [sg.Button('submit' ,key='submit')] ]
window = sg.Window('Typing Test',location=(0,0),size=(700,800)).Layout(layout).Finalize()
window.Maximize()

orignal = "i love programming".split()
appendaword = ""
i = 0
error = 0

while True:
    event, values = window.Read()
    def appendtostring(key):
        global appendaword
        appendaword = str(appendaword + str(key)).replace("'", "")

    def on_press(key):
        global error, i, appendaword
        print("hd")
        if key == Key.space:
            if appendaword != orignal[i]:
                error += 1
                print(error)
            i += 1
            appendaword = ""

        try:
            if (ord(str(key.char)) >= 65 and ord(str(key.char)) <= 90) or (
                    ord(str(key.char)) >= 97 and ord(str(key.char)) <= 121):
                appendtostring(key)
        except:
            pass


    if event =='submit':
            no=sg.PopupGetText("enter passwrod",password_char='*')
            print(no)
            if no=="iloveprogramming":
                name=values['name']
                enrollmentno = values['enrollmentno']
                usertyped=values['usertyped']

                datarow = [name, enrollmentno,error]
                with open('typingdata', 'a') as csvFile:
                    writer = csv.writer(csvFile)
                    writer.writerow(datarow)
                csvFile.close()

                window.FindElement('name').Update('')
                window.FindElement('enrollmentno').Update('')
                window.FindElement('name').Update('')
                window.FindElement('usertyped').Update('')
            else:
                sg.PopupError("wrongpassword")
with Listener(on_press=on_press) as listener:
    listener.join()
