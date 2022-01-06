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

import fileList as fL

#BUTTON 1 – FILENAME
class filenamewindow:
    def __init__(self, app):
        logo = Image.open('kepu.png')
        logo = ImageTk.PhotoImage(logo)
        logo_label=tkinter.Label(image=logo, bg = "white")
        logo_label.image = logo
        logo_label.grid(column=0, row=0, sticky='nsew' )

        textunderlogo = tkinter.Label(app, text="This is an application for visualising Raman Data.", bg = "white")
        textunderlogo.grid(column=0, row=1,  sticky='nsew')
            
        
        self.frame1 = LabelFrame(app, text = "Select file", bg = "white", padx = 55, pady = 100)

        # Displaying the frame1 in row 0 and column 0
        self.frame1.grid(row=2, column=0,  sticky='nsew')
                   
        # open button
        open_button = tkinter.Button(self.frame1, text='Open Files', bg = "white", command=self.select_files)
        open_button.pack(expand=True)
            
        #Option menu
        self.value_inside = tkinter.StringVar()
        currentFile = self.value_inside
        self.button1 = Button(self.frame1, text="Select Filename from list",
                command= self.select_from_list).pack()

            #self.value_inside.set("Select an Option") # Set the default value of the variable
            #self.om = OptionMenu(self.frame1, self.value_inside, *self.lst, command=self.show)
            #self.om.pack(side=RIGHT, anchor="ne")
        
            #self.button1 = Button(self.frame1, text="Select Filename from list",
             #                 command=self.select_from_list(self.value_inside)).pack()
            
            #self.button1 = Button(frame1, text = "Show Filename", command=self.show).pack()
            #self.btn2= Button(self.frame2, text="Show Method", command=self.show).pack()
            
            
    def select_files(self):
        self.filetypes = (("MAT files", "*.mat"), ("all files", ''))
        self.filenames = fd.askopenfilenames(
            title='Open a files',
            initialdir='/',
            filetypes=self.filetypes)
        
        # Update list and option menu
        fL.List.append(list(self.filenames))
        if len(fL.List)==1: #Once the first file has been selected, display the list and 'select files button'
            self.value_inside.set(fL.List[0])
            self.om = OptionMenu(self.frame1, self.value_inside, *fL.List) #, command=self.show)
            self.om.pack(side=RIGHT, anchor="ne")
            
        else:    
            menu = self.om["menu"]
            menu.delete(0, "end")
            for file in fL.List:
                menu.add_command(label=file, 
                             command=lambda value=file: self.value_inside.set(value))
                   
        
    def show(self): 
        myLabel = Label(self.frame1, text=self.value_inside.get()).pack()
        #return value_inside.get()
            
    def select_from_list(self):
        fL.File=self.value_inside.get().lstrip("(")
        fL.File = fL.File.rstrip(",)")
        print(fL.File)

        
    def get_filename(self):
        return self.value_inside
        
            
        
        
