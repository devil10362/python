from tkinter import *
import os

def restart():
    os.system("shutdown /r /t 1");

def restarttime():
    os.system("shutdown /r /t 20");

def logout():
    os.system("shutdown  -1");

def shutdown():
    ("do you want to shutdown the system");
    yes=str(input("enter your choice"));
    if(yes=="yes"):
     os.system("shutdown /s /t 20");
    else:
       exit

def access():
   text=os.access("hello.txt",os.F_OK);
   print("exites of file",text);


r=Tk();
r.title("shutdown");
r.geometry("750x750");
r.config(bg="cyan");

b=Button(r,text="RESTART",height=3,width=10,fg='blue',bg='black',command=restart);
b.config(font=(60));
b.grid();
b.place(x=700,y=50);

lgout=Button(r,text="LOGOUT",height=3,width=10,fg='blue',bg='black',command=logout);
lgout.config(font=(60));
lgout.grid();
lgout.place(x=700,y=150);

shutdown=Button(r,text="SHUTDOWN",height=3,width=10,fg='blue',bg='black',command=shutdown);
shutdown.config(font=(60));
shutdown.grid();
shutdown.place(x=700,y=250);

retime=Button(r,text="RESTART TIME",height=3,width=17,fg='blue',bg='black',command=restarttime);
retime.config(font=(60));
retime.grid();
retime.place(x=675,y=350);

access=Button(r,text="ACCESS",height=3,width=17,fg='blue',bg='black',command=restarttime);
access.config(font=(60));
access.grid();
access.place(x=700,y=450);

r.mainloop();
