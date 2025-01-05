import tkinter as tk
from tkinter import *
from tkinter import ttk
import mysql.connector

mydb = mysql.connector.connect(host = 'localhost',user = 'root',passwd = '1234',database = 'hospitalmanagement')

mycursor = mydb.cursor()

root = tk.Tk()
root.geometry('600x600')
root.title('Exit Page')

root.configure(bg = 'alice blue')

fr = open("guestFlag.txt","r")
ln = fr.read()
fr.close()

if(ln == "1"):
    fr = open("flag2.txt","r")
else:
    fr = open("PData-access.txt","r")
ln = fr.readline().split()
code = ln[0]

def exitPage():
    root1.destroy()
    root.deiconify()

def reportData():
    root.withdraw()
    global root1
    root1 = Toplevel(root)
    root1.geometry('600x600')
    root1.configure(bg = 'alice blue')

    #Ambulance data
    rows = IntVar()
    rowsM = IntVar()
    rowsS = IntVar()

    Label(root1,text = "OVERVIEW OF USERS USING AUXILIO",font = ("Calibri 20"),bg = "alice blue").place(x = 110, y = 0)

    Label(root1,text = "",font = ("Calibri 18"),bg = "alice blue").grid(row = 1, column = 0)
    
    Label(root1,text = 'Ambulance Data',font = ('Calibri 16 underline'),bg = 'alice blue').grid(row = 2, column = 1)

    #Formatting to be done here
    query = "select *from ambulance_data"
    mycursor.execute(query)
    data = mycursor.fetchall()
    rows.set(mycursor.rowcount)

    Label(root1,text = "Total No.of patients:",font = ("Calibri 13"),bg = 'alice blue').grid(row = 3, column = 0)
    Label(root1,textvariable = rows,font = ("Calibri 13"),bg = 'alice blue').grid(row = 3, column = 2)

    query = "select *from ambulance_data where BOOKING_TYPE = %s"
    b = ["M"]
    mycursor.execute(query,b)
    data = mycursor.fetchall()
    rowsM.set(mycursor.rowcount)

    Label(root1,text = "No.of patients (Myself):",font = ("Calibri 13"),bg = "alice blue").grid(row = 4, column = 0)
    Label(root1,textvariable = rowsM,font = ("Calibri 13"),bg = "alice blue").grid(row = 4, column = 2)

    query = "select *from ambulance_data where BOOKING_TYPE = %s"
    b = ["S"]
    mycursor.execute(query,b)
    data = mycursor.fetchall()
    rowsS.set(mycursor.rowcount)

    Label(root1,text = "No.of patients (Someone):",font = ("Calibri 13"),bg = "alice blue").grid(row = 5, column = 0)
    Label(root1,textvariable = rowsS,font = ("Calibri 13"),bg = "alice blue").grid(row = 5, column = 2)



    backbtn = Button(root1,text = "Back",font = ("Calibri 10"),command = lambda:exitPage()).place(x = 563,y = 0)

    #Patient Data
    Trows = IntVar()
    rowsG = IntVar()
    rowsR = IntVar()

    Label(root1,text = "Patient Data",font = ("Calibri 16 underline"),bg = 'alice blue').grid(row = 7, column = 1)

    #Formatting to be done here
    query = "select *from patient_data"
    mycursor.execute(query)
    data = mycursor.fetchall()
    Trows.set(mycursor.rowcount)

    Label(root1,text = "Total No.of patients:",font = ("Calibri 13"),bg = 'alice blue').grid(row = 8, column = 0)
    Label(root1,textvariable = Trows,font = ("Calibri 13"),bg = 'alice blue').grid(row = 8, column = 2)

    query = "select *from patient_data where PATIENT_TYPE = %s"
    b = ["R"]
    mycursor.execute(query,b)
    data = mycursor.fetchall()
    rowsR.set(mycursor.rowcount)

    Label(root1,text = "No.of patients (Registered):",font = ("Calibri 13"),bg = "alice blue").grid(row = 9, column = 0)
    Label(root1,textvariable = rowsR,font = ("Calibri 13"),bg = "alice blue").grid(row = 9, column = 2)

    query = "select *from patient_data where PATIENT_TYPE = %s"
    b = ["G"]
    mycursor.execute(query,b)
    data = mycursor.fetchall()
    rowsG.set(mycursor.rowcount)

    Label(root1,text = "No.of patients (Guest):",font = ("Calibri 13"),bg = "alice blue").grid(row = 10, column = 0)
    Label(root1,textvariable = rowsG,font = ("Calibri 13"),bg = "alice blue").grid(row = 10, column = 2)
    
        
display = Label(root,text = 'PCode/GPCode:'+" "+str(code),font = ("Calibri 12"),bg = 'alice blue').place(x = 0,y = 0)

label = Label(root,text = 'Thank you for choosing\nAuxilio',font = ("Finnmark 30"),bg = 'alice blue').place(x = 100,y = 200)

Btn = Button(root,text = "   Overview   ",font = ("Calibri 12"),command = lambda:reportData()).place(x = 0,y = 25)

root.mainloop()
