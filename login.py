from tkinter import *
from tkinter import messagebox
import mysql.connector
import gadhahumai as gd

flag=False

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="tiger",
    database="xycams"
)
mycursor=mydb.cursor()

table_name="security"
mycursor.execute("SELECT * FROM "+str(table_name))

myresult = mycursor.fetchall()

root=Tk()
root.title('XYCams Login')
root.geometry('925x500+300+200')
root.configure(bg="white")
root.resizable(False,False)

def signin():
    loginflag=False
    username=user.get()
    password=key.get()

    for x in myresult:

        if username==x[1] and password==x[2]:
            loginflag=True

    if loginflag:
        flag=True
        screen=Toplevel(root)
        screen.title('XYCams')
        screen.geometry('925x500+300+200')
        screen.config(bg="white")

        Label(screen,text="Thanks for using XYCams security system",bg="#fff",font=('Calibri(Body)',30,'bold')).pack(expand=True)

        if flag:
            detector = gd.MugDetection(capture_index=0, model_name='bestv5p1.pt')
            detector.run()
            
    else:
        messagebox.showerror("Invalid","Incorrect username and/or password")
                    

img=PhotoImage(file='security_img.png')
Label(root,image=img,bg="white").place(x=50,y=50)

frame=Frame(root,width=350,height=350,bg="white")
frame.place(x=480,y=70)

heading=Label(frame,text="Sign In",fg="green",bg="white",font=('Microsoft YaHei UI Light',25,'bold'))
heading.place(x=100,y=5)

##----------
 
def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')
        
user=Entry(frame,width=30,fg='green',border=0,bg="white",font=('Microsoft YaHei UI Light',10))
user.place(x=30,y=80)
user.insert(0,'Username@security/@resident')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)


Frame(frame,width=295,height=2,bg='black').place(x=25,y=107)

##-----------

def on_enter(e):
    key.delete(0,'end')

def on_leave(e):
    name=key.get()
    if name=='':
        key.insert(0,'Password')

key=Entry(frame,width=25,fg='green',border=0,bg="white",font=('Microsoft YaHei UI Light',10))
key.place(x=30,y=150)
key.insert(0,'Security Key')
key.bind('<FocusIn>',on_enter)
key.bind('<FocusOut>',on_leave) 

Frame(frame,width=295,height=2,bg='black').place(x=25,y=177)

##-----------

Button(frame,width=40,pady=7,text='Sign in',bg='green',fg='white',border=0,command=signin).place(x=35,y=204)
label=Label(frame,text="New resident ?",fg='black',bg='white',font=('Microsoft YaHei UI Light',8))
label.place(x=75,y=270)

sign_up=Button(frame,width=20,text='Register as a Resident',border=0,bg='white',cursor='hand2',fg='green')
sign_up.place(x=160,y=270)


root.mainloop()
