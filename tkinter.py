# frame python
from tkinter import * 
from tkinter import messagebox



r=Tk();
r.title("gui programme");
r.geometry("750x750");

#lable
lbl=Label(r,text="GUI PYTHON",height=3,width=15,fg='blue',bg='cyan');
lbl.config(font=(40,40));
lbl.grid();
lbl.place(x=700,y=50);


##button
#b=Button(r,text="BUTTON",height=3,width=10,fg='blue',bg='black');
#b.config(font=(60));
#b.grid();
#b.place(x=50,y=600);



#checkbox
#c=Checkbutton(r,text="CHECK BOX",fg='blue',bg='black');
#c.config(font=(180));
#c.grid();
#c.place(x=50,y=500);


#text field
#t=Text(r,bg='black',fg='white');
#t.config(font=(20,10));
#t.grid();

e1lbl=Label(r,text="FIRST NAME");              
e1lbl.grid();
e1lbl.place(x=680,y=200);
e1=Entry(r);
e1.place(x=850,y=200);

e2lbl=Label(r,text="LAST NAME");
e2lbl.place(x=680,y=250);
e2=Entry(r);e2.place(x=850,y=250)

e3lbl=Label(r,text="EMAIL@");
e3lbl.grid();
e3lbl.place(x=680,y=300);
e3=Entry(r);
e3.place(x=850,y=300);
       
e4lbl=Label(r,text="FATHER NAME");
e4lbl.place(x=680,y=350);
e4=Entry(r);
e4.grid();
e4.place(x=850,y=350);



e5lbl=Label(r,text="MOTHER NAME");
e5lbl.grid();
e5lbl.place(x=680,y=400);
e5=(Entry(r));
e5.grid();
e5.place(x=850,y=400);

e6lbl=Label(r,text="PHONE NUMBER");
e6lbl.grid();
e6lbl.place(x=680,y=450);
e6=(Entry(r));
e6.grid();
e6.place(x=850,y=450);

def msg():
        messagebox.showinfo('form complete'," FORM COMPLETED");
                                                                 
b=Button(r,text="SUBMIT",height=3,width=10,fg='blue',bg='black',command=msg);
b.config(font=(60));
b.grid();
b.place(x=720,y=500);

#radiobutton
#r=Radiobutton(r,text="RADIOBUTTON",height=3,width=12);
#r.config(font=(60));
#r.grid();
#r.place(x=50,y=700);

#bu=Button(r,text="start form",height=2,width=11,fg='blue',bg='black');
#bu.config(font=(60));
#bu.grid();
#bu.place(x=720,y=550);

r.configure(bg='cyan');
r.mainloop();


