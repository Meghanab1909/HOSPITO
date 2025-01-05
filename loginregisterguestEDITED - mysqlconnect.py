from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
import random
import os

mydb = mysql.connector.connect(host = 'localhost',passwd = '1234',user = 'root',database = 'hospitalmanagement')

mycursor = mydb.cursor()

#creating database
#mycursor.execute("CREATE DATABASE HospitalManagement")

#creating table
'''
patientData = """CREATE TABLE PATIENT_DATA(
                 CODE VARCHAR(5) PRIMARY KEY,
                 PATIENT_TYPE VARCHAR(10) NOT NULL,
                 NAME VARCHAR(50) NOT NULL,
                 AGE INT NOT NULL,
                 GENDER VARCHAR(20) NOT NULL,
                 WEIGHT FLOAT NOT NULL,
                 HEIGHT FLOAT NOT NULL,
                 ALLERGY_HISTORY VARCHAR(50) NOT NULL,
                 PHONE_No VARCHAR(10) NOT NULL,
                 EMAIL_ID VARCHAR(50) NOT NULL,
                 HOSPITAL_NAME VARCHAR(50) NOT NULL
                 )"""
mycursor.execute(patientData)
'''  
''' 
AmbData = """CREATE TABLE AMBULANCE_DATA(
             CODE VARCHAR(5) PRIMARY KEY,
             PATIENT_NAME  VARCHAR(50) NOT NULL,
             BOOKING_TYPE VARCHAR(5) NOT NULL,
             HOSPITAL_NAME VARCHAR(50) NOT NULL
             )"""
mycursor.execute(AmbData)
'''

def register_user():
    n=name.get() 
    p=password.get()
    a = age.get()
    g = gender.get()
    w = weight.get()
    h = height.get()
    al = allergy.get()
    ph = phoneNo.get()
    e = email.get()

    '''n_entry.delete(0, END)
    p_entry.delete(0, END)'''
            
    #Checking if it is a valid email
    flag = 0
    for i in e:
        if(i == '@'):
            flag += 1
    
    '''flag2 = 0
    domain = ""
    for i in range(len(e)-4,len(e),1):
        domain += e[i]
    if(domain != ".com"):
        flag2 = 1'''

    counter = 0
    if(n.isdigit() is True or a.isdigit() is False or h.isalpha() is True or w.isalpha() is True or flag != 1 or e[len(e)-4:len(e)] != ".com" or len(ph) != 10):
        counter = 1
    
    if(counter != 1):
        List = [i for i in range(0000, 10000)]
        code = random.choice(List)
        c = "R"+str(code)
        
        file=open(n,"w")
        file.write(n+"\n")
        file.write(p)
        file.close()
        fileName = open("PData.txt","a")
        fileName.write(c+" "+n+" "+a+" "+g+" "+w+" "+h+" "+al+" "+ph+" "+e)
        fileName.write("\n")
        fileName.close()
        messagebox.showinfo("","Registration Successful")
        root1.withdraw()

        fileName = open("PData-access.txt","w")
        fileName.write(c+" "+n+" "+a+" "+g+" "+w+" "+h+" "+al+" "+ph+" "+e)
        fileName.write("\n")
        fileName.close()

        #python-sql connectivity
        sqlQuery = "INSERT INTO PATIENT_DATA (CODE,PATIENT_TYPE,NAME,AGE,GENDER,WEIGHT,HEIGHT,ALLERGY_HISTORY,PHONE_NO,EMAIL_ID,HOSPITAL_NAME) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (c,'R',n,a,g,w,h,al,ph,e,'-')
        mycursor.execute(sqlQuery,val)
        
        sqlQuery1 = "INSERT INTO AMBULANCE_DATA (CODE,PATIENT_NAME,BOOKING_TYPE,HOSPITAL_NAME) VALUES (%s,%s,%s,%s)"
        valQuery1 = (c,n,'','')
        mycursor.execute(sqlQuery1,valQuery1)

        mydb.commit()

        login()
    else:
        messagebox.showwarning("","Kindly enter correct information")
    
def login_verify():
    name1=name_verify.get()
    password1=password_verify.get()
    '''n_entry1.delete(0, END)
    p_entry1.delete(0, END)'''
    list_of_files=os.listdir()
    if name1 in list_of_files:
        file1=open(name1,"r")
        verify=file1.read().splitlines()
        if password1 in verify:
            messagebox.showinfo("info","Login Successfull!!")
            guestfile = open("guestFlag.txt","w")
            guestfile.write("0")
            guestfile.close()
            root.destroy()
            os.startfile('amb1 - mysqlconnect.py')
        else:
            messagebox.showinfo("info","Password has not been recognised")
    else:
        messagebox.showinfo("info","User not found")
        
def guest():
    guestfile = open("guestFlag.txt","w")
    guestfile.write("1")
    guestfile.close()
    os.startfile("amb1 - mysqlconnect.py")
    root.destroy()

def back2():
    root1.destroy()
    mainscreen()
    
