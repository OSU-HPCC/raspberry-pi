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

def acceptInfo():
    emailInfo = open('studentemail.txt', 'w')
    emailInfo.write("None\n")
    emailInfo.write(str(sl.get()))
    emailInfo.close()
    myFractal.quit()
    

#This window has a slider and presents student with options for number of steps they want each pi to take.

someText = open('justforfun.txt', 'r')							#Info. text
info = someText.read()
someText.close()
lb = Label(myFractal, text=info, justify=CENTER, font="Verdana 20")
lb.pack(pady=((height/8), 0))

sl = Scale(myFractal, from_=1, to=1500, orient=HORIZONTAL, length=(length - 10))	#Scroll bar.
sl.pack(padx=(50, 50), pady=((height/6), 50))

bt = Button(myFractal, text="Make Fractal", command=acceptInfo, font="Verdana 20")
bt.pack(side=BOTTOM)

myFractal.mainloop()						#Start the demo. :)

os.system("python ./fractaldemo5.py")
