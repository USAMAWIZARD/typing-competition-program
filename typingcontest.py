import csv
import PySimpleGUI as sg

layout = [ [sg.Text('Name',size=(30, 1),font=("Helvetica", 15), text_color='blue'),sg.InputText(key="name" )],
            [sg.Text('Enrollment no',size=(30, 1), font=("Helvetica", 15), text_color='blue'),sg.InputText(key="enrollmentno" )],
            [sg.Text('type this paragraph',size=(20, 1), font=("Helvetica", 15), text_color='blue'),sg.Text('usama',size=(30, 1), font=("Helvetica", 15), text_color='blue')],

           [sg.Text('type paragraph here',size=(20, 1), font=("Helvetica", 15), text_color='blue'),sg.Text('', size=(1, 1)), sg.Multiline('',key="usertyped",size=(11,31),font=("Helvetica", -1),enter_submits=False,text_color="black",background_color="black")],
           [sg.Button('submit' ,key='submit')] ]
window = sg.Window('Typing Test',location=(0,0),size=(700,800)).Layout(layout).Finalize()
window.Maximize()
while True:
    event,values = window.Read()
    if event =='submit':
        no=sg.PopupGetText("enter passwrod",password_char='*')
        print(no)
        if no=="iloveprogramming":
            name=values['name']
            enrollmentno = values['enrollmentno']
            usertyped=values['usertyped']
            #print(name,enrollmentno,usertyped)
            orignal="usama is a computerwizard"
            origanallist = orignal.split(" ")
            usertypedlist = usertyped.split(" ")
            orignalindex=0
            userindex=0
            i=0
            print(origanallist)
            print(usertypedlist)
            typedwrong=[]
            for orignal in origanallist:
                if orignal in usertypedlist:
                    pass
                else:
                    typedwrong.append(orignal)
            print(typedwrong)
            datarow=[name,enrollmentno,"eror"]
            with open('typingdata','a') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(datarow)
            csvFile.close()
            window.FindElement('name').Update('')
            window.FindElement('enrollmentno').Update('')
            window.FindElement('name').Update('')
            window.FindElement('usertyped').Update('')
        else:
            sg.PopupError("wrongpassword")