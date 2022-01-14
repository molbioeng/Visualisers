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
from ErrorPopupWindows import ArraySelectionPopup

"""
Pop up window with display of all images in image database (ImageDB). The display is mouse click sensitive, if 
clicked it will create a pop up of the same image in its matplotlib interactive version.  
"""

#IMAGE VIEWER FRAME - VIEW THROUGH ALL IMAGES PRODUCED USING THE APP

class ImgViewPop(Toplevel):
    #constructor
    def __init__(self, imgDB, master=None):
        # using toplevel to create a new window that isn't root
        Toplevel.__init__(self, master)
        # configuring the pop up window
        self.title("All Images")
        self.geometry('600x400')

        # CONFIGURING GRID GEOMETRY OF WINDOW
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

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

        # THE CONSTRUCTOR BELOW WAS TO HAVE THIS AS A FRAME IN THE APP WINDOW
    #def __init__(self, container, imgDB):
        #super().__init__(container)
        #constructing frame4
        #self.imgframe = LabelFrame(container, text = "View All Images Produced", bg = "white", padx=120, pady=50)
        #self.imgframe.grid(row=8, column=0, sticky="NSEW")

        
        #self.imgList = list(imgDB.values())
        #imgdb[name]
        
        self.fig = Figure()
        self.fig.suptitle(self.imgDB_names[0])
        self.a = self.fig.add_subplot(111)
        self.a.axis('off')
        self.canvas_preview = FigureCanvasTkAgg(self.fig, self)
        self.canvas_preview.mpl_connect('button_press_event', self.onclick_display)
        
        if imgDB:
            self.imgList = list(imgDB.values())
            self.image = self.imgList[self.index]
            self.image = self.image.img
            print("these are the objects in imgDB", self.imgList)

            # PLOTTING
            mappable = self.a.imshow(self.image)
            self.fig.colorbar(mappable)
            self.canvas_preview.draw()
            self.canvas_preview.get_tk_widget().grid(column=0, row=0, columnspan=2, sticky='EW')
            self.canvas_preview.get_tk_widget().configure(bg="grey")
            
        else:
            print("no Image yet")

    def back(self):
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
            self.canvas_preview.get_tk_widget().configure(bg="grey")

        #self.fig.clear()
        return

    def forward(self):
        #self.canvas_preview.clear()
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
            self.canvas_preview.get_tk_widget().configure(bg="grey")
        return

    def onclick_display(self, event):
        print("this has been clicked")
        self.image = self.imgList[self.index]
        if type(self.image) is ImagePCA.ImagePCA:
            pc_n_str = str(self.image)
            pc_n = int(pc_n_str[-1])
            print(pc_n)
            self.image.display(pc_n)
        else:
            self.image.display()