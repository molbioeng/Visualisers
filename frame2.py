#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 13:07:42 2021

@author: aron
"""
# Import the library tkinter
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os
import tkinter

from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

import fileList as fL

#FRAME 2 – FILENAME


class filenamewindow2:
    
    

    #Constructor
    def __init__(self, app):
        self.frame2 = LabelFrame(app, text = "Select method", bg = "white", padx = 50, pady = 30) # Constructing the second frame, frame2
        # Displaying the frame2 in row 0 and column 1
        self.frame2.grid(row=2, column=0, sticky='nsew')
        
        
        self.options = ["Mean","PCA", "K-Means Clustering"]
        
        self.var2 = StringVar()
        self.var2.set(self.options[0]) #.index())
        
        print("method in frame 2 is...",fL.method)
        
        # Variable to keep track of the option
        # selected in OptionMenu
        self.drop2 = OptionMenu(self.frame2, self.var2, *self.options)
        self.drop2.pack(side=RIGHT)
        
        self.btn2= Button(self.frame2, text="Select Method", command=self.show).pack()
        
        
    def show(self):
        fL.method = self.var2.get()
        myLabel = Label(self.frame2, text=str(fL.method)).pack()