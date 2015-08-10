#!/usr/bin/env python
"""
Parallel Engine Wrapper
"""

from mpi4py import MPI
import sys
import os

size = MPI.COMM_WORLD.Get_size()
rank = MPI.COMM_WORLD.Get_rank()
name = MPI.Get_processor_name()

if rank == 0:		#Pecan reads in bash directive and passes it on.
    command = open('/home/pi/raspberry-pi/fractals/parallelthis.txt', 'r')
    commandtext = command.read()
    command.close()
else:
    commandtext = None

commandtext = MPI.COMM_WORLD.bcast(commandtext, root=0)

os.system(commandtext)


#Each pi runs the C back-end and gets their data.

cpoints = open('/home/pi/raspberry-pi/fractals/fractalpoints.txt', 'r')
mypoints = cpoints.read()
cpoints.close()
os.system("rm /home/pi/raspberry-pi/fractals/fractalpoints.txt") #Clean up.

mypoints = mypoints.split('\n') #Make the data nice to work with.
mypoints = mypoints[:-1]
for i in range(len(mypoints)):
    mypoints[i] = mypoints[i].split(' ')
    mypoints[i][0] = float(mypoints[i][0])
    mypoints[i][1] = float(mypoints[i][1])
    mypoints[i].append(rank)	#So Pecan knows where the point data came from.


#Pass all the data back to Pecan who writes it out into file.

if rank == 0:
    masterCopy = mypoints

for j in range(1, size):
    if rank == j:
        MPI.COMM_WORLD.send(mypoints, dest=0, tag=j)
    if rank == 0:
        incomming = MPI.COMM_WORLD.recv(source=j, tag=j)
        masterCopy.append(incomming)

#Pecan writes it all out to a file...the end.

if rank == 0:
    pointFile = open('fractalpoints.txt', 'w')
    for x in range(len(mypoints)):
        for y in range(size):
            pointFile.write(masterCopy[x+(y*x)][0])
            pointFile.write(" ")
            pointFile.write(masterCopy[y][x][1])
            pointFile.write(" ")
            pointFile.write(masterCopy[y][x][2])
            pointFile.write("\n")
    pointFile.close()
