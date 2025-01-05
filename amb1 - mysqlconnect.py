from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import random
import mysql.connector
import os

root = Tk()
root.title('Ambulance booking main menu')
root.geometry('600x600')
root.configure(bg = "coral1")

name = StringVar()
age = StringVar()
gender = StringVar()
weight = StringVar()
height = StringVar()

mydb = mysql.connector.connect(host = 'localhost',user = 'root',passwd = '1234',database = 'hospitalmanagement')

mycursor = mydb.cursor()

def back():
    root3.withdraw()
    root.deiconify()

def nextpage():
    os.startfile("mapbookingMove.py")
    root.destroy()

def submit():
    n = name.get()  #string
    a = age.get()   #int
    g = gender.get()#string
    w = weight.get()#int
    h = height.get()#int

    H = ""

    N = ""

    for i in n:
        if(i != ' '):
            N += i

    for i in h:
        if(i != '.'):
            H += i
        

    if(N.isalpha() is True and a.isdigit() is True and g.isalpha() is True and w.isdigit() is True and H.isdigit() is True):
        List = [i for i in range(0000, 10000)]
        code = random.choice(List)
        c = "G"+str(code)
        
        file = open("flag2.txt","w")
        file.write(c+" "+n+" "+a+" "+g+" "+w+" "+h+"\n")
        file.close()

        #python - mysql connectivity
        #CODE| PATIENT_TYPE | NAME | AGE | GENDER | WEIGHT | HEIGHT | ALLERGY_HISTORY | PHONE_No | EMAIL_ID | HOSPITAL_NAME
        sqlQuery = "INSERT INTO PATIENT_DATA (CODE,PATIENT_TYPE,NAME,AGE,GENDER,WEIGHT,HEIGHT,ALLERGY_HISTORY,PHONE_No,EMAIL_ID,HOSPITAL_NAME) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (c,'G',n,a,g,w,h,'-','-','-','-')
        mycursor.execute(sqlQuery,val)

        sqlQuery1 = "INSERT INTO AMBULANCE_DATA (CODE,PATIENT_NAME,BOOKING_TYPE,HOSPITAL_NAME) VALUES (%s,%s,%s,%s)"
        valQuery1 = (c,n,'','')
        mycursor.execute(sqlQuery1,valQuery1)

        mydb.commit()
        nextpage()
    else:
        messagebox.showwarning("","Kindly enter the correct information")
def form():
    root.withdraw()
    global root3
    root3 = Toplevel(root)
    root3.geometry('600x600')
    root3.configure(bg = "LightYellow2")
    label1 = Label(root3, text = "* Enter the details of the patient *",font = ("Calibri 16"),bg = "LightYellow2").grid(row = 1, column = 1)

    nameLabel = Label(root3, text = "Name",font = ("Calibri 16"),bg = "LightYellow2").grid(row = 2, column = 0)
    nameEntry = Entry(root3, textvariable = name,font = ("Calibri 16")).grid(row = 2, column = 1)

    ageLabel = Label(root3, text = "Age",font = ("Calibri 16"),bg = "LightYellow2").grid(row = 3, column = 0)
    ageEntry = Entry(root3, textvariable = age, font = ("Calibri 16")).grid(row = 3, column = 1)

    genLabel = Label(root3, text = "Gender",font = ("Calibri 16"),bg = "LightYellow2").grid(row = 4, column = 0)
    genEntry = ttk.Combobox(root3, width = 18, textvariable = gender, font = ('Calibri 16'))
    genEntry['values'] = ('Male',
                          'Female')
    genEntry.grid(row = 4, column = 1)
    genEntry.current()

    weightLabel = Label(root3, text = "Weight in Kg",font = ("Calibri 16"),bg = "LightYellow2").grid(row = 5, column = 0)
    weightEntry = Entry(root3, textvariable = weight, font = ("Calibri 16")).grid(row = 5, column = 1)

    heightLabel = Label(root3, text = "Height in m",font = ("Calibri 16"),bg = "LightYellow2").grid(row = 6, column = 0)
    heightEntry = Entry(root3, textvariable = height, font = ("Calibri 16")).grid(row = 6, column = 1)                    

    subbtn = Button(root3, text = "Submit",font = ("Calibri 16"),bg = "ghost white",command = lambda:submit()).grid(row = 7, column = 1)

    backbtn = Button(root3, text = "Back to Main Menu",font = ("Calibri 10"),bg = "ghost white",command = lambda:back()).place(x = 480, y = 0)   

def user():
    fr = open("guestFlag.txt","r")
    flag = fr.read()
    fr.close()

    #setting the booking type to be 'M'. M standing for MYSELF
    fw = open("booking_type.txt","w")
    fw.write('M')
    fw.close()

    if(flag == "1"):
        messagebox.showinfo("Patient Data Entry","As you have logged in as a guest, please fill the form that would be displayed shortly")
        form()
    else:
        nextpage()
    
def nonuser():
    fr = open("guestFlag.txt","r")
    flag = fr.read()
    fr.close()

    #setting the booking type to be 'S'. S standing for SOMEONE

    fw = open("booking_type.txt","w")
    fw.write('S')
    fw.close()

    if(flag == "1"):
        messagebox.showinfo("Patient Data Entry","Patient Details haven't been registered, kindly enter patient details")
        form()
    else:
        nextpage()
    
title = Label(root,text = "AMBULANCE BOOKING MAIN MENU",font = ("Calibri 20"),bg = "coral1",fg = "purple").place(x = 110, y = 150)
btn1 = Button(root,text = "🚑 Book for myself ",font = ("Calibri 16"),bg = "white",command = lambda:user()).place(x = 100, y = 225)
btn2 = Button(root,text = "🚑 Book for someone",font = ("Calibri 16"),bg = "white",command = lambda:nonuser()).place(x = 315, y = 225)

root.mainloop()
