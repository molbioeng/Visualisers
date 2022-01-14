# import the tkinter library
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import tkinter

from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

import fileList as fL

#FRAME 2 – METHOD SELECTION

class filenamewindow2(LabelFrame):

    #Constructor

    def __init__(self, container):
        super().__init__(container)
        self.frame2 = LabelFrame(container, text = "Select method", bg = "white", padx = 120, pady = 50) # Constructing the second frame, frame2

        # configuration of grid on frame
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)

        # Displaying the frame2 in row 0 and column 1
        self.frame2.grid(row=2, column=0, sticky='nsew')


        self.options = ["Mean","PCA", "K-Means Clustering"]

        self.var2 = StringVar()

        self.var2.set(self.options[0]) #.index())

        print("method in frame 2 is...",fL.method)

        # Variable to keep track of the option
        # selected in OptionMenu
        self.drop2 = OptionMenu(self.frame2, self.var2, *self.options)

        self.drop2.grid(column=0, row=0)

        self.btn2= Button(self.frame2, text="Confirm Selection", command=self.show).grid(row=0, column=1)
        self.label = Label(self.frame2, text=str(self.var2.get() + " Selected"))
        self.label.grid(column=0, row=2, columnspan=2)

    def show(self):
        fL.method = self.var2.get()
        self.label['text'] = str(fL.method + " Selected")
