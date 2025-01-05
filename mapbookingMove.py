import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
import random
import os

root = tk.Tk()
root.geometry('800x800')
root.title('Map Booking')

bg = PhotoImage(file = "C:\\Users\\ramab\\OneDrive\\Desktop\\MEGHANA\\XII PROJECTS\\COMPUTER XII\\Screenshot 2022-03-25 152908 map - Copy.png")
label1 = Label( root, image = bg)
label1.place(x = 0,y = 0)

stloc = StringVar()
edloc = StringVar()

name = ["Selby Theo Devin","Tory Darryl Dean","Joseph Vincent","Anoop Ganesh","Shrek","Arjun Rajesh","Siddarth Jayendra Devi","Dinesh Hari D'Cruz","Mohammad Inayat Zaman","Zawar Dilshad Muhammad","Deep Ravi Bachchan","Pran Narayan Kumar","Subramanyam Rishi Shetty","Raza Babur Mohammad","Daniel K Shekhar"]
phoneNo = random.randint(1000000000,5000000000)
index = random.randint(0,(len(name)-1))

mydb = mysql.connector.connect(host = 'localhost',user = 'root',passwd = '1234',database = 'hospitalmanagement')

mycursor = mydb.cursor()


def click10(label1,label2):
    label1.destroy()
    label2.destroy()
    hide10.destroy()

def northblorehospital():
    global hide10
    label1 = Label(root,text = "Kalyananagara, SY No.104, 4th, \nG Street, 125/1,\n125/2, Kalyan\nResidency Road\n091643 99999",font = ("Calibri 12"),bg = "honeydew2")
    label1.place(x = 320,y = 490)
    label2 = Label(root,text = "25 min (8.0 km) via 1st Main Rd",font = ("Calibri 12"),bg = "LavenderBlush2")
    label2.place(x = 320,y = 570)
    hide10 = Button(root,text = "Hide",font = ("Calibri 12"),bg = "white",command = lambda:click10(label1,label2))
    hide10.place(x = 400, y = 592)

def click9(label1,label2):
    label1.destroy()
    label2.destroy()
    hide9.destroy()
    
def chirayuhospital():
    global hide9
    label1 = Label(root,text = "6/8, Anjaneya Temple, Thanisandra Main\nRd,\n080 2544 5444",font = ("Calibri 12"),bg = "honeydew2")
    label1.place(x = 5, y = 300)
    label2 = Label(root,text = "16 min (6.3 km) via 1st Main Rd/Hennur\nMain Rd/New Airport Rd, K Narayanapura\nMain Rd and Thanisandra Main Rd",font = ("Calibri 12"),bg = "LavenderBlush2")
    label2.place(x = 5,y = 360)
    hide9 = Button(root,text = "Hide",font = ("Calibri 12"),bg = "white",command = lambda:click9(label1,label2))
    hide9.place(x = 120, y = 420)
        
def click8(label1,label2):
    label1.destroy()
    label2.destroy()
    hide8.destroy()
    
def manoharhospital():
    global hide8
    label1 = Label(root,text = "KHB Colony Main Road, No 1, 1st\nCross Rd,Sultanpalya, RT Nagar\n080 2365 6464",font = ("Calibri 12"),bg = "honeydew2")
    label1.place(x = 0, y = 570)
    label2 = Label(root,text = "34 min (11.6 km) via 1st Main Rd",font = ("Calibri 12"),bg = "LavenderBlush2")
    label2.place(x = 0, y = 670)
    hide8 = Button(root,text = "Hide",font = ("Calibri 12"),bg = "white",command = lambda:click8(label1,label2))
    hide8.place(x = 80, y = 695)
        
def click7(label1,label2):
    label1.destroy()
    label2.destroy()
    hide7.destroy()

