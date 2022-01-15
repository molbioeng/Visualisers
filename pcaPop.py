from tkinter import *
from tkinter import filedialog
import os
import tkinter
# from tkinter import font
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

import tkinter as tk
from tkinter import ttk
import matplotlib

matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

import mat73
from Image import Image
from PrincipalComponent import PrincipalComponent
import numpy as np
from ImagePCA import ImagePCA
from PrincipalComponentDB import*
import fileList as fL
from pcaGraphs import pcaGraphs

"""
Pop up window that enables user to select the settings for PCA data reduction and plotting.
They can either plot based on PCs calculated for a previous data set or generate new ones for the current
data set. 
"""

class pcaPop(Toplevel):  # Create a window
    def __init__(self, pcdb, data, draw, master=None):
        # using toplevel to create a new window that isn't app
        Toplevel.__init__(self, master)
        # configuring the pop up window
        self.title("PCA Settings")
        self.geometry('800x600')

        # CONFIGURING GRID GEOMETRY OF WINDOW
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=2)

        # variables for PCA analysis
        self.pcdb = pcdb
        self.pcdb_names = list(pcdb.keys())
        self.data = data
        self.new_pc =False
        self.pca_t3 = None
        self.imgdb = draw
        self.did_select = False # Used to check if the user had selected PC

        # TITLE ON WINDOW AND SUBMIT BUTTON

        buttonX = ttk.Button(self, text="Submit", command=self.submit)
        buttonX.grid(column=0, row=10, columnspan=3, sticky=S, padx=10, pady=10)

        # DROP DOWN MENU WITH PREVIOUSLY CALCULATED PCs USER CAN SELECT FOR PLOTTING

        print("This is pcdb before if", self.pcdb_names)
        if len(self.pcdb_names)!=0:
            self.dd_var = StringVar()
            print("This is first dd_var ",self.dd_var)
            self.dd_var.set(self.pcdb_names[0])
            print("This is second dd_var ",self.dd_var)

            # label for drop down menu
            drop_down_text = "If you would like to use PCs from a previous image please select:"
            self.dd_label = Label(self, text=drop_down_text, font="lucida 14")
            self.dd_label.grid(column=0, row=0, columnspan=2, sticky=N, padx=10, pady=(15, 5))

            new_pc_label = "Create new PCs"
            self.pcdb_names.insert(0,new_pc_label)
            self.drop = OptionMenu(self, self.dd_var, *self.pcdb_names)
            self.drop.grid(column=0, row=1, columnspan=2, sticky=N, padx=10, pady=5)
            self.cfm_opt_btn = Button(self, text="Confirm Selection", command=self.get_sel_principal_component)
            self.cfm_opt_btn.grid(column=2, row=1, sticky=N, pady=10, padx=10)

        # PC RADIOBUTTON CODE - SELECTING PCs

        # label at the top of the check list
        self.cl_label = Label(self, text="Select PC to be included in the image:", font="lucida 14 underline")
        self.cl_label.grid(column=0, row=3, pady=(15, 5))

        # variables to store on/off value of radiobutton
        self.rb_var = IntVar()
        self.rb_var.set(0)

        # Radiobuttons
        self.rb_1 = Radiobutton(self, text="PC 1", variable=self.rb_var, value=1, command=lambda: self.display_preview(self.rb_var.get()))
        self.rb_1.grid(column=0, row=4)

        self.rb_2 = Radiobutton(self, text="PC 2", variable=self.rb_var, value=2, command=lambda: self.display_preview(self.rb_var.get()))
        self.rb_2.grid(column=0, row=5)

        self.rb_3 = Radiobutton(self, text="PC 3", variable=self.rb_var, value=3, command=lambda: self.display_preview(self.rb_var.get()))
        self.rb_3.grid(column=0, row=6)

        # PREVIEW BOX
        # title
        self.pb_label = Label(self, text="Preview Image", font="lucida 13 bold")
        self.pb_label.grid(column=1, row=3, columnspan=2, sticky='N', pady=(15, 0))
        self.image = None

    # setting up canvas
    # self.canvas_preview = Canvas(self, height=400, bd=0, bg='Grey')
    # self.canvas_preview.grid(column=1, row=4, columnspan=2, rowspan=6, sticky='EW')

    # PREVIEW BOX CODE

    # canvas = FigureCanvasTkAgg(f,self)
    # canvas.draw()
    # # # canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True )
    # canvas.get_tk_widget().grid(column=0,row=11, columnspan=3, sticky=S, padx=10, pady=10)
    # canvas.get_tk_widget().configure(bg="black")

    # self.canvas_preview2 = FigureCanvasTkAgg(f,self)
    # self.canvas_preview2.draw()
    # # canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True )
    # self.canvas_preview2.get_tk_widget().grid(column=1,row=4, columnspan=2,rowspan=6, sticky='EW')
    # self.canvas_preview2.get_tk_widget().configure(bg="grey")

    def get_sel_principal_component(self):
        """ Confirms user selection in drop down menu (through label) and stores it.
        """
        if self.dd_var.get()=="Create new PCs":
            pc_selected_text = 'User selected \'Create new PCs\''
            print(pc_selected_text)
            self.new_pc = True
        else:
            self.pca_t3=self.pcdb[self.dd_var.get()]
            pc_selected_text = self.dd_var.get()+' has been selected'
        label_pc_selected = Label(self, text=pc_selected_text, font="lucida 14")
        label_pc_selected.grid(column=0, row=1, columnspan=2, sticky=N, padx=10, pady=5)

    def display_preview(self, rb_var):
        """ Plots on preview box based on PC chosen
        """
        self.did_select=True
        f = Figure()
        a = f.add_subplot(111)
        a.axis('off')

        # if there is saved PCs
        # if ldb length is none --->
        # else pca_new = self.ldb[selected]
        # new_image = ImagePCA(self.data,)
        # img = new_image.return_Image()
        # img.display()
        if (self.pca_t3==None) or (self.new_pc==True):
            self.pca_t3 = PrincipalComponent(array=self.data)
            self.new_pc=False
            #new_pc= False
        # if self.new_pc==True:
        #     self.pca_t3 = PrincipalComponent(array=self.data)
        #     self.new_pc=False
        #     print('new_pc is true!')

        self.image = ImagePCA(self.data, self.pca_t3)
        
        self.canvas_preview = FigureCanvasTkAgg(f, self)


        if rb_var == 1:
            print('Var1 is 1')
            self.image.img = self.image.return_Image(1)
            a.imshow(self.image.img)
            self.canvas_preview.draw()
            self.canvas_preview.get_tk_widget().grid(column=1, row=4, columnspan=2, rowspan=6, sticky='EW')
            self.canvas_preview.get_tk_widget().configure(bg="grey")

        elif rb_var == 2:
            print('Var2 is 1')
            self.image.img = self.image.return_Image(2)
            a.imshow(self.image.img)
            self.canvas_preview.draw()
            self.canvas_preview.get_tk_widget().grid(column=1, row=4, columnspan=2, rowspan=6, sticky='EW')
            self.canvas_preview.get_tk_widget().configure(bg="grey")

        elif rb_var == 3:
            print('Var3 is 1')
            self.image.img = self.image.return_Image(3)
            a.imshow(self.image.img)
            self.canvas_preview.draw()
            self.canvas_preview.get_tk_widget().grid(column=1, row=4, columnspan=2, rowspan=6, sticky='EW')
            self.canvas_preview.get_tk_widget().configure(bg="grey")
        else:
            print('error')

    def submit(self):
        """ Creates interactive image based on PC chosen, defines a name and adds object to Image Database
        """
        if self.pca_t3 is None or self.did_select==False:
            submit_error_text = "Please select PC before submitting."
            print(submit_error_text) #To display error in terminal
            submit_error_label = Label(self, text=submit_error_text, font="lucida 14", fg='red')
            submit_error_label.grid(column=1, row=11, pady=10)
        else:
            self.destroy()
            self.pcaGraphs = pcaGraphs(self.image)
            self.pcdb[self.pca_t3.name] = self.pca_t3
            self.image.name = self.image.name + '/' + str(self.rb_var.get())
            self.imgdb.addImage(self.image)
            self.image.display()


'''
# FOR TESTING
def openSettings():
    a=pcaPop()


def openSettings():
    a = pcaPop(master=app)


def select_files():
    app.filenames = fd.askopenfilenames(title='Open a files', initialdir='/')
    app.lst = list(app.filenames)

app = Tk()
app.geometry("400x400")
b1 = Button(app, text="Load Files", command=select_files)
b1.pack()
b2 = Button(app, text="Open PCA Settings", command=openSettings)
b2.pack()

app.mainloop()
'''
