
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
The first frame on the main app window. It contains an button that opens an open file dialog box
and widgets that allow the user to select the file they want to analyze.
"""

# Import the tkinter library
import tkinter

from tkinter import *
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from PIL import ImageTk, Image
import os

import fileList as fL
from frame4 import filenamewindow4
from ErrorPopupWindows import FileSelectionPopup

#FRAME 1 – OPEN AND SELECT FILE

#BUTTON 1 – FILENAME
class filenamewindow(LabelFrame):
    def __init__(self, container):
        super().__init__(container)
        # configuration of grid on frame
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        
        # logo = Image.open('kepu.png')
        # logo = ImageTk.PhotoImage(logo)
        # logo_label=tkinter.Label(image=logo, bg = "white")
        # logo_label.image = logo
        # logo_label.grid(column=0, row=0, sticky='nsew' )

        # textunderlogo = tkinter.Label(app, text="This is an application for visualising Raman Data.", bg = "white")
        # textunderlogo.grid(column=0, row=1,  sticky='nsew')
            
        
        self.frame1 = LabelFrame(container, text = "Select file", bg = "white", padx=120, pady=50)

        # Displaying the frame1 in row 0 and column 0
        self.frame1.grid(column=0, row=1, sticky="nsew")
                   
        # open button
        self.open_button = Button(self.frame1, text='Open Files', bg = "white", command=self.select_files)
        self.open_button.grid(row=0, column=0, columnspan=2)
        #self.open_button.grid_rowconfigure(1, weight=1)
        #self.open_button.grid_columnconfigure(1, weight=1)
            
        #Option menu
        self.value_inside = StringVar()
        self.button1 = Button(self.frame1, text="Select Filename from list",
                command= self.select_from_list).grid(row=1, column=1)
        self.om = None

        self.label = Label(self.frame1, text=self.value_inside.get())
        self.label.grid(row=2, column=0, columnspan=2, sticky="nsew")


    def select_files(self):
        self.filetypes = (("MAT files", "*.mat"), ("all files", ''))
        self.filenames = fd.askopenfilenames(
            title='Open a files',
            initialdir='/',
            filetypes=self.filetypes)
        print(type(self.filenames))
        self.filenames = list(self.filenames)

        # Update list and option menu
        for i in self.filenames:
            fL.List.append(i) #If there is none selected, don't ADD ANYTHING

        if (self.om == None) and len(fL.List) > 0: #Once the first file has been selected, display the list and 'select files button'
            self.value_inside.set(fL.List[0])
            self.om = OptionMenu(self.frame1, self.value_inside, *fL.List) #, command=self.show)

            self.om.grid(row=1, column=0, sticky="ne")
            
        else:
            menu = self.om["menu"]
            menu.delete(0, "end")
            for file in fL.List:
                 menu.add_command(label=file,
                              command=lambda value=file: self.value_inside.set(value))                
        

    def popup_window(self):
        FileSelectionPopup(self.frame1)

    def select_from_list(self):
        fL.File=self.value_inside.get() #.lstrip("(")
        #fL.File = fL.File.rstrip(")
        #print(fL.File)
        
        if not fL.File:
            self.popup_window()
        self.label['text'] = str(fL.File + " SELECTED") 

    def get_filename(self):
        return self.value_inside

