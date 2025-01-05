from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from queue import PriorityQueue


import os

#creating the first window for hospito
firstroot = Tk()
firstroot.geometry('600x600')
firstroot.title("Hospito Main Menu")
firstroot.configure(bg = "lightblue")


'''em_queue = PriorityQueue()
emergencies = ["gunshot","cerebral damage","electrocution","fire damage","cardiac arrest"]
priorities = [2,3,1,5,4]
times = [15,14,16,18,12]
temp = []
'''
emergency = StringVar()

sp = Label(firstroot,text = "",bg = "lightblue").pack()
sp = Label(firstroot,text = "",bg = "lightblue").pack()
sp = Label(firstroot,text = "",bg = "lightblue").pack()
sp = Label(firstroot,text = "",bg = "lightblue").pack()

title = Label(firstroot,text = "HOSPITO",font = ("Calibri 42"),bg = "lightblue",fg = "black").pack()
sp = Label(firstroot,text = "",bg = "lightblue").pack()
#sp = Label(firstroot,text = "",bg = "lightblue").pack()
sp = Label(firstroot,text = "Enter hospital name",bg = "lightblue",font = ("Calibri 20")).pack()

hospitalentry = ttk.Combobox(firstroot, width = 15, textvariable = emergency, font = ('Calibri 17'))
hospitalentry['values'] = ('Ashwini Hospital',
'Regal Hospital',
'Royal Care Hospital',
'Sai Hospital',
'KOSHY Hospital',
'Cratis Hospital',
'JMJ Hospital',
'Manohar Hospital',
'Chirayu Hospital',
'North Bangalore Hospital')
hospitalentry.set( "Ashwini Hospital")
hospitalentry.pack()

sp = Label(firstroot,text = "",bg = "lightblue").pack()
sp = Label(firstroot,text = "",bg = "lightblue").pack()
btn1 = Button(firstroot,text = "          Next            ",font = ("Calibri 17"),fg = "black",command = lambda:rootwindow()).pack()

temp = []

