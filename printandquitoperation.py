from tkinter import *
root=Tk()
root.title("@happy_coding01")
root.geometry("300x100")
def printt():
    print("DEMO TEXT")
button=Button(root,text="Print",command=printt,bg="black"
                        ,width=6,height=2,fg="yellow")
button.pack(side=LEFT)
button=Button(root,text="Quit",command=root.destroy,bg="black"
                        ,width=6,height=2,fg="yellow")
button.pack(side=RIGHT)

root.mainloop()