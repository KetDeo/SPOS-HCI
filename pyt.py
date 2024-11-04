import tkinter;
from tkinter import *;
from tkinter import messagebox;


def clicked():
    name=e1.get()
    opt=""
    if v.get()==1:
        opt="F.E."
    elif v.get()==2:
        opt="S.E."
    elif v.get()==3:
        opt="T.E."
    elif v.get()==4:
        opt="B.E."
    else:
        opt="none"    
    
    opt2=""
    if w.get()==1:
        opt2+="Sports "
    if x.get()==1:
        opt2+="Books "
    if y.get()==1:
        opt2+="Movies "    
    text='Hello '+ name + '. Registered for class: ' + opt + ' Department: ' + val.get() + '. Your hobbies are: ' + opt2
    messagebox.showinfo("Registered",text)
    
def exit():
    messagebox.showerror("Alert!","The session is about to end")
    root.quit()
    
def helped():
    messagebox.showinfo("Help","This is a practice gui")
    
root =Tk()
root.title("Practice")
root.geometry("620x350")
menubar=Menu(root)
menubar.add_command(label="File")
menubar.add_command(label="Help",command=helped)
menubar.add_command(label="Exit",command=exit)
root.configure(menu=menubar)

frameTitle=Frame(root)
frameTitle.configure(bg='lightblue')
frameTitle.pack(fill='x')
Label(frameTitle,text="Trial code",bg="lightblue",font=("bold",20)).pack()

frame1=Frame(root)
frame1.pack(fill='x')
Label(frame1,text="").grid(row=0,column=0,sticky='w')

Label(frame1,text="Enter your name",font=(18)).grid(row=1,column=0,sticky='w',padx=(20,0))
e1=Entry(frame1)
e1.grid(row=2,column=0,sticky='w',padx=(20,0))
Label(frame1,text="",font=(18)).grid(row=4,column=0,sticky='w',padx=(20,0))

Label(frame1,text="Enter your year",font=(18)).grid(row=5,column=0,sticky='w',padx=(20,0))
v=IntVar()
r1=Radiobutton(frame1,variable=v,text="F.E.",value=1,font=(10)).grid(row=5,column=1,padx=(20,0))
r2=Radiobutton(frame1,variable=v,text="S.E.",value=2,font=(10)).grid(row=5,column=2,padx=(20,0))
r3=Radiobutton(frame1,variable=v,text="T.E.",value=3,font=(10)).grid(row=5,column=3,padx=(20,0))
r4=Radiobutton(frame1,variable=v,text="B.E.",value=4,font=(10)).grid(row=5,column=4,padx=(20,0))
Label(frame1,text="",font=(18)).grid(row=6,column=0,sticky='w',padx=(20,0))

val=StringVar()
Label(frame1,text="Select Department",font=(18)).grid(row=7,column=0,sticky='w',padx=(20,0))
options=["Comp","IT","Mech"]
val.set("None")
o=OptionMenu(frame1,val,*options).grid(row=7,column=1,sticky='w',padx=(20,0))
Label(frame1,text="",font=(18)).grid(row=8,column=0,sticky='w',padx=(20,0))

Label(frame1,text="Select hobbies",font=(18)).grid(row=9,column=0,sticky='w',padx=(20,0))
w=IntVar()
x=IntVar()
y=IntVar()
c1=Checkbutton(frame1,text="Sports",variable=w,onvalue=1).grid(row=9,column=1,sticky='w',padx=(20,0))
c2=Checkbutton(frame1,text="Books",variable=x,onvalue=1).grid(row=9,column=2,sticky='w',padx=(20,0))
c3=Checkbutton(frame1,text="Movies",variable=y,onvalue=1).grid(row=9,column=3,sticky='w',padx=(20,0))
Label(frame1,text="",font=(18)).grid(row=10,column=0,sticky='w',padx=(20,0))

frame2=Frame(root)
frame2.pack(fill='x')
Button(frame2,text="Submit",bg="lightblue",font=(12),command=clicked).grid(row=0,column=0,sticky='w',padx=(190,0))
Button(frame2,text="Cancel",bg="lightblue",font=(12),command=exit).grid(row=0,column=1,sticky='w',padx=(80,0))

root.mainloop()