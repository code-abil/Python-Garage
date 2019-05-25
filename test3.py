from tkinter import *
from tkinter import messagebox

def insert():
    f=open("filegui.txt","a+")
    rollno=e1.get()
    name=e2.get()
    dept=e3.get()
    
    f.write(rollno +"\n")
    f.write(name +"\n")
    f.write(dept +"\n")
    f.close()

def fetch():
    v=ent.get()
    v=v+"\n"
    roll=""
    name=""
    dept=""
    f=open("filegui.txt","r+")
    l=f.readlines()
    for i in range(len(l)):
        if l[i]==v:
            global name_var,dept_var
            name_var.set(l[i+1])
            dept_var.set(l[i+2])
            #print(l[i+1])
            break
        else:
            i=i+2
    f.close()

def delete():
    ans=messagebox.askyesno("DELETE","are u sure want to delete")
    v=e.get()
    v=v+"\n"
    if ans:
        f=open("filegui.txt","r")
        l=f.readlines()
        print(l)
        for i in range(len(l)):
            if l[i]==v:
                l.pop(i)
                l.pop(i)
                l.pop(i)
                break
        f.close()
        f=open("filegui.txt","w")
        print(l)
        for i in range(len(l)):
            f.write(l[i])
        
        f.close()
        
root=Tk()

f1=Frame(root)
l1=Label(f1,text="ROLL NO")
l1.grid(row=1,column=0)

e1=Entry(f1)
e1.grid(row=1,column=1)

l2=Label(f1,text="NAME")
l2.grid(row=2,column=0)
e2=Entry(f1)
e2.grid(row=2,column=1)

l3=Label(f1,text="DEPARTMENT")
l3.grid(row=3,column=0)
e3=Entry(f1)
e3.grid(row=3,column=1)

b1=Button(f1,text="insert",command=insert)
b1.grid(row=5,column=2)
f1.pack()


f2=Frame(root)
lab=Label(f2,text="ENTER ROLL NO")
lab.grid(row=0,column=0)
ent=Entry(f2)
ent.grid(row=0,column=1)
b2=Button(f2,text="fetch",command=fetch)
b2.grid(row= 2,column=2)

name_var=StringVar()
dept_var=StringVar()
lb1=Label(f2,text='NAME')
lb1.grid(row=5,column=0)
en1=Entry(f2,textvariable=name_var)
en1.grid(row=5,column=1)

lb2=Label(f2,text="DEPARTMENT")
lb1.grid(row=7,column=0)
en2=Entry(f2,textvariable=dept_var)
en2.grid(row=7,column=1)


f2.pack()

f3=Frame(root)

la=Label(f3,text="enter the roll no to be  deleted ").grid(row=0,column=0)
e=Entry(f3)
e.grid(row=0,column=1)
b3=Button(f3,text="delete",command=delete)
b3.grid(row=2,column=2)

f3.pack()

root.mainloop()


Button(win,command=lambda:func(5))