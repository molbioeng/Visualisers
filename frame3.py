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
from ErrorPopupWindows import ImagePopup, FileSelectionPopup, NoImageForKMCPopup
from PrincipalComponentDB import PrincipalComponentDB
from pcaPop import pcaPop
from KMClusterPop import KMClusterPop
from ImageMean import ImageMean
from ImageViewerPop import *

"""
The final frame on the main app window. Allows user to display an interactive image, generated based on selections made 
in previous frames, as well as from pop up setting windows. Each image displayed is stored in the 
image database (ImageDB). 

The frame contains a button that opens a window where the user can view all images contained in the image database.
"""


#FRAME 3 - SHOW 2D IMAGE

import mat73
import scipy.io as sio

class filenamewindow3(LabelFrame):
    #Constructor
    def load_data(self):
        """Update the Array"""
        print("current file load")
        if fL.File is not None :
            try:
                print(fL.File)
                mat = mat73.loadmat(fL.File)
                return fL.Array
            except NotImplementedError:
                print(fL.File)
                mat = sio.loadmat(fL.File)
            except:
                ValueError('Could not read at all')

    def button_clicked(self):
        print('Button clicked')

    def __init__(self, container):
        super().__init__(container)
        self.frame3 = LabelFrame(container, text = "2D image", bg = "white", padx = 120, pady = 50)
        self.frame3.grid(row=4, column=0, sticky="nsew")

        # configuration of grid on frame
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)


        self.b1 = Button(self.frame3, text="Show Image", command=self.show_plot).grid(column=0, row=0, columnspan=2)#self.show_plot(filename)).pack()

        self.draw = drawing()
        # self.ldb = LoadingsDB().loadingDB
        self.pcdb = PrincipalComponentDB().principalComponents

        self.b2 = Button(self.frame3, text="Show All Images", command=self.open_img_viewer).grid(column=0, row=1, columnspan=2)


    def open_img_viewer(self):
        self.img_viewer_pop = ImgViewPop(self.draw.imgDB.images)

    def popup_window(self):
        FileSelectionPopup(self.frame3)

    def show_plot(self):
        print("No worky")
        c = self.load_data()
        print("Selected option is " , fL.method)
        #"Mean","PCA", "K-Means Clustering"
        if fL.method == "Mean":
            print("Adding mean...")
            img_mean = ImageMean(c)
            self.draw.addImageMean(img_mean)
            self.draw.displayImage(img_mean)

        elif fL.method == "PCA":
            self.pcaPop = pcaPop(self.pcdb, fL.Array,draw=self.draw)

        elif fL.method == "K-Means Clustering":
            if bool(self.draw.imgDB.images):
                self.KMClusterPop = KMClusterPop(self.draw.imgDB.images)
            else:
                print('no images to work on')
                noImgPopup = NoImageForKMCPopup()
                #To display erroPopup window if there is no image class which user can apply KMClustering method to



        #if self.method == 0:
        #
        #else:
        #    print("Selected option is 1")

        #if array and method not select, display warning message
        # if not fL.Array and fL.method:
        #     self.popup_window()
