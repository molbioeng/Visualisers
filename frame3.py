# import the tkinter library
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
from ErrorPopupWindows import ImagePopup, FileSelectionPopup
from LoadingsDB import LoadingsDB
from pcaPop import pcaPop

#FRAME 3 - SHOW 2D IMAGE

import mat73
import scipy.io

class filenamewindow3(LabelFrame):
    #Constructor
    def load_data(self):
        """Update the Array"""
        print("current file load")
        if fL.File is not None :
            print(fL.File)
            mat = mat73.loadmat(fL.File)
            return fL.Array

    def button_clicked(self):
        print('Button clicked')

    def __init__(self, container):
        super().__init__(container)
        self.frame3 = LabelFrame(container, text = "2D image", bg = "white", padx = 120, pady = 50)
        self.frame3.grid(row=3, column=0, sticky='nsew')

        # configuration of grid on frame
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)


        self.b1 = Button(self.frame3, text="Show Image", command=self.show_plot).grid(column=0, row=0, columnspan=2)#self.show_plot(filename)).pack()

        self.draw = drawing()
        self.ldb = LoadingsDB()

    def popup_window(self):
        FileSelectionPopup(self.frame3)

    def show_plot(self):
        print("No worky")
        c = self.load_data()
        print("Selected option is " , fL.method)
        #"Mean","PCA", "K-Means Clustering"
        if fL.method == "Mean":
            print("Adding mean...")
            self.draw.addImageMean(c)
            self.draw.displayImage(0)

        elif fL.method == "PCA":
            self.pcaPop = pcaPop(self.ldb, fL.Array)
            #testing
            print("this is from frame 3",self.ldb)


        #if self.method == 0:
        #
        #else:
        #    print("Selected option is 1")

        #if array and method not select, display warning message
        # if not fL.Array and fL.method:
        #     self.popup_window()
