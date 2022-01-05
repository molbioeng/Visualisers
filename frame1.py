#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 13:05:18 2021
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

#BUTTON 1 – FILENAME

class filenamewindow:
    def select_files(self):
        self.filetypes = (
            ('text files', '*.png'),
            ('All files', '*.*')
        )
        self.filenames = fd.askopenfilenames(
            title='Open a files',
            initialdir='/',
            filetypes=self.filetypes)

        self.showinfo(
            title='Selected Files',
            message=self.filenames,
            lst = list(self.filenames)
        )



   # def show(self):
    #    myLabel = Label(frame1, text=self.value_inside.get()).pack()

        #Constructor
    def __init__(self, app):


            logo = Image.open('kepu.png')
            logo = ImageTk.PhotoImage(logo)
            logo_label=tkinter.Label(image=logo, bg = "white")
            logo_label.image = logo
            logo_label.grid(column=0, row=0, sticky='nsew' )


            textunderlogo = tkinter.Label(app, text="This is an application for visualising Raman Data.", bg = "white")
            textunderlogo.grid(column=0, row=1,  sticky='nsew')


            #self.create_image(20,20, anchor=NW, image=img)

            self.frame1 = LabelFrame(app, text = "Select file", bg = "white", padx = 55, pady = 100)

            self.filenames = ""

            # Displaying the frame1 in row 0 and column 0

            self.frame1.grid(row=2, column=0,  sticky='nsew')

           # open button
            open_button = tkinter.Button(self.frame1, text='Open Files', bg = "white", command=self.select_files)

            open_button.pack(expand=True)



            #self.frame1.filenames2 = filedialog.askopenfilenames(initialdir="/Users/Aron/Recents", title="Select a File",
                                            #filetypes=(("PNG files", "*.png"),("mat files", "*.mat"), ("all files", '')))






            # Variable to keep track of the option
            # selected in OptionMenu
            self.value_inside = tkinter.StringVar()
            self.value_chosen = self.value_inside
            self.value_inside.set("Select an Option") # Set the default value of the variable

            #self.button1 = Button(frame1, text = "Show Filename", command=self.show).pack()
            #self.btn2= Button(self.frame2, text="Show Method", command=self.show).pack()




            self.lst = list(self.filenames)
            if len(self.lst)!=0:
                self.drop1 = OptionMenu(self.frame1, self.value_inside, *self.lst)
                self.drop1.pack(side=RIGHT, anchor="ne")

            #self.button1 = Button(self.frame1, text = "Select Filename from list", command=self.select_from_list(self.value_inside)).pack()


    def show(self):
            myLabel = Label(self.frame1, text=self.value_inside.get()).pack()

    def select_from_list(self, value):
        self.value_chosen=value

    def update_value_inside(self, value):
        self.value_inside=value
