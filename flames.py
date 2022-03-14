import tkinter
from tkinter import *
gui = Tk()
gui.configure(background="pink")
gui.title("Flames")
gui.geometry("400x400")

def fun():
    name1=entry1.get()
    name2=entry2.get()
    name1.lower()
    name2.lower()
    name1.replace(" ", "")
    name2.replace(" ", "")
    name1 = list(name1)
    name2 = list(name2)
    for i in name1[:]:
        if i in name2:
            name1.remove(i)
            name2.remove(i)
    count = len(name1) + len(name2)

    flames = ["Friend", "Love", "Affection", "Marriage", "Enemy", "Sister"]
    index = count % len(flames) - 1

    msg="Result : "+flames[index]
    label=Label(gui,text=msg,bg="red")
    label.place(x=150,y=250)

label1=Label(gui,text="Name1",bg="sky blue")
label1.place(x=90,y=100)
entry1=Entry(gui)
entry1.place(x=160,y=100)

label2=Label(gui,text="Name2",bg="sky blue")
label2.place(x=90,y=140)
entry2=Entry(gui)
entry2.place(x=160,y=140)

button=Button(gui,text="Check",bg="pink",command=fun).place(x=200,y=200)

gui.mainloop()
