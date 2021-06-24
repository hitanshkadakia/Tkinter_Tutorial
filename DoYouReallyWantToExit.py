from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("300x200")
def yesno():
    answer=messagebox.askquestion("Exit","Do You Really Want To Exit")
    if answer=='yes':
        root.quit()
def yesnocancel():
    answer=messagebox.askyesnocancel("Exit","Do You Really Want To Exit")
    if(answer):
        root.quit()
button1=Button(root,text="Yes No Cancel",command=yesnocancel)
button1.pack()
button2=Button(root,text="Yes No",command=yesno)
button2.pack()
root.mainloop()
