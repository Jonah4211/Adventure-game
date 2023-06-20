
from tkinter import *
from tkinter import ttk

def NewOrder():
    pass   

def close():
    exit()
    #quityn=Messagebox

def DoNothing():
    pass


root=Tk()
root.title("Restaurant")
root.geometry('435x200+200+200')

menuBar=Menu(root)

fileMenu=Menu(menuBar,tearoff=0)
menuBar.add_cascade(label="File",menu=fileMenu)

fileMenu.add_command(label="New File", command=DoNothing)
fileMenu.add_command(label="Open...", command=DoNothing)
fileMenu.add_separator()
fileMenu.add_command(label="Close", command=close)

orderMenu=Menu(menuBar,tearoff=1)
menuBar.add_cascade(label="Order",menu=orderMenu)

orderMenu.add_command(label="New Order", command=NewOrder)

root.config(menu=menuBar)

root.mainloop()
