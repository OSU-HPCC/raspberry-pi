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
point_size = 5				#Size of points being plotted.
canvas_width = 500			#Width and height for plotting fractals.
canvas_height = 500			
click_counter = 0			#Count the number of screen touches/mouse clicks.
last_point = [0, 0]			#Last point plotted on fractal.
triangle_points = [canvas_width*0.5, canvas_height*0.05, canvas_width*0.05, canvas_height*0.95, canvas_width*0.95, canvas_height*0.95]
auto_num_pts = "1000"			#Number of iteration when computer takes over doing random walk.

#*******************************
#Some function definitions
#*******************************
def information(text):					#Function for showing dialog boxes.
    global demo_step

    showinfo("Fractals", text)
    demo_step += 1


def runEngine(bashCommand):				#Function runs back end gives back results
    os.system(bashCommand)
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
    return plotme

def plotaPoint(plotme):					#Plots a single point
    paper.create_oval(plotme[0] - point_size, plotme[1] + point_size, plotme[0] + point_size, plotme[1] - point_size, outline="black", fill="orange", width=2)
    last_point[0] = plotme[0]
    last_point[1] = plotme[1]				#Update record of last point plotted.

def plotPoint(event):			#Function for plotting point when mouse is clicked.
    global triangle_points
    global click_counter
    global demo_step
    global auto_num_pts

    if demo_step == 0:			#Pick fractal 'seed'
        paper.create_oval(event.x - point_size, event.y + point_size, event.x + point_size, event.y - point_size, outline="black", fill="orange", width=2)
        last_point[0] = event.x
        last_point[1] = event.y
        demo_step += 1			#Move to next step of demo.
        computerRun = "./fractalengine -fx " + str(triangle_points[0]) + " -fy " + str(triangle_points[1]) + " -sx " + str(triangle_points[2]) + " -sy " + str(triangle_points[3]) + " -tx " + str(triangle_points[4]) + " -ty " + str(triangle_points[5]) + " -ox " + str(last_point[0]) + " -oy " + str(last_point[1]) + " -i " + auto_num_pts + " -p " + "0"
        enginePoints = runEngine(computerRun)
        for k in range(len(enginePoints)):			#Let the computer plot a bunch of points so the fractal pattern emmerges.
            plotaPoint(enginePoints[k])
        secondInfo = open('supercomputers.txt', 'r')		#Get message about how supercomputers work.
        secondInfotext = secondInfo.read()
        secondInfo.close()
        information(secondInfotext)
    elif demo_step > 0:
        firstSteps.quit()


#*********************************************
#Stuff in window for steps 0 and 1 of tutorial
#*********************************************
paper = Canvas(firstSteps, width = canvas_width, height = canvas_height)				#Setup the canvas
paper.bind('<Button-1>', plotPoint)								#and set it to recieve
paper.pack()											#input from clicks.


#********************************
#Draw the points of the triangle.
#********************************
paper.create_oval(triangle_points[0] - point_size*2, triangle_points[1] + point_size*2, triangle_points[0] + point_size*2, triangle_points[1] - point_size*2, outline="black", fill="black", width=2)
paper.create_oval(triangle_points[2] - point_size*2, triangle_points[3] + point_size*2, triangle_points[2] + point_size*2, triangle_points[3] - point_size*2, outline="black", fill="black", width=2)
paper.create_oval(triangle_points[4] - point_size*2, triangle_points[5] + point_size*2, triangle_points[4] + point_size*2, triangle_points[5] - point_size*2, outline="black", fill="black", width=2)

introduction = open('lesspoints.txt', 'r')			#Get starting info message from file and use it in dialog box.
introText = introduction.read()
introduction.close()
information(introText)
firstSteps.mainloop()						#Start the demo. :)

os.system("./fractaldemo3.py")
