#!/usr/bin/python

import os
from subprocess import *
from Tkinter import *
from tkMessageBox import *
import time
import sys

#******************
#Setup MPI
#******************
from mpi4pi import MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()

print str(sys.argv)