def JMJhospital():
    global hide7
    label1 = Label(root,text = "Philomena Hospital Rd, Vyalikaval\nHBCS Layout,Nagavara\n080 2544 1768",font = ("Calibri 12"),bg = "honeydew2")
    label1.place(x = 250, y = 500)
    label2 = Label(root,text = "21 min (7.9 km) via 1st Main Rd/\nNew Airport Rd",font = ("Calibri 12"),bg = "LavenderBlush2")
    label2.place(x = 250, y = 560)
    hide7 = Button(root,text = "Hide",font = ("Calibri 12"),bg = "white",command = lambda:click7(label1,label2))
    hide7.place(x = 468, y = 560)

def click6(label1,label2):
    label1.destroy()
    label2.destroy()
    hide6.destroy()
        
def cratishospital():
    global hide6
    label1 = Label(root,text = "Geddalahalli, 4-4/1, 1st Main Rd, \nBanjara Residency,\nKothanur\n088844 11041",font = ("Calibri 12"),bg = "honeydew2")
    label1.place(x = 430,y = 300)
    label2 = Label(root,text = "10 min (4.5 km) via 1st Main Rd/  \nNew Airport Rd",font = ("Calibri 12"),bg = "LavenderBlush2")
    label2.place(x = 430,y = 380)
    hide6 = Button(root,text = "Hide",font = ("Calibri 12"),bg = "white",command = lambda:click6(label1,label2))
    hide6.place(x = 515,y = 424)
        
def click5(label1,label2):
    label1.destroy()
    label2.destroy()
    hide5.destroy()
    
def koshyhospital():
    global hide5
    label1 = Label(root,text = "127, 7th Main Rd, Raghavendra Nagar,\nRamamurthy Nagar\n084312 22444",font = ("Calibri 12"),bg = "honeydew2")
    label1.place(x = 500, y = 530)
    label2 = Label(root,text = "26 min (11.7 km) via K Channasandra  \nMain Rd",font = ("Calibri 12"),bg = "LavenderBlush2")
    label2.place(x = 500, y = 590)
    hide5 = Button(root,text = "Hide",font = ("Calibri 12"),bg = "white",command = lambda:click5(label1,label2))
    hide5.place(x = 610, y = 635)

def click4(label1,label2):
    label1.destroy()
    label2.destroy()
    hide4.destroy()
        
def saihospital():
    global hide4
    label1 = Label(root,text = "2nd Main Rd, 2nd Phase, Sri Balaji Krupa \nLayout\nRK Hegde Nagar\n080 2844 3062",font = ("Calibri 12"),bg = "honeydew2")
    label1.place(x = 5, y = 200)
    label2 = Label(root,text = "11 min (4.3 km) via Thanisandra Main Rd",font=("Calibri 12"),bg = "LavenderBlush2")
    label2.place(x = 5, y = 280)
    hide4 = Button(root,text = "Hide",font = ("Calibri 12"),bg = "white",command = lambda:click4(label1,label2))
    hide4.place(x = 125, y = 305)

def click3(label1,label2):
    label1.destroy()
    label2.destroy()
    hide3.destroy()
        
def royalhospital():
    global hide3
    label1 = Label(root,text = "1st Main Rd, Chikkagubbi Village\n080 2846 5401",font = ("Calibri 12"),bg = "honeydew2")
    label1.place(x = 450, y = 240)
    label2 = Label(root,text = "3 min (900.0 m) via 1st Main Rd/\nHennur Main Rd/New Airport Rd",font = ("Calibri 12"),bg = "LavenderBlush2")
    label2.place(x = 450,y = 280)
    hide3 = Button(root,text = "Hide",font = ("Calibri 12"),bg = "white",command = lambda:click3(label1,label2))
    hide3.place(x = 550, y = 320)

def click2(label1,label2):
    label1.destroy()
    label2.destroy()
    hide2.destroy()
        
