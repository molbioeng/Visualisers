'''
This class will be used to display window for PCA graphs
Created 8 Jan 2022
author: pg

'''
from tkinter import *
import tkinter as tk
from tkinter import ttk
import os
from ImagePCA import ImagePCA

class pcaGraphs(Toplevel):

    def __init__(self, pca_image, master=None):

        self.image = pca_image
        self.image.data_frames() #To get access to all data inside the image

        # self.is_error = False #Used to switch error labels when the user does not select anything
        # self.no_select_error = Label(self, text = "None of the graphs has been selected.", fg='red')

        Toplevel.__init__(self, master)
        self.geometry('400x500')
        self.title("Principal Component Analysis")
        self.columnconfigure(0, weight=1)

        label = tk.Label(self, text = "Select which graphs to plot:")
        label.grid(column=0,row=0, pady=(0,15))

        self.cb_var1 = IntVar()
        self.cb_var2 = IntVar()
        self.cb_var3 = IntVar()

        #CHECKBUTTONS
        cb_1 = Checkbutton(self, text="Scree plot", variable=self.cb_var1)
        cb_1.grid(column=0, row=1)
        cb_2 = Checkbutton(self, text="Scores plot", variable=self.cb_var2)
        cb_2.grid(column=0, row=2)
        cb_3 = Checkbutton(self, text="Loadings plot", variable=self.cb_var3)
        cb_3.grid(column=0, row=3)


        buttonConfirm = ttk.Button(self, text="Confirm", command=self.display_plots)
        buttonConfirm.grid(column=0, row=4, columnspan=3, sticky=S, padx=10, pady=10)

        buttonClose = ttk.Button(self, text="Close", command=self.destroy)
        buttonClose.grid(column=0, row=5, columnspan=3, sticky=S, padx=10, pady=10)

    def display_plots(self):
        if self.cb_var1.get()==0 and self.cb_var2.get()==0 and self.cb_var3.get()==0:
            no_select_error = Label(self, text = "None of the graphs has been selected.", fg='red')
            no_select_error.grid(column=0,row=6, pady=(0,15))
            print('Nothing has been selected')
            # self.is_error = True

        if self.cb_var1.get() == 1:
            print('Scree plot selected')
            self.image.scree_plot()
            # if self.is_error == True:
            #     self.no_select_error.grid_remove()
            #     self.is_error=False
        if self.cb_var2.get() == 1:
            print('Scores plot selected')
            self.image.scores_plot()
            # if self.is_error == True:
            #     self.no_select_error.grid_remove()
            #     self.is_error=False
        if self.cb_var3.get() == 1:
            self.image.loadings_plot()
            print('Loadings plot selected')
            # if self.is_error == True:
            #     self.no_select_error.grid_remove()
            #     self.is_error=False
