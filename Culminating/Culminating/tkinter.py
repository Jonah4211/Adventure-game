#ICS3U Culminating
#Jonah F
#06/09/2022
#RPG Character creator


from tkinter import *
from tkinter import ttk
import random 

#Functions


#mainCode

ranStat1=random.randint(3,18)
ranStat2=random.randint(3,18)
ranStat3=random.randint(3,18)
ranStat4=random.randint(3,18)
ranStat5=random.randint(3,18)
ranStat6=random.randint(3,18)


root=Tk()


root.title("RPG Character Creator")
root.geometry("700x550+300+100")

art=Label(root, image='placeholder.png')
art.grid(row=0, column=0, padx=10, pady=10)

root.mainloop()
