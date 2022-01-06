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
import fileList as fL
#import filenamewindow

import mat73 
import scipy.io

class filenamewindow3:
    #Constructor
    def load_data(self):
        print("current file load")
        if fL.File is not None :
            mat = mat73.loadmat(fL.File)
            self.c = mat["map_t3"]
    
    def button_clicked(self):
        print('Button clicked')
    
    def __init__(self, app): 
        self.frame3 = LabelFrame(app, text = "2D image", bg = "white", padx = 100, pady = 30)
        self.frame3.grid(row=4, column=0,  sticky='nsew')
        
        self.b1 = Button(self.frame3, text="Show image", command=self.show_plot).pack()#self.show_plot(filename)).pack()
        self.draw = drawing()
        
    def show_plot(self):
        print("No worky")
        c = self.load_data()
        self.draw.addImageMean(c)
        self.draw.plotImage(0)
        
        
