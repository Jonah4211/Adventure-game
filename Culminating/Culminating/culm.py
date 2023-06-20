#ICS3U Culminating
#Jonah F
#06/09/2022
#RPG Character creator


from tkinter import *
from tkinter import ttk
import random 


#Functions


currentClass=str('Fighter')

def classRight():       #next class
    global currentClass
    global img
    if currentClass=='Fighter':
        Class.config(text='Wizard')
        currentClass='Wizard'
        img=PhotoImage(file='Wizard.png')
        photo.config(image=img)
    elif currentClass=='Wizard':
        Class.config(text='Ranger')
        currentClass='Ranger'
        img=PhotoImage(file='Ranger.png')
        photo.config(image=img)
    elif currentClass=='Ranger':
        Class.config(text='Rogue')
        currentClass='Rogue'
        img=PhotoImage(file='Rogue.png')
        photo.config(image=img)
    elif currentClass=='Rogue':
        Class.config(text='Bard')
        currentClass='Bard'
        img=PhotoImage(file='Bard.png')
        photo.config(image=img)
    elif currentClass=='Bard':
        Class.config(text='Cleric')
        currentClass='Cleric'
        img=PhotoImage(file='Cleric.png')
        photo.config(image=img)
    else:
        Class.config(text='Fighter')
        currentClass='Fighter'
        img=PhotoImage(file='Fighter.png')
        photo.config(image=img)
        
def classLeft():        #prev class
    global currentClass
    global img
    if currentClass=='Cleric':
        Class.config(text='Bard')
        currentClass='Bard'
        img=PhotoImage(file='Bard.png')
        photo.config(image=img)
    elif currentClass=='Bard':
        Class.config(text='Rogue')
        currentClass='Rogue'
        img=PhotoImage(file='Rogue.png')
        photo.config(image=img)
    elif currentClass=='Rogue':
        Class.config(text='Ranger')
        currentClass='Ranger'
        img=PhotoImage(file='Ranger.png')
        photo.config(image=img)
    elif currentClass=='Ranger':
        Class.config(text='Wizard')
        currentClass='Wizard'
        img=PhotoImage(file='Wizard.png')
        photo.config(image=img)
    elif currentClass=='Wizard':
        Class.config(text='Fighter')
        currentClass='Fighter'
        img=PhotoImage(file='Fighter.png')
        photo.config(image=img)
    else:
        Class.config(text='Cleric')
        currentClass='Cleric'
        img=PhotoImage(file='Cleric.png')
        photo.config(image=img)
        
def update():           #check for mistakes and update av points
    currentpoints=68-(currentStr.get()+currentDex.get()+currentCon.get()+currentInt.get()+currentWis.get()+currentCha.get())
    points.config(text=currentpoints)

    if currentpoints>=0 and currentpoints<=20:
        pass
        
    else:
        currentStr.set(8)
        curStr.config(text=currentStr)
        currentDex.set(8)
        curDex.config(text=currentDex)
        currentCon.set(8)
        curCon.config(text=currentCon)
        currentInt.set(8)
        curInt.config(text=currentInt)
        currentWis.set(8)
        curWis.config(text=currentWis)
        currentCha.set(8)
        curCha.config(text=currentCha)
        update()
    
        
def submit():           #update and print summary of char
    update()
    print('You created',name,'the',currentClass)
    print(name,'has a strength of', currentStr.get(), 'a dexterity of', currentDex.get(), 'a constitution of', currentCon.get(), 'a inteligence of', currentInt.get(), 'a wisdom of', currentWis.get(), 'and a charisma of', currentCha.get())


#Main Code




root=Tk()
root.title("RPG Character Creator")
root.geometry("570x700+300+100")

img=PhotoImage(file='Fighter.png')                  #image box
photo= Label(root, width=280, height=300, image=img)
photo.grid(row=1, columnspan=6, rowspan=3, column=1, padx=10, pady=10 )

name = 'Input Name'

nameEntry=ttk.Entry(root, textvariable = name, width=20, justify=CENTER)            #name box
nameEntry.grid(row=1, column=7, columnspan=3, padx=10, pady=0, sticky=S)
nameEntry.config(font='Helvetica 16')
nameEntry.insert(0,name)

theLabel=Label(root, text='the')                            #'the' label
theLabel.grid(row=2, column=8, padx=10, pady=0)
theLabel.config(font='Helvetica 15')

