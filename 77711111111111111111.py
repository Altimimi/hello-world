from tkinter import *
def Insert():
    	name = text.get()
    	Text1.insert(END, name)
    	text.delete(0,END)	
    
root = Tk()
root.geometry('500x500')
root.title("Hello world")

Text1 = Text(root)
Text1.pack(side=TOP)

text = Entry(root, bg = 'white')
text.pack()

def delete():
  Text1.delete(1.0, END)
Text1 = Text(Text1)
Text1.pack()

Button3 = Button(root, text='Exit', width=10, command=root.destroy)
Button2 = Button(root, text="Clear", width=10, command=delete)
Button1 = Button(root, text="ENTRY", width=10, command=Insert)


Button3.pack(side=BOTTOM)
Button2.pack(side=BOTTOM)
Button1.pack(side=BOTTOM)


root.mainloop()
  	
