#!/usr/bin/python

#******************************
#Get stuff going.
#******************************

#import pdb				#Debugger for development
import os
from subprocess import *
from Tkinter import *
from tkMessageBox import *
import time

firstSteps = Tk()
firstSteps.title("Fractal Pie")	
firstSteps.attributes("-fullscreen", True)

#*******************************
#Some universal variables needed
#by everybody.
#*******************************
demo_step = -1 
point_size = 2				#Size of points being plotted.
canvas_width = firstSteps.winfo_screenwidth()			#Width and height for plotting fractals.
canvas_height = firstSteps.winfo_screenheight()
click_counter = 0			#Count the number of screen touches/mouse clicks.
last_point = [0, 0]			#Last point plotted on fractal.
triangle_points = [canvas_width*0.5, canvas_height*0.05, canvas_width*0.05, canvas_height*0.95, canvas_width*0.95, canvas_height*0.95]

#**********************
#Read in student's email info.
#**********************
studentEmail = open('studentemail.txt', 'r')
email = studentEmail.read()
studentEmail.close()
os.system("rm ./studentemail.txt")
email = email.split('\n')
auto_num_pts = email[1]				#Number of iteration when computer takes over doing random walk.
email = email[0]

#*******************************
#Some function definitions
#*******************************
def information(text):					#Function for showing dialog boxes.
    global demo_step

    showinfo("Fractals", text)
    demo_step += 1


def runParallelEngine(bashCommand):				#Function runs back end gives back results
    passOutCommand = open('/home/pi/raspberry-pi/fractals/parallelthis.txt', 'w')
    passOutCommand.write(bashCommand)
    passOutCommand.close()
    os.system("mpirun -np 8 --machinefile ~/slicesofpie python /home/pi/raspberry-pi/fractals/distribute.py")
    os.system("rm /home/pi/raspberry-pi/fractals/parallelthis.txt")
    pointFile = open('fractalpoints.txt', 'r')
    plotme = pointFile.read()				#Read text from file and clean up for next time.
    pointFile.close()
    os.system("rm ./fractalpoints.txt")
    plotme = plotme.split('\n')				#Format data into something nice to work with.
    plotme = plotme[:-1]
    for i in range(len(plotme)):
        plotme[i] = plotme[i].split(' ')
        plotme[i][0] = float(plotme[i][0])
        plotme[i][1] = float(plotme[i][1])
        plotme[i][2] = int(plotme[i][2])
    return plotme

def plplotaPoint(plotme):					#Plots a single point
    if plotme[2] == 0:
        paper.create_oval(plotme[0] - point_size, plotme[1] + point_size, plotme[0] + point_size, plotme[1] - point_size, outline="black", fill="orange", width=1)
    if plotme[2] == 1:
        paper.create_oval(plotme[0] - point_size, plotme[1] + point_size, plotme[0] + point_size, plotme[1] - point_size, outline="black", fill="black", width=1)
    if plotme[2] == 2:
        paper.create_oval(plotme[0] - point_size, plotme[1] + point_size, plotme[0] + point_size, plotme[1] - point_size, outline="black", fill="blue", width=1)
    if plotme[2] == 3:
        paper.create_oval(plotme[0] - point_size, plotme[1] + point_size, plotme[0] + point_size, plotme[1] - point_size, outline="black", fill="yellow", width=1)
    if plotme[2] == 4:
        paper.create_oval(plotme[0] - point_size, plotme[1] + point_size, plotme[0] + point_size, plotme[1] - point_size, outline="black", fill="red", width=1)
    if plotme[2] == 5:
        paper.create_oval(plotme[0] - point_size, plotme[1] + point_size, plotme[0] + point_size, plotme[1] - point_size, outline="black", fill="green", width=1)
    if plotme[2] == 6:
        paper.create_oval(plotme[0] - point_size, plotme[1] + point_size, plotme[0] + point_size, plotme[1] - point_size, outline="black", fill="white", width=1)
    if plotme[2] == 7:
        paper.create_oval(plotme[0] - point_size, plotme[1] + point_size, plotme[0] + point_size, plotme[1] - point_size, outline="black", fill="purple", width=1)
    last_point[0] = plotme[0]
    last_point[1] = plotme[1]				#Update record of last point plotted.
    firstSteps.update_idletasks()

