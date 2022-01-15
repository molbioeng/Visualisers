from tkinter import *
import mat73
import scipy.io as sio
import numpy as np
import fileList as fL
import os
from ErrorPopupWindows import ErrorPopup

#FRAME 4 – SELECTING 3D ARRAY

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
    def __init__(self, container, controller):
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
        
        self.drop4 = None

    def browse_arrays(self):
        """ Checks if a MATLAB file has been loaded, then creates an option menu
        + confirm button for the user to browse through its corresponding arrays"""
        if not fL.File: #if no MATLAB file has been opened or confirmed, display error message
            fL.ErrorMessage = "Please open a MATLAB file and confirm your selection."
            self.popup_window()
        else:
            fL.Data = self.open_file() #loading selected MATLAB file
            

            # filtering through arrays in MATLAB file and creating options list for dropdown menu
            self.options = self.filter_options(fL.Data) #keeps 3D arrays of floats, integers and unsigned integers

            self.var4 = StringVar()  # datatype of menu text
            self.var4.set(self.options[0])  # initial menu text

            # creating options dropdown menu
            self.drop4 = OptionMenu(self.frame4, self.var4, *self.options)
            self.drop4.grid(row=1, column=0, sticky='nsew')
            self.btn4 = Button(self.frame4, text="Confirm Selection", command=self.confirm).grid(row=1, column=1, sticky='nsew')
            self.label = Label(self.frame4, text="No Array Selected")
            self.label.grid(column=0, row=2, columnspan=2, sticky='nsew')


    def popup_window(self): #general error message popup window
        """Error popup"""
        ErrorPopup(self.frame4)


    def check_ArrayDB(self,name, array):
        """Updates the ArrayDB, and assigns current_array to the selected file"""
        if name not in fL.arrdb.arrays.keys():
            fL.arrdb.addArray(array, name)
        fL.arrdb.current_array = name


    def confirm(self): 
        """Checks that a valid array has been selected, and saves array selection"""
        try:
            name = self.var4.get() 
            self.label['text'] = str(self.var4.get() + " Selected")
            name = (os.path.basename(fL.File)).rsplit(".", 1)[0] + '/' + name #Set array name
            self.check_ArrayDB(name, fL.Data[self.var4.get()])  #loads array data
        except KeyError as e: #if array isn't selected, display error message
            fL.ErrorMessage = "Please select a 3D array from the drop-down menu."
            self.popup_window()
        except Exception as e: #any other error
            fL.ErrorMessage = e
            self.popup_window()

    def open_file(self): #loads MATLAB file
        """Loads the MATLAB file, checks if it can be loaded"""
        try:
            selected_file = mat73.loadmat(fL.File) #for -v7.3 MATLAB files
        except Exception:
            try:
                selected_file = sio.loadmat(fL.File) #for previous versions of MATLAB files
            except Exception as e: #if import of MATLAB file doesn't work, display error message
                fL.ErrorMessage = "MATLAB file not supported."
                self.popup_window()
        return selected_file

    def filter_options(self, file): #input = imported MATLAB file
        """Runs through the MATLAB file and checks if there are valid arrays present
        + loads them into the option menu"""
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
        return menu_options
    
    def update(self):
        """Deletes the option menu, label, and 'Confirm selection' button after 
        new file has been selected to prevent the user from selecting invalid arrays"""
        if self.drop4:
            self.drop4.destroy()
            self.label.destroy()
            self.btn4.destroy()