def regalhospital():
    global hide2
    label1 = Label(root,text = "No 30, CMR, Complex,Thanisandra\nMain Rd\n088840 58888",font = ("Calibri 12"),bg = "honeydew2")
    label1.place(x = 45, y = 75)
    label2 = Label(root,text = "8 min (2.8 km) via 1st Main Rd/     \nHennur Main Rd/New Airport Rd",font = ("Calibri 12"),bg = "LavenderBlush2")
    label2.place(x = 45, y = 135)
    hide2 = Button(root,text = "Hide",font = ("Calibri 12"),bg = "white",command = lambda:click2(label1,label2))
    hide2.place(x = 140, y = 178)

def click1(label1,label2):
    label1.destroy()
    label2.destroy()
    hide1.destroy()
        
def ashwinihospital():
    global hide1
    label1 = Label(root,text = "Yelahanka Old Town, Opp B.D.K.\nKalyana Mandapa,\nNehru Nagar\n08042103880",font = ("Calibri 12"),bg = "honeydew2")
    label1.place(x = 8, y = 70)
    label2 = Label(root,text = "17 min (8.1 km) via Kogilu Main\nRd",font = ("Calibri 12"),bg = "LavenderBlush2")
    label2.place(x = 8, y = 130)
    hide1 = Button(root,text = "Hide",font = ("Calibri 12"),bg = "white",command = lambda:click1(label1,label2))
    hide1.place(x = 90, y = 172)

def nextpage():
    os.startfile('exit.py')
    root.destroy()
    
#Tracking Simulation PNG images
img_1 = PhotoImage(name = "img1",file = "C:\\Users\\ramab\\OneDrive\Desktop\MEGHANA\XII PROJECTS\COMPUTER XII\Screenshot 2022-05-05 133407.png")
img_2 = PhotoImage(name = "img2",file = "C:\\Users\\ramab\\OneDrive\\Desktop\\MEGHANA\\XII PROJECTS\\COMPUTER XII\\Screenshot 2022-05-05 135121.png")
img_3 = PhotoImage(name = "img3",file = "C:\\Users\\ramab\\OneDrive\\Desktop\\MEGHANA\\XII PROJECTS\\COMPUTER XII\\Screenshot 2022-05-05 134511.png")
img_4 = PhotoImage(name = "img4",file = "C:\\Users\\ramab\\OneDrive\\Desktop\\MEGHANA\\XII PROJECTS\\COMPUTER XII\\Screenshot 2022-05-05 134924.png")
img_5 = PhotoImage(name = "img5",file = "C:\\Users\\ramab\\OneDrive\\Desktop\\MEGHANA\\XII PROJECTS\\COMPUTER XII\\image0[3860].png")
img_6 = PhotoImage(name = "img6",file = "C:\\Users\\ramab\\OneDrive\\Desktop\\MEGHANA\\XII PROJECTS\\COMPUTER XII\\Screenshot 2022-05-03 065315.png")    
img_7 = PhotoImage(name = "img7",file = "C:\\Users\\ramab\\OneDrive\\Desktop\\MEGHANA\\XII PROJECTS\\COMPUTER XII\\Screenshot 2022-05-03 063544 - Copy.png")
img_8 = PhotoImage(name = "img8",file = "C:\\Users\\ramab\\OneDrive\\Desktop\\MEGHANA\\XII PROJECTS\\COMPUTER XII\\Screenshot 2022-05-03 070003 - Copy.png")    
img_9 = PhotoImage(name = "img9",file = "C:\\Users\\ramab\\OneDrive\\Desktop\\MEGHANA\\XII PROJECTS\\COMPUTER XII\\Screenshot 2022-05-03 061135 - Copy.png")
img_10 = PhotoImage(name = "img10",file = "C:\\Users\\ramab\\OneDrive\\Desktop\\MEGHANA\\XII PROJECTS\\COMPUTER XII\\Screenshot 2022-05-03 070539 - Copy.png")
def track():
    global root1,code
    root1 = tk.Toplevel(root)
    root1.geometry("635x610")
    root1.title("Route between start and end location")
    label = Label(root1)

    fr = open("guestFlag.txt","r")
    ln = fr.read()
    fr.close()

    if(ln == "1"):
        fr = open("flag2.txt","r")
    else:
        fr = open("PData-access.txt","r")
    ln = fr.readline().split()
    code = ln[0]
    
    display = Label(root1,text = 'Code:'+" "+str(code),font = ("Calibri 11"),bg = 'alice blue').pack()
    #First 5 hospitals to be added here
    if(x == 1):
        label = Label(root1, image = img_1, bd = 5, relief = FLAT)
    elif(x == 2):
        label = Label(root1, image = img_2, bd = 5, relief = FLAT)
    elif(x == 3):
        label = Label(root1, image = img_3, bd = 5, relief = FLAT)
    elif(x == 4):
        label = Label(root1, image = img_4, bd = 5, relief = FLAT)
    elif(x == 5):
        label = Label(root1, image = img_5, bd = 5, relief = FLAT)
    elif(x == 6):
        label = Label(root1, image = img_6, bd = 5, relief = FLAT)
    elif(x == 7):
        label = Label(root1, image = img_7, bd = 5, relief = FLAT)
    elif(x == 8):
        label = Label(root1, image = img_8, bd = 5, relief = FLAT)
    elif(x == 9):
        label = Label(root1, image = img_9, bd = 5, relief = FLAT)
    elif(x == 10):
        label = Label(root1, image = img_10, bd = 5, relief = FLAT)
    label.pack()
    note = Label(root1, text = "Kindly click exit on\nreaching the\nhospital",font = ("Calibri 11"), bg = "white")
    note.place(x = 512, y = 0)

    driverdetails = Label(root1, text = "DRIVER DETAILS\nName: "+name[index]+"\nPhone Number: "+str(phoneNo)+"\nETA: "+eta,font = ("Calibri 12"),bg = "light salmon")
    driverdetails.place(x = 0, y = 0)
    
    nextBtn = Button(root1,text = "Exit",font = ("Calibri 11"),command = lambda:nextpage()).place(x = 555,y = 60)
     
