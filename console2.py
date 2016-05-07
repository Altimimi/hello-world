from Tkinter import *

master = Tk()

master.title("key control")        # title first frame
master.geometry("300x300")       # frame size 

#second frame to show text
root = Tk()
root.title("our text")
text = Text(root)
text.pack()

def Clear():
  e.delete(0,END)
e = Entry(master)
e.pack()


def callback():
          text.insert(INSERT, e.get())

Button1 = Button(master, text="ENTRY", width=10, command=callback)
Button2 = Button(master, text="Clear Text", width=10, command=Clear)
Button3= Button(master, text='Exit Program', command=master.destroy)
Button1.pack()

Button2.pack()
Button3.pack()
mainloop()


