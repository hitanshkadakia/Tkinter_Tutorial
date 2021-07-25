from tkinter import *

root=Tk()
root.geometry("300x200")

frame=LabelFrame(root,text="Input",padx=5,pady=5)
frame.pack()

entry=Entry(frame)
entry.pack()

root.mainloop()