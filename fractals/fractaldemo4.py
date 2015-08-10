#!/usr/bin/python

#******************************
#Get stuff going.
#******************************

import os
from subprocess import *
from Tkinter import *
from tkMessageBox import *
import time

myFractal = Tk()
myFractal.title("My Turn")	
myFractal.attributes("-fullscreen", True)

length = myFractal.winfo_screenwidth()					#Dimensions of screen.
height = myFractal.winfo_screenheight()
canDelete = True
checkYesNo = IntVar()

#Some function definitions.

def checkCheck(event):
    global canDelete

    if (checkYesNo.get() != 0) and canDelete == True:
        tx.config(state=NORMAL)
        email.set("")
        canDelete = False
    elif checkYesNo.get() == 0:
        tx.config(state=DISABLED)
        email.set("youremail@example.com")
        canDelete = True

#This window has a slider and presents student with options for number of steps they want each pi to take.
#Also gives them an option to input their email so they can email themselves a picture of their fractal.

someText = open('justforfun.txt', 'r')							#Info. text
info = someText.read()
someText.close()
lb = Label(myFractal, text=info, justify=CENTER, font="Verdana 20")
lb.pack(pady=((height/8), 0))

#Check box.
cb = Checkbutton(myFractal, text="Email me a picture of my factal when you are done.", font="Verdana 15", variable=checkYesNo)
cb.pack(pady=((height/8),0))
cb.bind('<Button-1>', checkCheck)

sl = Scale(myFractal, from_=1, to=10000, orient=HORIZONTAL, length=(length - 10))	#Scroll bar.
sl.pack(padx=(50, 50), pady=((height/6), 50))

email = StringVar()									#Textbox for inputing email.
tx = Entry(myFractal, width=75, font="Verdana 15", textvariable=email, state=DISABLED)
tx.pack(pady=((height/8)))
email.set("youremail@example.com")

myFractal.mainloop()						#Start the demo. :)

#os.system("python ./fractaldemo5.py")
