from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry("300x200")
def infocallme():
    messagebox.showinfo("Success","Installation Complete")
def alertcallme():
    messagebox.showerror("Error","Error Messagebox")
def warning():
    messagebox.showwarning("Warning","Warning message box")
button1=Button(root,text="show info message",command=infocallme)
button1.pack()
button2=Button(root,text="Alert Message",command=alertcallme)
button2.pack()
button3=Button(root,text="Warning Message",command=warning)
button3.pack()

root.mainloop()
