import tkinter
from tkinter import *

import matplotlib
from matplotlib import pyplot as plt

matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import ImagePCA
from tkinter import filedialog as fd
from tkinter import messagebox
import os

import mat73
import scipy
import scipy.io as sio
import numpy as np

import fileList as fL

#IMAGE VIEWER POP - VIEW THROUGH ALL IMAGES PRODUCED USING THE APP

"""
Pop up window with display of all images in image database (ImageDB). The display is mouse click sensitive, if 
clicked it will create a pop up of the same image in its matplotlib interactive version.  
"""


class imgviewPop(Toplevel):
    #constructor
    def __init__(self, imgDB, master=None):
        # using toplevel to create a new window that isn't root
        Toplevel.__init__(self, master)
        # configuring the pop up window
        self.title("All Images")
        self.geometry('600x400')

        # CONFIGURING GRID GEOMETRY OF WINDOW
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        # Variables
        self.imgDB = imgDB
        self.imgDB_names = list(imgDB.keys())
        #print(fL.Pc_n)
        #print("this is from image viewer", self.pcaDict)

        # Buttons
        button_back = Button(self, text="<<", command=self.back)
        button_back.grid(row=1, column=0)
        button_forward = Button(self, text=">>", command=self.forward)
        button_forward.grid(row=1, column=1)

        #index
        self.index = 0
        
        self.fig = Figure()
        self.fig.suptitle(self.imgDB_names[0])
        self.a = self.fig.add_subplot(111)
        self.a.axis('off')
        self.canvas_preview = FigureCanvasTkAgg(self.fig, self)
        # the next line allows the plot to be mouse click sensitive, and execute self.onclick_display
        # when there is a mouse button click on the plot
        self.canvas_preview.mpl_connect('button_press_event', self.onclick_display)
        
        self.imgList = list(imgDB.values())
        self.image = self.imgList[self.index]
        # The next line is necessary because .img allows us to access the actual array which is needed
        # for a.imshow plotting
        self.image = self.image.img
        
        # PLOTTING
        mappable = self.a.imshow(self.image)
        self.fig.colorbar(mappable)
        self.canvas_preview.draw()
        self.canvas_preview.get_tk_widget().grid(column=0, row=0, columnspan=2, sticky='EW')

    def back(self):
        """Command for backwards button, allowing us to change position in the list of image objects
        by going to previous object and plotting accordingly"""
        # If statement accounting for being at first position in index
        if self.index == 0:
            pass
        else:
            self.index = self.index-1
            self.image = self.imgList[self.index]
            self.image = self.image.img
            self.fig.suptitle(self.imgDB_names[self.index])
            self.a.imshow(self.image)

            self.canvas_preview.draw()
            self.canvas_preview.get_tk_widget().grid(column=0, row=0, columnspan=2, sticky='EW')
        return

    def forward(self):
        """Command for forwards button, allowing us to change position in the list of image objects
        by going to next object and plotting accordingly"""
        # If statement accounting for being at last position in index
        if self.index == len(self.imgList)-1:
            pass
        else:
            self.index = self.index+1
            self.image = self.imgList[self.index]
            self.fig.suptitle(self.imgDB_names[self.index])
            self.image = self.image.img
            self.a.imshow(self.image)
            self.canvas_preview.draw()
            self.canvas_preview.get_tk_widget().grid(column=0, row=0, columnspan=2, sticky='EW')
        return

    def onclick_display(self, event):
        """Command connected to mouse click event, produces the interactive plot from which you
        can get raw Raman spectra if user clicks mouse button on canvas"""
        self.image = self.imgList[self.index]
        # Produces the interactive plot from which you can get raw Raman spectra
        self.image.display()