def plotPoint(event):			#Function for plotting point when mouse is clicked.
    global triangle_points
    global click_counter
    global demo_step
    global auto_num_pts

    if demo_step == 0:			#Pick fractal 'seed'
        paper.create_oval(event.x - point_size*4, event.y + point_size*4, event.x + point_size*4, event.y - point_size*4, outline="black", fill="orange", width=2)
        last_point[0] = event.x
        last_point[1] = event.y
        firstSteps.update_idletasks()
        demo_step += 1			#Move to next step of demo.
        computerRun = "./fractalengine -fx " + str(triangle_points[0]) + " -fy " + str(triangle_points[1]) + " -sx " + str(triangle_points[2]) + " -sy " + str(triangle_points[3]) + " -tx " + str(triangle_points[4]) + " -ty " + str(triangle_points[5]) + " -ox " + str(last_point[0]) + " -oy " + str(last_point[1]) + " -i " + auto_num_pts + " -p " + "0" + " -r "
        enginePoints = runParallelEngine(computerRun)
        for k in range(len(enginePoints)):			#Let the computer plot a bunch of points so the fractal pattern emmerges.
            plplotaPoint(enginePoints[k])
        os.system("scrot /home/pi/raspberry-pi/fractals/myfractal.jpeg")
        messagelb2 = paper.create_text(canvas_width - 50, 50, anchor="ne")
        paper.itemconfig(messagelb2, text="Touch anywhere to finish.", font='Verdana 20')
        paper.insert(messagelb2, 20, "")
    elif demo_step == 1:
        firstSteps.quit()
        if email != 'None':
            os.system("echo 'Thank you so much for checking out our demonstration on high performance computing! The fractal you made is attached to this email. If you want to know more about high performance computing, check out the info. on our website:\nhttps://hpcc.okstate.edu/content/hpc-education-resources\n\nWe hope you enjoy it!\n\nSincerely,\n\nOkstate HPCC Team' | mutt -s Fractal -a ./myfractal.jpeg -- " + email)
        os.system("rm ./myfractal.jpeg")
        os.system("echo '\n\n~~~~~~~~~~~~Thanks so much! We hope you enjoyed!~~~~~~~~~~~~\n\n'")

#*********************************************
#Stuff in window for steps 0 and 1 of tutorial
#*********************************************
paper = Canvas(firstSteps, width = canvas_width, height = canvas_height)				#Setup the canvas
paper.bind('<Button-1>', plotPoint)								#and set it to recieve
paper.pack()											#input from clicks.


#********************************
#Draw the points of the triangle.
#********************************
paper.create_oval(triangle_points[0] - point_size*16, triangle_points[1] + point_size*16, triangle_points[0] + point_size*16, triangle_points[1] - point_size*16, outline="black", fill="black", width=2)
paper.create_oval(triangle_points[2] - point_size*16, triangle_points[3] + point_size*16, triangle_points[2] + point_size*16, triangle_points[3] - point_size*16, outline="black", fill="black", width=2)
paper.create_oval(triangle_points[4] - point_size*16, triangle_points[5] + point_size*16, triangle_points[4] + point_size*16, triangle_points[5] - point_size*16, outline="black", fill="black", width=2)

introduction = open('lastremark.txt', 'r')			#Get starting info message from file and use it in dialog box.
introText = introduction.read()
introduction.close()
messagelb = paper.create_text(50, 50, anchor="nw")
paper.itemconfig(messagelb, text=introText, font='Verdana 20')
paper.insert(messagelb, 20, "")
demo_step += 1
firstSteps.mainloop()						#Start the demo. :)
os.system("printf 'All done.\n' ")
