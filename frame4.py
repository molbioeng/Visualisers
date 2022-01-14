import tkinter
from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox
import os

import mat73
import scipy
import scipy.io as sio
import numpy as np

import fileList as fL
from ErrorPopupWindows import ErrorPopup

#FRAME 4 – SELECTING 3D ARRAY

class filenamewindow4(LabelFrame):
    #constructor
    def __init__(self, container):
        super().__init__(container)
        #constructing frame4
        self.frame4 = LabelFrame(container, text = "Select 3D array", bg = "white", padx = 120, pady = 50)

        #displaying the frame in row 3 and column 0
        #self.frame4.grid(row=3, column=0, sticky='nsew')
        self.frame4.grid(row=2, column=0, sticky='nsew')

        # configuration of grid on frame
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=2)

        self.main_btn = Button(self.frame4, text = "Browse Arrays", command = self.browse_arrays)
        self.main_btn.grid(row=0, column=0, columnspan=2)


        #self.label = Label(self.frame4, text=(str(self.var4.get()) + " selected"))
        #self.label.grid(column=0, row=2, columnspan=2)

        #self.label = Label(self.frame4, text="No File Selected").pack()
        #print(type(self.label))

        # self.filename = fL.File
        # self.filename2 ='/Users/Shirin/Desktop/Prog3 Project/tissue_t3_1_workspace.mat'
        # #self.filename = self.select_files()
        #
        # #opening selected MATLAB file
        # print("this works",self.filename)
        #
        # self.selected_files = self.open_file(self.filename2)
        #
        # #filtering through arrays in MATLAB file and creating options list for dropdown menu
        # self.options = self.filter_options(self.selected_files)
        # #self.options = ["Testing"]
        #
        # self.var4 = StringVar() #datatype of menu text
        # self.var4.set(self.options[0]) #initial menu text
        #
        # #creating dropdown menu
        # self.drop4 = OptionMenu(self.frame4, self.var4, *self.options)
        # self.drop4.pack(side=RIGHT)
        #
        # self.btn4= Button(self.frame4, text = "Show Array", command=self.show).pack()

    def browse_arrays(self):
        #self.filename = fL.File
        #self.filename2 = '/Users/Shirin/Desktop/Prog3 Project/tissue_t3_1_workspace.mat'
        # self.filename = self.select_files()

        # opening selected MATLAB file
        #print("this works", fL.File)
        if not fL.File:
            fL.ErrorMessage = "Please open a MATLAB file and confirm your selection."
            self.popup_window()
        else:
            print(fL.File)

            fL.Data = self.open_file()

            # filtering through arrays in MATLAB file and creating options list for dropdown menu
            self.options = self.filter_options(fL.Data)
            # self.options = ["Testing"]

            self.var4 = StringVar()  # datatype of menu text
            self.var4.set(self.options[0])  # initial menu text

            # creating dropdown menu
            self.drop4 = OptionMenu(self.frame4, self.var4, *self.options)
            self.drop4.grid(row=1, column=0)
            self.btn4 = Button(self.frame4, text="Confirm Selection", command=self.confirm).grid(row=1, column=1)
            self.label = Label(self.frame4, text="No Array Selected")
            self.label.grid(column=0, row=2, columnspan=2)


    def popup_window(self):
        ErrorPopup(self.frame4)

    # def confirm(self):
    #     fL.Array = fL.Data[self.var4.get()]
    #     fL.Array_name = self.var4.get()
    #     self.label['text'] = str(fL.Array_name + " Selected")
    #     #print(fL.Array)

    def confirm(self):
        try:
            fL.Array = fL.Data[self.var4.get()]
            fL.Array_name = self.var4.get()
            self.label['text'] = str(fL.Array_name + " Selected")
        except KeyError as e:
            print("KeyError:", e)
            fL.ErrorMessage = "Please select a 3D array from the drop-down menu."
            self.popup_window()
        except Exception as e:
            print("Error:", e)

    def open_file(self):
        try:
            selected_file = mat73.loadmat(fL.File)
        except Exception:
            try:
                selected_file = sio.loadmat(fL.File)
            except Exception as e:
                #print(e, "\n MATLAB file not supported.")
                fL.ErrorMessage = "MATLAB file not supported."
                self.popup_window()
        return selected_file

    def filter_options(self, file):
        file_variables = list(file.keys())
        menu_options = ["Select an array"]
        class_list = [np.float32, np.float64, np.int8, np.uint8, np.int16, np.uint16, np.int32, np.uint32, np.int64, np.uint64]
        for i in range(len(file_variables)):
            if type(file[file_variables[i]]) == np.ndarray:
                if (file[file_variables[i]].squeeze().ndim == 3) and (np.array(list(file[file_variables[i]])).dtype in class_list):
                    menu_options.append(file_variables[i])
        if menu_options == ["Select an array"]:
            fL.ErrorMessage = "File selected does not contain 3D number data."
            self.popup_window()
            #menu_options.append("File selected does not contain 3D number data.")
            #tkinter.messagebox.showerror("Warning", "File selected does not contain 3D number data.")
        return menu_options