def rootwindow():
    global root
    root = Tk()
    root.geometry('600x600')
    root.title("Hospito Main Menu")
    root.configure(bg = "lightblue")
   
    global  hospital
    hospital=hospitalentry.get()
    print(hospital)
    em_queue = PriorityQueue()
    #Ensuring that hospital name selected here is same as hospital in sql
    emergencies = ["Gunshot",
                                "Cerebral Damage",
                                "Electrocution",
                                "Fire Damage",
                                "Cardiac Arrest"]
    priorities = [2,3,1,5,4]
    times = [15,14,16,18,12]
    temp = []

    emergency = StringVar()

    def backAddPatient():
        root3.withdraw()
        root.deiconify()
        

    def addpatient():
        global root3
        root.withdraw()
        root3 = Toplevel(root)
        root3.geometry('600x600')
        root3.configure(bg = "lightblue")
        Label(root3, text = "Enter code",font = ("Calibri 16"),bg = "lightblue").grid(row = 0, column = 0)
        patient_code=Entry(root3,font = ("Calibri 16"))
        patient_code.grid(row=0,column=1)
        Label(root3,text = "",font = ("Calibri 18"),bg = "lightblue").grid(row = 2, column = 0)
        Label(root3, text = "Select Emergency",font = ("Calibri 16"),bg = "lightblue").grid(row = 3, column = 0)
        emg_entry = ttk.Combobox(root3, width = 18, textvariable = emergency, font = ('Calibri 16'))
        emg_entry['values'] = ("Gunshot",
                                "Cerebral Damage",
                                "Electrocution",
                                "Fire Damage",
                                "Cardiac Arrest")

        emg_entry.grid(row = 3, column = 1)
        emg_entry.current()
        Label(root3,text = "",font = ("Calibri 18"),bg = "lightblue").grid(row = 4, column = 0)
        btn1 = Button(root3,text = "    Next    ",font = ("Calibri 17"),fg = "black",command = lambda:next()).grid(row = 5, column = 1)
        btn2 = Button(root3, text = "Back to Main Menu",font = ("Calibri 10"),command = lambda:backAddPatient()).place(x = 483, y = 0)
        Label(root3,text = "",font = ("Calibri 18"),bg = "lightblue").grid(row = 6, column = 0)
        def next():
            global code
            code=patient_code.get()
            flag = True
            
            if(code == "" or code == None):
                messagebox.showinfo("","Kindly enter patient code")
                flag = False

            if(flag == True):
                print("patient code",code)

                global emergency
                emergency=emg_entry.get()
                print("emergency = ",emergency)
                
                global t
                
                t = enter()
                
                if t[1] == True:
                    Label(root3, text = "Record added successfully!",font = ("Calibri 16"),bg = "lightblue",fg = "black").grid(row = 7, column = 1)
                else :
                    Label(root3, text = "Record not found",font = ("Calibri 16"),bg = "lightblue",fg = "black").grid(row = 7, column = 1)
                
    def backWaitingTime():
        root6.withdraw()
        root.deiconify()
        
        
    def waitingtime():
        global root6
        root.withdraw()
        root6 = Toplevel(root)
        root6.geometry('600x600')
        root6.configure(bg = "lightblue")
        Label(root6, text = "Enter patient code",font = ("Calibri 16"),bg = "lightblue",fg = "black").grid(row = 0, column = 0)
        pname=Entry(root6,font = ("Calibri 16"))
        pname.grid(row=0,column=1)
        Label(root6,text = "",font = ("Calibri 16"),bg = "lightblue").grid(row = 1, column = 1)
        btn1 = Button(root6,text = "    Next     ",font = ("Calibri 16"),fg = "black",command = lambda:next()).grid(row = 2, column = 1)
        def next():
            global name
            name=pname.get()
            print("Patient Code: ",name)
            flag = True
            if(name == "" or name == None):
                messagebox.showinfo("","Kindly enter valid patient code")
                flag = False
                
            if(flag == True):
                time=search(name)
                t = StringVar()
                t = time[0]
                if(time[1] != -1):
                    Label(root6,text="",font = ("Calibri 16"),bg = "lightblue").grid(row = 4, column = 0)
                    Label(root6,text="Waiting Time:",font = ("Calibri 16"),bg = "lightblue").grid(row = 5, column = 0)
                    Label(root6, text = t,font = ("Calibri 16"),bg = "lightblue").grid(row = 5, column = 1)
                    Label(root6,text="(in minutes)",font = ("Calibri 16"),bg = "lightblue").grid(row = 6, column = 0)
                else:
                    Label(root6,text = "No such patient record exists",font = ("Calibri 16"),bg = "lightblue").grid(row = 5, column = 1)
        Button(root6,text = "Back to Main Menu",font = ("Calibri 10"),command = lambda:backWaitingTime()).place(x = 483, y = 0)

    def backsearch():
        root2.withdraw()
        root.deiconify()
            
    def searcht():
        def next():
                #global pno
            flag = True
            pno=patient_num.get()
            if(len(pno) == 0):
                messagebox.showinfo("","Enter valid phone number")
                flag = False
            while (flag == True):
                print("patient num: ",pno)
                if(len(pno) == 10):
                    query = "select *from patient_data where PHONE_No = %s"
                    phoneNo = [pno]
                    mycursor.execute(query,phoneNo)
                    data = mycursor.fetchall()
                    flag = True
                    
                    
                    if(data != []):
                        
                        print(data)
                        flag = False
                        if(data!=None):
                            Label(root2,text = "Record Found",font = ("Calibri 16"),bg = "lightblue").grid(row = 4, column = 1)
                            
                            Label(root2,text = "Patient Record",font = ("Calibri 16 underline"),bg = "lightblue").grid(row = 6, column = 0)
                            Label(root2,text = "Patient Code:",font = ("Calibri 16"),bg = "lightblue").grid(row = 7, column = 0)
                            Label(root2, text = data[0][0],font = ("Calibri 16"),bg = "lightblue",fg = "black").grid(row = 7, column = 1)

                            Label(root2, text = "Patient Type:",font = ("Calibri 16"),bg = "lightblue").grid(row = 8, column = 0)
                            Label(root2, text = data[0][1],font = ("Calibri 16"),bg = "lightblue").grid(row = 8, column = 1)

                            Label(root2, text = "Name:",font = ("Calibri 16"),bg = "lightblue").grid(row = 9, column = 0)
                            Label(root2, text = data[0][2],font = ("Calibri 16"),bg = "lightblue").grid(row = 9, column = 1)

                            Label(root2, text = "Age:",font = ("Calibri 16"),bg = "lightblue").grid(row = 10, column = 0)
                            Label(root2, text = data[0][3],font = ("Calibri 16"),bg = "lightblue").grid(row = 10, column = 1)

                            Label(root2, text = "Gender:",font = ("Calibri 16"),bg = "lightblue").grid(row = 11, column = 0)
                            Label(root2, text = data[0][4],font = ("Calibri 16"),bg = "lightblue").grid(row = 11, column = 1)

                            Label(root2, text = "Weight in Kg:",font = ("Calibri 16"),bg = "lightblue").grid(row = 12, column = 0)
                            Label(root2, text = data[0][5],font = ("Calibri 16"),bg = "lightblue").grid(row = 12, column = 1)

                            Label(root2, text = "Height in m:",font = ("Calibri 16"),bg = "lightblue").grid(row = 13, column = 0)
                            Label(root2, text = data[0][6],font = ("Calibri 16"),bg = "lightblue").grid(row = 13, column = 1)

                            Label(root2, text = "Allergy History:",font = ("Calibri 16"),bg = "lightblue").grid(row = 14, column = 0)
                            Label(root2, text = data[0][7],font = ("Calibri 16"),bg = "lightblue").grid(row = 14, column = 1)

                            Label(root2, text = "Phone No.:",font = ("Calibri 16"),bg = "lightblue").grid(row = 15, column = 0)
                            Label(root2, text = data[0][8],font = ("Calibri 16"),bg = "lightblue").grid(row = 15, column = 1)

                            Label(root2, text = "Email ID:",font = ("Calibri 16"),bg = "lightblue").grid(row = 16, column = 0)
                            Label(root2, text = data[0][9],font = ("Calibri 16"),bg = "lightblue").grid(row = 16, column = 1)

                            Label(root2, text = "Hospital Name:",font = ("Calibri 16"),bg = "lightblue").grid(row = 17, column = 0)
                            Label(root2, text = data[0][10],font = ("Calibri 16"),bg = "lightblue").grid(row = 17, column = 1)
                        else:
                            Label(root2, text = "Record not found",font = ("Calibri 16"),bg = "lightblue",fg = "black").grid(row = 6, column = 0)
                        break
                    elif(flag == True):
                        messagebox.showinfo("","Patient not registered")
                        break
                else:
                    messagebox.showinfo("","Enter valid phone number")
                    break
                        
        global root2
        root.withdraw()
        root2 = Toplevel(root)
        root2.geometry('600x600')
        root2.configure(bg = "lightblue")
        #Add phone number instead of code
        Label(root2, text = "Enter phone number",font = ("Calibri 16"),bg = "lightblue").grid(row = 0, column = 0)
        patient_num=Entry(root2,font = ("Calibri 16"))
        patient_num.grid(row=0,column=1)
        Label(root2,text = "",font = ("Calibri 16"),bg = "lightblue").grid(row = 1, column = 1)
        btn1 = Button(root2,text = "     Next     ",font = ("Calibri 16"),fg = "black",command = lambda:next()).grid(row = 2, column = 1)
        btn2 = Button(root2,text = "Back to Main Menu",font = ("Calibri 10"),command = lambda:backsearch()).place(x = 483, y = 0)
        '''def next():
            global pno
            pno=patient_num.get()
            print("patient num: ",pno)

            if enter()== True:
                Label(root2, text = "Record Found",font = ("Calibri 16"),bg = "lightblue",fg = "black").grid(row = 6, column = 1)
            else :
                Label(root2, text = "Record not found",font = ("Calibri 16"),bg = "lightblue",fg = "black").grid(row = 6, column = 1)'''
               
        '''while True:
            #pno
            if len(pno)==10:
                pno=int(pno)
                break

            else:
                Label(root2, text = "ENTER A VALID PHONE NUMBER",font = ("Calibri 16"),bg = "lightblue",fg = "black").grid(row = 7, column = 1)'''

    def backsql():
        root5.withdraw()
        root.deiconify()
           
    def removesql():
        '''def next():
            global code,pcode
            #print(REMOVAL(code))
            
            print("patient code : ",code)
            t = REMOVAL(code)
            data = t[0]
            if t[-1]==True:
                Label(root2, textvariable = data,font = ("Calibri 16"),bg = "lightblue",fg = "black").grid(row = 6, column = 1)
                Label(root2, text = "deleted",font = ("Calibri 16"),bg = "lightblue",fg = "black").grid(row = 7, column = 1)
            else:
                Label(root2, text = "Record not found",font = ("Calibri 16"),bg = "lightblue",fg = "black").grid(row = 7, column = 1)'''
        global root5
        root.withdraw()
        root5 = Toplevel(root)
        root5.geometry('600x600')
        root5.configure(bg = "lightblue")
        Label(root5, text = "Enter patient code",font = ("Calibri 16"),bg = "lightblue",fg = "black").grid(row = 1, column = 0)
        pcode=Entry(root5,font = ("Calibri 16"))
        pcode.grid(row = 1, column = 1)
        code=pcode.get()
        def next():
            global name
            code=pcode.get()
            flag = True
            if(code == None or code == ""):
                flag = False
                messagebox.showinfo("","Enter valid patient code")
            #checking if the code is present in the table
            if(flag == True):
                print("patient code : ",code)
                t = REMOVAL(code)
                data = t[0]

                if(t[-1] == False):
                    Label(root5, text = "Record not found",font = ("Calibri 16"),bg = "lightblue",fg = "black").grid(row = 7, column = 1)
                elif(t[-1]==True):
                    Label(root5,text = "Patient Record",font = ("Calibri 16 underline"),bg = "lightblue").grid(row = 6, column = 0)
                    Label(root5,text = "Patient Code:",font = ("Calibri 16"),bg = "lightblue").grid(row = 7, column = 0)
                    Label(root5, text = data[0][0],font = ("Calibri 16"),bg = "lightblue",fg = "black").grid(row = 7, column = 1)

                    Label(root5, text = "Patient Type:",font = ("Calibri 16"),bg = "lightblue").grid(row = 8, column = 0)
                    Label(root5, text = data[0][1],font = ("Calibri 16"),bg = "lightblue").grid(row = 8, column = 1)

                    Label(root5, text = "Name:",font = ("Calibri 16"),bg = "lightblue").grid(row = 9, column = 0)
                    Label(root5, text = data[0][2],font = ("Calibri 16"),bg = "lightblue").grid(row = 9, column = 1)

                    Label(root5, text = "Age:",font = ("Calibri 16"),bg = "lightblue").grid(row = 10, column = 0)
                    Label(root5, text = data[0][3],font = ("Calibri 16"),bg = "lightblue").grid(row = 10, column = 1)

                    Label(root5, text = "Gender:",font = ("Calibri 16"),bg = "lightblue").grid(row = 11, column = 0)
                    Label(root5, text = data[0][4],font = ("Calibri 16"),bg = "lightblue").grid(row = 11, column = 1)

                    Label(root5, text = "Weight in Kg:",font = ("Calibri 16"),bg = "lightblue").grid(row = 12, column = 0)
                    Label(root5, text = data[0][5],font = ("Calibri 16"),bg = "lightblue").grid(row = 12, column = 1)

                    Label(root5, text = "Height in m:",font = ("Calibri 16"),bg = "lightblue").grid(row = 13, column = 0)
                    Label(root5, text = data[0][6],font = ("Calibri 16"),bg = "lightblue").grid(row = 13, column = 1)

                    Label(root5, text = "Allergy History:",font = ("Calibri 16"),bg = "lightblue").grid(row = 14, column = 0)
                    Label(root5, text = data[0][7],font = ("Calibri 16"),bg = "lightblue").grid(row = 14, column = 1)

                    Label(root5, text = "Phone No.:",font = ("Calibri 16"),bg = "lightblue").grid(row = 15, column = 0)
                    Label(root5, text = data[0][8],font = ("Calibri 16"),bg = "lightblue").grid(row = 15, column = 1)

                    Label(root5, text = "Email ID:",font = ("Calibri 16"),bg = "lightblue").grid(row = 16, column = 0)
                    Label(root5, text = data[0][9],font = ("Calibri 16"),bg = "lightblue").grid(row = 16, column = 1)

                    Label(root5, text = "Hospital Name:",font = ("Calibri 16"),bg = "lightblue").grid(row = 17, column = 0)
                    Label(root5, text = data[0][10],font = ("Calibri 16"),bg = "lightblue").grid(row = 17, column = 1)

                    Label(root5,text = "",font = ("Calibri 16"),bg = "lightblue").grid(row = 18, column = 0)
                    
                    Label(root5, text = "Record Deleted Successfully",font = ("Calibri 16"),bg = "lightblue",fg = "black").grid(row = 19, column = 1)
                    
                    query = "delete from patient_data where code = %s"
                    c = [code]
                    mycursor.execute(query,c)
                    mydb.commit()
            '''else:
                Label(root5, text = "Record not found",font = ("Calibri 16"),bg = "lightblue",fg = "black").grid(row = 7, column = 1)'''
        pcode.grid(row=1,column=1)
        Label(root5,text = "",font = ("Calibri 16"),bg = "lightblue").grid(row = 4, column = 0)
        btn1 = Button(root5,text = "    Next    ",font = ("Calibri 16"),fg = "black",command = lambda:next()).grid(row = 5, column = 1)
        btn2 = Button(root5,text = "Back to Main Menu",font = ("Calibri 10"),command = lambda:backsql()).place(x = 483, y = 0)
        '''def next():
            global name
            code=pcode.get()
            print("patient code : ",code)
            if REMOVAL(code)==True:
                Label(root2, text = data,font = ("Calibri 16"),bg = "lightblue",fg = "black").grid(row = 6, column = 1)
                Label(root2, text = "deleted",font = ("Calibri 16"),bg = "lightblue",fg = "black").grid(row = 7, column = 1)
            else:
                Label(root2, text = "Record not found",font = ("Calibri 16"),bg = "lightblue",fg = "black").grid(row = 7, column = 1)'''
        
    def backCondition():
        root4.withdraw()
        root.deiconify()
    
    def condition():
        N = StringVar()
        T = StringVar()
        global root4
        root.withdraw()
        root4 = Toplevel(root)
        root4.geometry('600x600')
        root4.configure(bg = "lightblue")
        t = remove()
        flag = True
        if(t == False):
            flag = False
            root4.withdraw()
            messagebox.showinfo("","Queue is empty")
            backCondition()

        if(flag == True):
            N = t[0]
            T = t[1]

            Label(root4,text = "",font = ("Calibri 16"),bg = "lightblue").grid(row = 0, column = 0)
            Label(root4,text = "PATIENT DETAILS - STABLE CONDITION",font = ("Calibri 20"),bg = "lightblue").grid(row = 1, column = 1)
            Label(root4,text = "",font = ("Calibri 16"),bg = "lightblue").grid(row = 2, column = 0)
            Label(root4,text = "Patient Code:",font = ("Calibri 16"),bg = "lightblue").grid(row = 3, column = 0)
            Label(root4,text = N,font = ("Calibri 16"),bg = "lightblue").grid(row = 3, column = 1)

            Label(root4,text = "Emergency:",font = ("Calibri 16"),bg = "lightblue").grid(row = 4, column = 0)
            Label(root4,text = T,font = ("Calibri 16"),bg = "lightblue").grid(row = 4, column = 1)

            Button(root4, text = "Back to Main Menu",font = ("Calibri 10"),command = lambda:backCondition()).place(x = 483, y = 0)

    def backpatient():
        root7.withdraw()
        root.deiconify()

    def print_queue():
        global root7
        root.withdraw()
        root7 = Toplevel(root)
        root7.geometry('600x600')
        root7.configure(bg = "lightblue")
        Button(root7, text = "Back to Main Menu",font = ("Calibri 10"),command = lambda:backpatient()).place(x = 483, y = 0)
        '''
        for i in temp:
            Label(root7, text = i,font = ("Calibri 16"),bg = "lightblue",fg = "black").pack()
        '''
        try:
            T = t[0]
            nrec = len(T)
            Label(root7,text = "No.of patients left to operate:",font = ("Calibri 16"),bg = "lightblue").pack()
            Label(root7,text = nrec,font = ("Calibri 16"),bg = "lightblue").pack()
            Label(root7,text = "",font = ("Calibri 18"),bg = "lightblue").pack()

            #emergency, em_priority, code
            
            tree = ttk.Treeview(root7, column=("EMERGENCY", "PRIORITY", "PATIENT CODE"), show='headings', height=5)
            tree.column("# 1", anchor=CENTER)
            tree.heading("# 1", text="EMERGENCY")
            tree.column("# 2", anchor=CENTER)
            tree.heading("# 2", text="PRIORITY")
            tree.column("# 3", anchor=CENTER)
            tree.heading("# 3", text="PATIENT CODE")
            # Insert the data in Treeview widget
            for i in T:
                tree.insert('', 'end', text="1", values=i)
            tree.pack()
        except NameError:
            Label(root7,text = "",font = ("Calibri 16"),bg = "lightblue").pack()
            Label(root7,text = "",font = ("Calibri 16"),bg = "lightblue").pack()
            Label(root7,text = "",font = ("Calibri 16"),bg = "lightblue").pack()
            Label(root7,text = "",font = ("Calibri 16"),bg = "lightblue").pack()
            Label(root7,text = "",font = ("Calibri 16"),bg = "lightblue").pack()
            Label(root7,text = "",font = ("Calibri 16"),bg = "lightblue").pack()
            Label(root7,text = "",font = ("Calibri 16"),bg = "lightblue").pack()
            Label(root7,text = "Currently 0 patients to operate",font = ("Calibri 16"),bg = "lightblue").pack()
            Label(root7,text = "***",font = ("Calibri 16"),bg = "lightblue").pack()

        #Button(root7, text = "Back to Main Menu",font = ("Calibri 10"),command = lambda:backpatient()).place(x = 483, y = 0)
        
    firstroot.withdraw()
    sp = Label(root,text = "",bg = "lightblue").pack()
    '''sp = Label(root,text = "",bg = "lightblue").pack()
    sp = Label(root,text = "",bg = "lightblue").pack()'''

    title = Label(root,text = "HOSPITO MAIN MENU",font = ("Calibri 24"),bg = "lightblue",fg = "black").pack()
    sp = Label(root,text = "",bg = "lightblue").pack()
    #sp = Label(root,text = "",bg = "lightblue").pack()

    btn1 = Button(root,text = "          Add Patient            ",font = ("Calibri 17"),fg = "black",command = lambda:addpatient()).pack()
    sp = Label(root,text = "",bg = "lightblue").pack()

    btn2 = Button(root,text = "       Condition Stable       ",font = ("Calibri 17"),fg = "black",command = lambda:condition()).pack()
    sp = Label(root,text = "",bg = "lightblue").pack()

    btn3 = Button(root,text = "           Waiting Time        ",font = ("Calibri 17"),fg = "black",command = lambda:waitingtime()).pack()
    sp = Label(root,text = "",bg = "lightblue").pack()

    btn4 = Button(root,text = "            Search Data          ",font = ("Calibri 17"),fg = "black",command = lambda:searcht()).pack()
    sp = Label(root,text = "",bg = "lightblue").pack()

    btn5 = Button(root,text = "       Remove Record         ",font = ("Calibri 17"),fg = "black",command = lambda:removesql()).pack()
    sp = Label(root,text = "",bg = "lightblue").pack()

    btn6 = Button(root,text = "   Patients left to operate  ",font = ("Calibri 17"),fg = "black",command = lambda:print_queue()).pack()
    sp = Label(root,text = "",bg = "lightblue").pack()

    btn7 = Button(root,text = "                  Exit                 ",font = ("Calibri 17"),fg = "black",command = lambda:root.destroy()).pack()


