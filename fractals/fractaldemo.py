#!/bin/python

from Tkinter import *
top = Tk()
top.title("Fractal Pie")

point_size = 5				#Size of points being plotted.
canvas_width = 1500			#Width and height for plotting fractals.
canvas_height = 700			
click_counter = 0			#Count the number of screen touches/mouse clicks.
last_point = [0, 0]			#Last point plotted on fractal.
triangle_points = [canvas_width*0.5, canvas_height*0.05, canvas_width*0.05, canvas_height*0.95, canvas_width*0.95, canvas_height*0.95]

def whichPoint(event, triangle_points):			#Function that plots a point when the student picks one of the triangle points.
    point1 = False
    point2 = False
    point3 = False

    if (event.x < triangle_points[0] + point_size*2) && (event.x > triangle_points[0] - point_size*2): #Test which point was clicked on
        if (event.y < triangle_points[1] + point_size*2) && (event.y > triangle_points[1] - point_size*2):
            point1 = True

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
        demo_step += 1			#Move to next step of demo.

    elif demo_step == 1:		#Student picks their own random path.
        if click_counter < 10:
            whichPoint(event, triangle_points)
            click_counter +=1
            if click_counter == 10:	#Move to next step of demo.
                demo_step +=1
        

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