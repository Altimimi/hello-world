from tkinter import *
master = Tk()

e = Entry(master)
e.pack()
def text():
    text.delete(INSERT)
    text.delete(button)

root = Tk()
text = Text(root)
e.focus_set()
text.pack()

def callback():
          text.insert(INSERT, e.get())

b = Button(master, text="ENTRY", width=10, command=callback)
a = Button(master, compound=TOP,  text="Quit", width=10, command=master.quit)

a.pack()
b.pack()

mainloop()


