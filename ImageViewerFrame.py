import tkinter
from tkinter import *

import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import filedialog as fd
from tkinter import messagebox
import os

import mat73
import scipy
import scipy.io as sio
import numpy as np

import fileList as fL
from ErrorPopupWindows import ArraySelectionPopup

#IMAGE VIEWER FRAME - VIEW THROUGH ALL IMAGES PRODUCED USING THE APP

class filenamewindow5(Toplevel):
    #constructor
    def __init__(self, imgDB, master=None):
        # using toplevel to create a new window that isn't root
        Toplevel.__init__(self, master)
        # configuring the pop up window
        self.title("All Images")
        self.geometry('600x600')

        # CONFIGURING GRID GEOMETRY OF WINDOW
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        # Variables
        self.imgDB = imgDB
        self.imgDB_names = list(imgDB.keys())

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
        self.a = self.fig.add_subplot(111)
        self.a.axis('off')
        self.canvas_preview = FigureCanvasTkAgg(self.fig, self)
        
        if imgDB:
            self.imgList = list(imgDB.values())
            self.image = self.imgList[self.index]
            self.image = self.image.img
            print(self.imgDB_names[0])
            self.a.imshow(self.image)
            self.canvas_preview.draw()
            self.canvas_preview.get_tk_widget().grid(column=0, row=0, columnspan=2, sticky='EW')
            self.canvas_preview.get_tk_widget().configure(bg="grey")
            
        else:
            print("no Image yet")
    def back(self):
        #self.fig.clear()
        return

    def forward(self):
        #self.canvas_preview.clear()
        self.image = self.imgList[self.index+1]
        self.image = self.image.img
        self.a.imshow(self.image)
        self.canvas_preview.draw()
        self.canvas_preview.get_tk_widget().grid(column=0, row=0, columnspan=2, sticky='EW')
        self.canvas_preview.get_tk_widget().configure(bg="grey")
        return