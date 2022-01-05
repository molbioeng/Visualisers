#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 16:20:18 2021

@author: aron
"""
# Import the library tkinter
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os
import tkinter
from tkinter import messagebox as tkMessageBox

from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

from drawing import drawing
#import filenamewindow

import mat73 
import scipy.io

class filenamewindow3:
    #Constructor
    def load_data(self, filename):
        if filename is not None :  
            mat = scipy.io.loadmat(filename)
            return mat["map_t3"]
    
    def button_clicked(self):
        print('Button clicked')
    
    def __init__(self, app, filename):
        self.filename=filename
        self.frame3 = LabelFrame(app, text = "2D image", bg = "white", padx = 100, pady = 30)
        self.frame3.grid(row=4, column=0,  sticky='nsew')
        
        self.b1 = Button(self.frame3, text="Show image", command=self.show_plot).pack()#self.show_plot(filename)).pack()
        
    def show_plot(self):
        self.c = self.load_data(self.filename)
        self.draw = drawing()
        self.draw.addImageMean(self.c)
        self.draw.plotImage(0)
        
        
