from tkinter import *

def ClickMe():
    print(entry.get())

root=Tk()
root.geometry("300x200")

entry=Entry(root)
entry.pack()

button1=Button(root,text="Print",command=ClickMe)
button1.pack()

root.mainloop()