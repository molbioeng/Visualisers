#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 13:04:20 2021

@author: aron
"""

# Import the library tkinter
from tkinter import *
from newuserPop import *
from newuser_instructions import *

from app import *

from main_frame import *
from frame1 import filename_select_frame
from frame2 import array_select_frame
from frame3 import method_select_frame
from frame4 import plot_frame


import fileList as fL

# Create a GUI app
app = App()
frame = main_frame(app)

# new user pop up
a = newuser_pop(master=app)
a.wm_attributes("-topmost", 1)

#Global variables
fL.init()

################################################################################

#FRAME 1


frame1=filename_select_frame(frame.second_frame)

#filename="tissue_t3_2_workspace_old.mat"
#print(filename)

################################################################################

#FRAME 2 – 3D array selection

frame2=array_select_frame(frame.second_frame)

################################################################################
#FRAME 3


frame3=method_select_frame(frame.second_frame)

################################################################################
#FRAME 4


frame4=plot_frame(frame.second_frame)




# Make the loop for displaying app
app.mainloop()
