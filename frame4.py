# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 11:23:47 2022

@author: thefr
"""


# Import the library tkinter
import tkinter
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox
import os
#import requests

import mat73
import scipy
import scipy.io as sio
import numpy as np
import fileList as fL

#FRAME 4 – SELECTING 3D ARRAY

class filenamewindow4:
    #constructor
    def __init__(self, app):
        #constructing frame4
        self.frame4 = LabelFrame(app, text = "Select 3D array", bg = "white",padx = 50, pady = 30)

        #displaying the frame in row 3 and column 0
        #self.frame4.grid(row=3, column=0, sticky='nsew')
        self.frame4.grid(row=1, column=0, sticky='nsew')

        self.main_btn = Button(self.frame4, text = "Browse Arrays", command = self.browse_arrays).pack()

        '''
        self.filename = fL.File
        self.filename2 ='/Users/Shirin/Desktop/Prog3 Project/tissue_t3_1_workspace.mat'
        #self.filename = self.select_files()

        #opening selected MATLAB file
        print("this works",self.filename)

        self.selected_files = self.open_file(self.filename2)

        #filtering through arrays in MATLAB file and creating options list for dropdown menu
        self.options = self.filter_options(self.selected_files)
        #self.options = ["Testing"]

        self.var4 = StringVar() #datatype of menu text
        self.var4.set(self.options[0]) #initial menu text

        #creating dropdown menu
        self.drop4 = OptionMenu(self.frame4, self.var4, *self.options)
        self.drop4.pack(side=RIGHT)

        self.btn4= Button(self.frame4, text = "Show Array", command=self.show).pack()
        '''


    def browse_arrays(self):
        #self.filename = fL.File
        #self.filename2 = '/Users/Shirin/Desktop/Prog3 Project/tissue_t3_1_workspace.mat'
        # self.filename = self.select_files()

        # opening selected MATLAB file
        #print("this works", fL.File)
        print(fL.File)
        print("/Users/Shirin/Desktop/Prog3 Project/tissue_t3_1_workspace.mat")


        self.selected_files = self.open_file()

        # filtering through arrays in MATLAB file and creating options list for dropdown menu
        self.options = self.filter_options(self.selected_files)
        # self.options = ["Testing"]

        self.var4 = StringVar()  # datatype of menu text
        self.var4.set(self.options[0])  # initial menu text

        # creating dropdown menu
        self.drop4 = OptionMenu(self.frame4, self.var4, *self.options)
        self.drop4.pack(side=RIGHT)

        self.btn4 = Button(self.frame4, text="Show Array", command=self.show).pack()

    def show(self):
        myLabel = Label(self.frame4, text=self.var4.get()).pack()
        #print(fL.File)

    def open_file(self):
        try:
            selected_file = mat73.loadmat(fL.File)
        except Exception:
            try:
                selected_file = sio.loadmat(fL.File)
            except Exception as e:
                print(e, "\n MATLAB file not supported.")
            finally:
                selected_file = "dummy"
        return selected_file

    # def open_file(self):
    #     global selected_file
    #     filename = fd.askopenfilename(initialdir = "/",filetypes = (("MAT files", "*.mat"), ("all files", '')))
    #     try:
    #         selected_file = mat73.loadmat(filename)
    #     except Exception:
    #         try:
    #             selected_file = sio.loadmat(filename)
    #         except Exception as e:
    #             print(e, "\n MATLAB file not supported.")
    #     return selected_file

    def filter_options(self, file):
        file_variables = list(file.keys())
        menu_options = ["Select an array"]
        class_list = [np.float32, np.float64, np.int8, np.uint8, np.int16, np.uint16, np.int32, np.uint32, np.int64, np.uint64]
        for i in range(len(file_variables)):
            if type(file[file_variables[i]]) == np.ndarray:
                if (file[file_variables[i]].squeeze().ndim == 3) and (np.array(list(file[file_variables[i]])).dtype in class_list):
                    menu_options.append(file_variables[i])
        if menu_options == ["Select an array"]:
            menu_options.append("File selected does not contain 3D number data.")
            #tkinter.messagebox.showerror("Warning", "File selected does not contain 3D number data.")
        return menu_options

