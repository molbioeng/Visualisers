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

"""Initial method of Passing arguments between frame windows, in future versions
we would delete this but did not have enough time"""
fL.init() 

class MainApp(tk.Tk):
    """App class, used OOP to pass information between the frames"""
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title('Visualize')
        self.geometry('850x550')
        frame = main_frame(self)

        # Set a menu bar so users can access the instructions again
        menubar = Menu(self, background='#ff8000', foreground='black', activebackground='white', activeforeground='black')
        filemenu= Menu(menubar, tearoff=False)
        menubar.add_cascade(label= "Help",underline=0, menu= filemenu)
        filemenu.add_command(label="How to navigate Visualiser", underline= 1, command= self.instructions)
        self.config(menu=menubar)
        
        # New user pop up
        a = newuser_pop(master=self)
        a.wm_attributes("-topmost", 1) # allows the newuser_pop to appear above the app window

        
        self.geometry('850x550')
        
        ###THE FRAMES OF THE APP###

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

    def instructions(self):
        a = ft_instructions()


if __name__ == "__main__":
    """Create MainApp object and loop through it"""
    app = MainApp()
    app.mainloop()