def SET():
    global x,eta
    #sending request

    x = 0

    fr = open("guestFlag.txt","r")
    flag = fr.read()
    fr.close()

    if(flag == "1"):
        fr = open("flag2.txt","r")
    else:
        fr = open("PData-access.txt","r")
    ln = fr.readline().split()
    code = ln[0]
    
    if(edloc.get() == "Ashwini Hospital"):
        x = 1
        eta = "18-24 minutes"
    elif(edloc.get() == "Regal Hospital"):
        x = 2
        eta = "8-14 minutes"
    elif(edloc.get() == "Royal Care Hospital"):
        x = 3
        eta = "3-5 minutes"
    elif(edloc.get() == "Sai Hospital"):
        x = 4
        eta = "11-15 minutes"
    elif(edloc.get() == "KOSHY Hospital"):
        x = 5
        eta = "22-28 minutes"
    elif(edloc.get() == "Cratis Hospital"):
        x = 6
        eta = "7-11 minutes"
    elif(edloc.get() == "JMJ Hospital"):
        x = 7
        eta = "16-24 minutes"
    elif(edloc.get() == "Manohar Hospital"):
        x = 8
        eta = "34-50 minutes"
    elif(edloc.get() == "Chirayu Hospital"):
        x = 9
        eta = "16-20 minutes"
    elif(edloc.get() == "North Bangalore Hospital"):
        x = 10
        eta = "25-35 minutes"

    hospital = edloc.get()
    if(x == 0):
        messagebox.showwarning("","Kindly choose a hospital and click SET")
    else:
        #Updating hospital name in patient data sql table
        sqlQ = "UPDATE PATIENT_DATA SET HOSPITAL_NAME = %s WHERE CODE = %s"
        valQ = (hospital,code)
        mycursor.execute(sqlQ,valQ)

        #Updating booking type in ambulance data sql table
        fr = open("booking_type.txt","r")
        b = fr.read()
        fr.close()

        sqlQ2 = "UPDATE AMBULANCE_DATA SET BOOKING_TYPE = %s WHERE CODE = %s"
        valQ2 = (b,code)
        mycursor.execute(sqlQ2,valQ2)

        #Updating hospital name in ambulance data sql table
        sqlQ3 = "UPDATE AMBULANCE_DATA SET HOSPITAL_NAME = %s WHERE CODE = %s"
        valQ3 = (hospital,code)
        mycursor.execute(sqlQ3,valQ3)

        mydb.commit()
        
        messagebox.showinfo("Request Sent","Request has been sent, it shall be accepted soon. Kindly wait")
        messagebox.showinfo("Request Accepted","Your request has been accepted")
        root.withdraw()
        track()

