from tkinter import *
import mat73
import scipy.io as sio
import numpy as np
import fileList as fL
from ErrorPopupWindows import ErrorPopup

#FRAME 2 – SELECTING 3D ARRAY

"""
The second frame on the main app window. Checks that the file selected by user is a .mat file that can be loaded
by the program and that contains a 3D array. The aim of the program is to apply data reduction techniques to 3D array
data for it to be visualized in an intuitive manner. If the file doesn't contain any 3D arrays, an error pop up window
will appear.

The frame also has widgets enabling the user to select which array out of those contained in the selected file,
they wish to analyze.
"""

class filenamewindow4(LabelFrame):
    #constructor
    def __init__(self, container):
        super().__init__(container)
        #constructing frame4
        self.frame4 = LabelFrame(container, text = "Select 3D array", bg = "white", padx=120, pady=50, width=300)

        #displaying the frame in row 2 and column 0
        self.frame4.grid(row=2, column=0, sticky='nsew')

        #configuration of grid on frame
        self.frame4.grid_columnconfigure(0, weight=1)
        self.frame4.grid_columnconfigure(1, weight=1)

        #"Browse Arrays" button
        self.main_btn = Button(self.frame4, text = "Browse Arrays", command = self.browse_arrays)
        self.main_btn.grid(row=0, column=0, columnspan=2)

    def browse_arrays(self):
        if not fL.File: #if no MATLAB file has been opened or confirmed, display error message
            fL.ErrorMessage = "Please open a MATLAB file and confirm your selection."
            self.popup_window()
        else:
            print(fL.File)

            fL.Data = self.open_file() #loading selected MATLAB file

            # filtering through arrays in MATLAB file and creating options list for dropdown menu
            self.options = self.filter_options(fL.Data) #keeps 3D arrays of floats, integers and unsigned integers
            # self.options = ["Testing"]

            self.var4 = StringVar()  # datatype of menu text
            self.var4.set(self.options[0])  # initial menu text

            # creating options dropdown menu
            self.drop4 = OptionMenu(self.frame4, self.var4, *self.options)
            self.drop4.grid(row=1, column=0, sticky='nsew')
            self.btn4 = Button(self.frame4, text="Confirm Selection", command=self.confirm).grid(row=1, column=1, sticky='nsew')
            self.label = Label(self.frame4, text="No Array Selected")
            self.label.grid(column=0, row=2, columnspan=2, sticky='nsew')


    def popup_window(self): #general error message popup window
        ErrorPopup(self.frame4)

    def confirm(self): #saves array selection
        try:
            fL.Array = fL.Data[self.var4.get()] #array data
            fL.Array_name = self.var4.get() #array name
            self.label['text'] = str(fL.Array_name + " Selected") #display selected array name
        except KeyError as e: #if array isn't selected, display error message
            #print("KeyError:", e)
            fL.ErrorMessage = "Please select a 3D array from the drop-down menu."
            self.popup_window()
        except Exception as e: #any other error
            print("Error:", e)

    def open_file(self): #loads MATLAB file
        try:
            selected_file = mat73.loadmat(fL.File) #for -v7.3 MATLAB files
        except Exception:
            try:
                selected_file = sio.loadmat(fL.File) #for previous versions of MATLAB files
            except Exception as e: #if import of MATLAB file doesn't work, display error message
                #print(e, "\n MATLAB file not supported.")
                fL.ErrorMessage = "MATLAB file not supported."
                self.popup_window()
        return selected_file

    def filter_options(self, file): #input = imported MATLAB file
        file_variables = list(file.keys()) #extracting workspace variables from MATLAB file & storing them in list
        menu_options = ["Select an array"] #dropdown menu options (default = "Select an array")
        class_list = [np.float32, np.float64, np.int8, np.uint8, np.int16, np.uint16, np.int32, np.uint32, np.int64, np.uint64] #accepted variable classes/types
        for i in range(len(file_variables)):
            if type(file[file_variables[i]]) == np.ndarray:
                if (file[file_variables[i]].squeeze().ndim == 3) and (np.array(list(file[file_variables[i]])).dtype in class_list) and (file[file_variables[i]].squeeze().shape[2] >= 3):
                #squeeze removes "empty" dimensions; keeping 3D arrays of floats, integers and unsigned integers; minimum z-dimension = 3
                    menu_options.append(file_variables[i])
        if menu_options == ["Select an array"]: #if no 3D arrays of numbers in file, display error message instead
            fL.ErrorMessage = "File selected does not contain 3D number data."
            self.popup_window()
            #menu_options.append("File selected does not contain 3D number data.")
        return menu_options
