from tkinter import *
root=Tk()
root.title("@happy_coding01")
root.geometry("300x300")
frame1=Frame(root,bg="blue")
frame1.pack(fill=BOTH,expand=True)
button=Button(frame1,text="Button")
button.pack()
root.mainloop()