#hospito part
from queue import PriorityQueue


import mysql.connector
from queue import PriorityQueue
mydb=mysql.connector.connect(host='localhost',user='root',passwd='1234',database = 'hospitalmanagement')
mycursor=mydb.cursor()

em_queue = PriorityQueue()
#get the hospital from drop down



emergencies = ["Gunshot",
                                "Cerebral Damage",
                                "Electrocution",
                                "Fire Damage",
                                "Cardiac Arrest"]
priorities = [2, 3, 1, 5, 4]
times = [15, 14, 16, 18, 12]
temp = []


def enter():
    st="select name from patient_data where code='%s'"%(code)

    mycursor.execute(st)
    name=mycursor.fetchall()
   
    #emergency from drop down
    #use list above
   
    if emergency in emergencies:
        em_priority = priorities[emergencies.index(emergency)]
        temp_tu = (emergency, em_priority, code)
        temp.append(temp_tu)
        def prio(tuples):
            return tuples[1]
        temp.sort(key=prio)
        em_queue.put(em_priority, emergency)
        return temp,True
    else:
        print('Emergeny Not Found\n*hint*\n')
        for i in emergencies:
            print(i,end=', ')
        print('')
        print('These are the accepted emergencies as of now\n')
        return False

#add tkinter window which shows message and closes it    
def remove():
    global n, t_em
    if(len(temp)==0):
        return False
    else:
        #print(temp)
        n=temp[0][2]
        #print(n)
        top = em_queue.get()
        temp.pop(0)
        t_em = emergencies[priorities.index(top)]
        #print(t_em)
        return n,t_em
        condition()

def search(name):
   
    pos = -1
    time = 0
    found = False

    for i in temp:
        if found:
            break

        if i[2] == name:
            pos = temp.index(i)
            found = True

        else:
            pos = -1

    if pos == -1:
        print("Record does not exist!\n")

    for j in range(0, pos):
        var = temp[j]
        time = time + times[emergencies.index(var[0])]

    print("Please wait for " + str(time) + " minutes\n ")
    k=str(time)
    return k,pos

def REMOVAL(code):
    st='select *from patient_data where code=%s'
    c = [code]
    mycursor.execute(st,c)
    data=mycursor.fetchall()
    if data!=[]:
        print(data)
        st="delete from patient_data where code='%s'"%(code)
        mycursor.execute(st)
        return data , True
        '''ch=int(input("ENTER 0 TO DELETE: "))
        if ch==0:
            st='delete from patient_data where code={}'.format(code)
        else:
            print("ABORTED")'''
    else:
        print("RECORD NOT FOUND")
        return data,False
firstroot.mainloop()
