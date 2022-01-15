#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 13:04:20 2021

@author: aron
"""

# Import the library tkinter
from tkinter import *
import tkinter as tk
from newuser_pop import *
from newuser_instructions import *

from app import *

from main_frame import *
from frame1 import filenamewindow
from frame2 import filenamewindow2
from frame3 import filenamewindow3
from frame4 import filenamewindow4
from ImageViewerPop import imgviewPop


import fileList as fL
fL.init()

class MainApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        
        frame = main_frame(self)

        # new user pop up
        a = newuser_pop(master=self)
        a.wm_attributes("-topmost", 1) # allows the newuser_pop to appear above the app window
        
        self.geometry('850x550')
        
        ################################################################################
        #FRAME 1
        
        
        self.filenamewindow1=filenamewindow(frame.second_frame, self)
        
        ################################################################################
        #FRAME 4 – 3D array selection
        
        self.filenamewindow4=filenamewindow4(frame.second_frame, self)
        
        ################################################################################
        #FRAME 2
        
        
        self.filenamewindow2=filenamewindow2(frame.second_frame, self)
        
        ################################################################################
        #FRAME 3
        
        
        self.filenamewindow3=filenamewindow3(frame.second_frame, self)
        
        #Image Viewer Frame
    #filenamewindow5(frame.second_frame, imgDB=filenamewindow3.draw.imgDB.images)

if __name__ == "__main__":
    #root = tk.Tk()
    #MainApp(root).pack(side="top", fill="both", expand=True)
    app = MainApp()
    app.mainloop()


# Create a GUI app
#app = App()
#frame = main_frame(app)

# new user pop up
# a = newuser_pop(master=app)
# a.wm_attributes("-topmost", 1) # allows the newuser_pop to appear above the app window

# #Global variables
# fL.init()

# ################################################################################
# #FRAME 1


# filenamewindow1=filenamewindow(frame.second_frame, app)

# ################################################################################
# #FRAME 4 – 3D array selection

# filenamewindow4=filenamewindow4(frame.second_frame, app)

# ################################################################################
# #FRAME 2


# filenamewindow2=filenamewindow2(frame.second_frame, app)

# ################################################################################
# #FRAME 3


# filenamewindow3=filenamewindow3(frame.second_frame, app)

#Image Viewer Frame
#filenamewindow5(frame.second_frame, imgDB=filenamewindow3.draw.imgDB.images)


# Make the loop for displaying app
#app.mainloop()
