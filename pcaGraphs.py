'''
This class will be used to display window for PCA graphs
Created 8 Jan 2022
author: pg

'''


from tkinter import *

class pcaGraphs(Toplevel):
    def __init__(self,master=None):
        # using toplevel to create a new window that isn't root
        Toplevel.__init__(self, master)
        # configuring the pop up window
        self.title("Principal Component Analysis")
        self.geometry('800x600')

        # CONFIGURING GRID GEOMETRY OF WINDOW
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=2)

        buttony = ttk.Button(self, text="Submit", command=self.destroy)
        buttony.grid(column=0, row=10, columnspan=3, sticky=S, padx=10, pady=10)
