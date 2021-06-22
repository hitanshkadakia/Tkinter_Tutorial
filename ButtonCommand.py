from tkinter import *
root=Tk()
root.title("@happy_coding01")
root.geometry("300x100")
def follow():
    print("You have successfully Followed @happy_coding01")
button=Button(root,text="Follow",command=follow,bg="black"
                                              ,fg="yellow")
button.pack()
root.mainloop()