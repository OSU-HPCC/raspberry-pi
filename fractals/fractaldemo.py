#!/bin/python

#import pdb				#Debugger for development
import os
from subprocess import *
from Tkinter import *
top = Tk()
top.title("Fractal Pie")

point_size = 5				#Size of points being plotted.
canvas_width = 500			#Width and height for plotting fractals.
canvas_height = 500			
click_counter = 0			#Count the number of screen touches/mouse clicks.
last_point = [0, 0]			#Last point plotted on fractal.
triangle_points = [canvas_width*0.5, canvas_height*0.05, canvas_width*0.05, canvas_height*0.95, canvas_width*0.95, canvas_height*0.95]

def runEngine(bashCommand):				#Function runs back end and plots results. 
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
        paper.create_oval(plotme[i][0] - point_size, plotme[i][1] + point_size, plotme[i][0] + point_size, plotme[i][1] - point_size, outline="black", fill="orange", width=2)
        last_point[0] = plotme[i][0]
        last_point[1] = plotme[i][1]

def whichPoint(event, triangle_points):			#Function that plots a point when the student picks one of the triangle points.
    global click_counter

    point1 = False
    point2 = False
    point3 = False

    if (event.x < triangle_points[0] + point_size*2)  and (event.x > triangle_points[0] - point_size*2): #Test if point1 was clicked on
        if (event.y < triangle_points[1] + point_size*2) and (event.y > triangle_points[1] - point_size*2):
            point1 = True
    if (event.x < triangle_points[2] + point_size*2)  and (event.x > triangle_points[2] - point_size*2): #Test if point2 was clicked on
        if (event.y < triangle_points[3] + point_size*2) and (event.y > triangle_points[3] - point_size*2):
            point2 = True
    if (event.x < triangle_points[4] + point_size*2)  and (event.x > triangle_points[4] - point_size*2): #Test if point3 was clicked on
        if (event.y < triangle_points[5] + point_size*2) and (event.y > triangle_points[5] - point_size*2):
            point3 = True

    if point1 == True:					#Calculate the next step base on the previous point plotted.
        bashCommand = "./fractalengine -fx " + str(triangle_points[0]) + " -fy " + str(triangle_points[1]) + " -sx " + str(triangle_points[2]) + " -sy " + str(triangle_points[3]) + " -tx " + str(triangle_points[4]) + " -ty " + str(triangle_points[5]) + " -ox " + str(last_point[0]) + " -oy " + str(last_point[1]) + " -i " + "1" + " -p " + "1"
        runEngine(bashCommand)
        click_counter += 1
    elif point2 == True:
        bashCommand = "./fractalengine -fx " + str(triangle_points[0]) + " -fy " + str(triangle_points[1]) + " -sx " + str(triangle_points[2]) + " -sy " + str(triangle_points[3]) + " -tx " + str(triangle_points[4]) + " -ty " + str(triangle_points[5]) + " -ox " + str(last_point[0]) + " -oy " + str(last_point[1]) + " -i " + "1" + " -p " + "2"
        runEngine(bashCommand)
        click_counter += 1
    elif point3 == True:
        bashCommand = "./fractalengine -fx " + str(triangle_points[0]) + " -fy " + str(triangle_points[1]) + " -sx " + str(triangle_points[2]) + " -sy " + str(triangle_points[3]) + " -tx " + str(triangle_points[4]) + " -ty " + str(triangle_points[5]) + " -ox " + str(last_point[0]) + " -oy " + str(last_point[1]) + " -i " + "1" + " -p " + "3"
        runEngine(bashCommand)
        click_counter += 1
    else:						#If student clicked too far away from a point, nothing happens.
        return

demo_step = 0
#********************************
# demo_step is special counter that
# allows the mouse-click event
# function handler to behave
# differently depending on the place
# where the student is in the demo.
# Counter numbers are associated with
# the following steps:
#
# 0: Student is asked to pick the
#    initial staring point or 'seed'
#    for the fractals.
# 1: Student picks their own random
#    path by touching points of the 
#    triangle.

def plotPoint(event):			#Function for plotting point when mouse is clicked.
    global triangle_points
    global click_counter
    global demo_step

    if demo_step == 0:			#Pick fractal 'seed'
        paper.create_oval(event.x - point_size, event.y + point_size, event.x + point_size, event.y - point_size, outline="black", fill="orange", width=2)
        last_point[0] = event.x
        last_point[1] = event.y
        demo_step += 1			#Move to next step of demo.

    elif demo_step == 1:		#Student picks their own random path.
        if click_counter < 10:
            whichPoint(event, triangle_points)
            if click_counter == 10:	#Move to next step of demo.
                demo_step +=1

    elif demo_step == 2:
        paper.create_oval(10, 10, 50, 50) 
        

paper = Canvas(top, width = canvas_width, height = canvas_height)				#Setup the canvas
paper.bind('<Button-1>', plotPoint)								#and set it to recieve
paper.pack()											#input from clicks.

#********************************
#Draw the points of the triangle.
#********************************
paper.create_oval(triangle_points[0] - point_size*2, triangle_points[1] + point_size*2, triangle_points[0] + point_size*2, triangle_points[1] - point_size*2, outline="black", fill="black", width=2)
paper.create_oval(triangle_points[2] - point_size*2, triangle_points[3] + point_size*2, triangle_points[2] + point_size*2, triangle_points[3] - point_size*2, outline="black", fill="black", width=2)
paper.create_oval(triangle_points[4] - point_size*2, triangle_points[5] + point_size*2, triangle_points[4] + point_size*2, triangle_points[5] - point_size*2, outline="black", fill="black", width=2)

top.mainloop()
