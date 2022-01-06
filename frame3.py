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
        """Update the Array"""
        print("current file load")
        if fL.File is not None :
            print(fL.File)
            mat = mat73.loadmat(fL.File)
            return mat["map_t3"]
    
    def button_clicked(self):
        print('Button clicked')
    
    def __init__(self, app): 
        self.frame3 = LabelFrame(app, text = "2D image", bg = "white", padx = 50, pady = 30)
        self.frame3.grid(row=3, column=0,  sticky='nsew')
        
        
        self.b1 = Button(self.frame3, text="Show image", command=self.show_plot).pack()#self.show_plot(filename)).pack()
        self.draw = drawing()
        
    def show_plot(self):
        
        print("No worky")
        c = self.load_data()
        print("Selected option is " , fL.method)
        #"Mean","PCA", "K-Means Clustering"
        if fL.method == "Mean":
            print("Adding mean...")
            self.draw.addImageMean(c)
            self.draw.displayImage(0)
        #if self.method == 0:
        #    
        #else:
        #    print("Selected option is 1")
        
        
        
