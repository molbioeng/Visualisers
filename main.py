#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 13:04:20 2021

@author: aron
"""

# Import the library tkinter
from tkinter import *
from newuser_pop import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os
import tkinter

from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

from frame1 import filenamewindow
from frame2 import filenamewindow2
from frame3 import filenamewindow3

# Create a GUI app
app = Tk()

# Give a title to your app
app.title("Volumetric Data Visualiser")
app.iconbitmap('icon.ico')

# new user pop up
a = newuser_pop(master=app)
a.wm_attributes("-topmost", 1)



################################################################################

#FRAME 1


filenamewindow1=filenamewindow(app)
filename=filenamewindow1.value_chosen.get()
filename="tissue_t3_2_workspace_old.mat"
print(filename)
################################################################################
#FRAME 2


filenamewindow2=filenamewindow2(app)

################################################################################
#FRAME 3


filenamewindow3=filenamewindow3(app,filename)

# Make the loop for displaying app
app.mainloop()