def register():
    global name,password,age,gender,weight,height,email,phoneNo,allergy
    global n_entry,p_entry,a_entry,g_entry,w_entry,h_entry,e_entry,ph_entry,root1,al_entry
    
    root1=Toplevel(root)
    name=StringVar()
    password=StringVar()
    age=StringVar()
    gender=StringVar()
    weight=StringVar()
    height=StringVar()
    email=StringVar()
    phoneNo=StringVar()
    allergy=StringVar()
    
    root1.title("Register")
    root1.geometry("600x600")
    root1.configure(bg = "powderblue")
    Label(root1,text="REGISTRATION",font=("Calibri 20"),bg = "powderblue",foreground = "SlateBlue4").grid(row = 0,column = 1)
    Label(root1, text = "Please enter the following details of the patient",font=("Calibri 14"),bg = "powderblue").grid(row = 1, column = 1)
    
    Label(root1,text="Name",font=("Calibri 16"),bg = "powderblue").grid(row = 3, column = 0)
    n_entry=Entry(root1,textvariable=name,font = ("Calibri 16")).grid(row = 3, column = 1)    

    Label(root1, text = "Age",font = ("Calibri 16"),bg = "powderblue").grid(row = 4, column = 0)
    a_entry=Entry(root1, textvariable=age,font = ("Calibri 16")).grid(row = 4, column = 1)

    Label(root1, text = "Gender",font = ("Calibri 16"),bg = "powderblue").grid(row = 5, column = 0)
    #g_entry=Entry(root1, textvariable=gender,font = ("Calibri 16")).grid(row = 5, column = 1)
    g_entry = ttk.Combobox(root1, width = 18, textvariable = gender, font = ('Calibri 16'))
    g_entry['values'] = ('Male',
                    'Female')
    g_entry.grid(row = 5, column = 1)
    g_entry.current()

    Label(root1, text = "Allergy History",font = ("Calibri 16"),bg = "powderblue").grid(row = 6, column = 0)
    al_entry = ttk.Combobox(root1, width = 18, textvariable = allergy,font = ("Calibri 16"))
    al_entry['values'] = ('Foods',
                          'Animals',
                          'Pollen',
                          'Mold',
                          'Dust',
                          'Mites',
                          'Medications',
                          'Latex',
                          'Insect Stings',
                          'Cockroaches',
                          'Perfumes/Household Chemicals',
                          'None')
    al_entry.grid(row = 6, column = 1)
    al_entry.current()
    
    Label(root1, text = "Weight in Kg",font = ("Calibri 16"),bg = "powderblue").grid(row = 7, column = 0)
    w_entry=Entry(root1, textvariable = weight,font = ("Calibri 16")).grid(row = 7, column = 1)

    Label(root1, text = "Height in m",font = ("Calibri 16"),bg = "powderblue").grid(row = 8, column = 0)
    h_entry=Entry(root1, textvariable = height, font = ("Calibri 16")).grid(row = 8, column = 1)
    
    Label(root1, text = "Please enter the following accounting details",font = ("Calibri 14"),bg = "powderblue").grid(row = 10, column = 1)
    Label(root1,text="Password",font=("Calibri 16"),bg = "powderblue").grid(row = 11, column = 0)
    p_entry=Entry(root1,textvariable=password,font = ("Calibri 16"),show = "*").grid(row = 11, column = 1)

    Label(root1, text = "Email",font = ("Calibri 16"),bg = "powderblue").grid(row = 12, column = 0)
    e_entry=Entry(root1,textvariable = email,font = ("Calibri 16")).grid(row = 12, column = 1)

    Label(root1, text = "Phone No.",font = ("Calibri 16"),bg = "powderblue").grid(row = 13, column = 0)
    ph_entry=Entry(root1, textvariable = phoneNo,font = ("Calibri 16")).grid(row = 13, column = 1)
    
    button=Button(root1,text="Register",command=lambda:register_user(),font=("Calibri 16"),bg = "white").grid(row = 15, column = 1)
    backbtn=Button(root1,text="Back to Main Menu",command=lambda:back2(),font=("Calibri 10")).place(x = 480, y = 0)
    root.withdraw()
    root1.mainloop()

def back1():
    root2.destroy()
    mainscreen()
    
def login():
    global root2,n_entry1,p_entry1
    global name_verify,password_verify
    
    name_verify=StringVar()
    password_verify=StringVar()
    
    root2=Toplevel(root)
        
    root2.geometry("600x600")
    root2.configure(bg="light blue")
    root2.title("Login")
    
    Label(root2, text = "LOGIN",font = ("Calibri 20"),bg = "light blue",foreground = "dark blue").pack()
    Label(root2,text="Name of Patient",font = ("Calibri 16"),bg = "light blue").pack()
    n_entry1=Entry(root2,textvariable=name_verify,font = ("Calibri 16")).pack()
    
    Label(root2,text="Password",font=("Calibri 16"),bg = "light blue").pack()
    p_entry1=Entry(root2,textvariable=password_verify,font = ("Calibri 16"),show="*").pack()

    Label(root2,text=" ",font = ("Calibri 16"),bg = "light blue").pack()
                                                          
    button1=Button(root2,text="Login",command=lambda:login_verify(),font=("Calibri 14"),bg = "white").pack()
    backbtn=Button(root2, text = "Back to Main Menu",command=lambda:back1(),font=("Calibri 10")).place(x = 480,y = 0)
    
    root.withdraw()
    root2.mainloop()

def mainscreen():
    global root,screen_w,screen_h,x,y
    root=Tk()
    screen_w=root.winfo_screenwidth()
    screen_h=root.winfo_screenheight()
    
    root.geometry("600x600")
    root.title("Register-Login")
    root.configure(bg="LightBlue1")
    heading=Label(root,text="REGISTER/LOGIN PAGE",font=("Calibri 20"),bg = "LightBlue1",foreground = "RoyalBlue4").place(x = 190, y = 150)
    
    login_button=Button(root,text="Login",font=("Calibri 16"),command=lambda:login(),bg = "white").place(x = 150, y = 200)

    register_button=Button(root,text="Register",font=("Calibri 16"),command=lambda:register(),bg = "white").place(x = 220, y = 200)

    guest_button=Button(root,text="Check in as Guest",font=("Calibri 16"),command=lambda:guest(),bg = "white").place(x = 312, y = 200)

    root.mainloop()
mainscreen()