rightButton=ttk.Button(root, text='Next', command=classRight)       #next class button
rightButton.grid(row=3, column=9, sticky=NE)

leftButton=ttk.Button(root, text='Back', command=classLeft)         #prev class button
leftButton.grid(row=3, column=7, sticky=NW)


Class=Label(root, text='Fighter')                           #current class label
Class.grid(row=3, column=8, padx=10, pady=0, sticky=N)
Class.config(font='Helvetica 16')

arLabel=Label(root, text='Available points')                                    #av points label
arLabel.grid(row=4, column=1, columnspan=20, sticky=N, pady=10, ipady=20)
arLabel.config(font='Helvetica 16')

Title=Label(root, text='RPG Character Creator')     #top title
Title.grid(row=0, column=1, columnspan=20)
Title.config(font='Helvetica 20')



#STATS

strength=Label(root, text='Str')
strength.grid(row=5, column=1, sticky=NW, padx=10, pady=20)
strength.config(font='Helvetica 16')

currentStr=IntVar()
currentStr.set(8)
curStr=ttk.Spinbox(root, from_=8, to=18, textvariable=currentStr, width=4, command=update)              #current str spinbox, runs update
curStr.grid(row=5, column=1, columnspan=20, sticky=NW, padx=50, pady=20)
curStr.config(font='Helvetica 16')

Dexterity=Label(root, text='Dex')
Dexterity.grid(row=5, column=1, columnspan=20, sticky=NW,padx=200, pady=20)
Dexterity.config(font='Helvetica 16')

currentDex=IntVar()
currentDex.set(8)
curDex=ttk.Spinbox(root, from_=8, to=18, textvariable=currentDex, width=4, command=update)                  #current dex spinbox, runs update
curDex.grid(row=5, column=1, columnspan=20, sticky=N, pady=20)
curDex.config(font='Helvetica 16')

Charisma=Label(root, text='Cha')
Charisma.grid(row=6, column=1, columnspan=20, sticky=SE, padx=90)
Charisma.config(font='Helvetica 16')

currentCha=IntVar()
currentCha.set(8)
curCha=ttk.Spinbox(root, from_=8, to=18, textvariable=currentCha, width=4, command=update)                  #current cha spinbox, runs update
curCha.grid(row=6, column=1, columnspan=20, sticky=SE, padx=10)
curCha.config(font='Helvetica 16')

Wisdom=Label(root, text='Wis')
Wisdom.grid(row=6, column=1, columnspan=20, sticky=SW, padx=200)
Wisdom.config(font='Helvetica 16')

currentWis=IntVar()
currentWis.set(8)
curWis=ttk.Spinbox(root, from_=8, to=18, textvariable=currentWis, width=4, command=update)                  #current wis spinbox, runs update
curWis.grid(row=6, column=1, columnspan=20, sticky=S)
curWis.config(font='Helvetica 16')


Inteligence=Label(root, text='Int')
Inteligence.grid(row=6, column=1, columnspan=20, sticky=SW, padx=10)
Inteligence.config(font='Helvetica 16')

currentInt=IntVar()     
currentInt.set(8)
curInt=ttk.Spinbox(root, from_=8, to=18, textvariable=currentInt, width=4, command=update)                  #current int spinbox, runs update
curInt.grid(row=6, column=1, columnspan=20, sticky=SW, padx=50)
curInt.config(font='Helvetica 16')

Constitution=Label(root, text='Con')
Constitution.grid(row=5, column=1, columnspan=20, sticky=NE, padx=90, pady=20)
Constitution.config(font='Helvetica 16')

currentCon=IntVar()     
currentCon.set(8)
curCon=ttk.Spinbox(root, from_=8, to=18, textvariable=currentCon, width=4, command=update)                  #current con spinbox, runs update
curCon.grid(row=5, column=1, columnspan=20, sticky=NE, padx=10, pady=20)
curCon.config(font='Helvetica 16')


#Main code CONT

currentpoints=68-(currentStr.get()+currentDex.get()+currentCon.get()+currentInt.get()+currentWis.get()+currentCha.get()) 

points=Label(root, text=currentpoints)                              #Current points label
points.grid(row=4, column=1, columnspan=20, sticky=S)
points.config(font='Helvetica 16')

finish=ttk.Button(root, text='Submit', command=submit)                  #Submit button
finish.grid(row=7, column=1, columnspan=20, sticky=S, pady=40)



root.mainloop()