startLabel = Label(root,text = "📍 Start Location",font = ("Calibri 16")).place(x = 420, y = 0)                                                                          
startEntry = Entry(root,textvariable = stloc, font = ("Calibri 16")).place(x = 575, y = 0)

endLabel = Label(root, text = "    📍 Hospital         ",  font = ("Calibri 16")).place(x = 420, y = 30)
hospitalbox = ttk.Combobox(root, width = 18, textvariable = edloc, font = ('Calibri 16'))
hospitalbox['values'] = ('Ashwini Hospital',
                         'Regal Hospital',
                         'Royal Care Hospital',
                         'Sai Hospital',
                         'KOSHY Hospital',
                         'Cratis Hospital',
                         'JMJ Hospital',
                         'Manohar Hospital',
                         'Chirayu Hospital',
                         'North Bangalore Hospital')
hospitalbox.place(x = 575, y = 30)
hospitalbox.current()

fr = open("guestFlag.txt","r")
ln = fr.read()
fr.close()

if(ln == "1"):
    fr = open("flag2.txt","r")
else:
    fr = open("PData-access.txt","r")
ln = fr.readline().split()
code = ln[0]

display = Label(root,text = 'Code:'+" "+str(code),font = ("Calibri 12"),bg = 'alice blue').place(x = 0,y = 0)

setbtn = Button(root,text = "Set",font = ("Calibri 16"),bg = "white",command = lambda:SET()).place(x = 650, y = 63)

shriramluxor = Label(root,text = "⌂",font = ("Calibri 21"),bg = "dark blue",fg = "white").place(x = 465, y = 140)

AshwiniHospital = Button(root,text = "⚕",font = ("Calibri 14"),bg = "red",fg = "white",command = lambda:ashwinihospital()).place(x = 0, y = 28)

RegalHospital = Button(root,text = "⚕",font = ("Calibri 14"),bg = "red",fg = "white",command = lambda:regalhospital()).place(x = 295, y = 155)

RoyalHospital = Button(root,text = "⚕",font = ("Calibri 14"),bg = "red",fg = "white",command = lambda:royalhospital()).place(x = 445,y=200)

SaiHospital = Button(root,text = "⚕",font = ("Calibri 14"),bg = "red",fg = "white",command = lambda:saihospital()).place(x = 280, y = 265)

KoshyHospital = Button(root,text = "⚕",font = ("Calibri 14"),bg = "red",fg = "white",command = lambda:koshyhospital()).place(x = 630,y = 670)

CratisHospital = Button(root,text = "⚕",font = ("Calibri 14"),bg = "red",fg = "white",command = lambda:cratishospital()).place(x = 380, y = 445)

JMJHospital = Button(root,text = "⚕",font = ("Calibri 14"),bg = "red",fg = "white",command = lambda:JMJhospital()).place(x = 210,y = 512)

ManoharHospital = Button(root,text = "⚕",font = ("Calibri 14"),bg = "red",fg = "white",command = lambda:manoharhospital()).place(x = 40, y = 630)

ChirayuHospital = Button(root,text = "⚕",font = ("Calibri 14"),bg = "red",fg = "white",command = lambda:chirayuhospital()).place(x = 280, y = 412)

northbloreHospital = Button(root,text = "⚕",font = ("Calibri 14"),bg = "red",fg = "white",command = lambda:northblorehospital()).place(x = 330,y = 620)

root.mainloop()

