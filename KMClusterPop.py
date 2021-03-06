from tkinter import *
from tkinter import ttk
import os
from ImageKMCluster import ImageKMCluster
from ImagePCA import ImagePCA

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

"""
Pop up window that enables user to select the settings for KM Clustering data reduction and plotting.
They user can enter the number of clusters they want to create, and see a preview of the image before
the interactive plot is generated.
"""

class KMClusterPop(Toplevel):
    def __init__(self, imgDB, master=None):


        self.imgDB = imgDB
        self.imgDB_names = list(imgDB.keys())
        # using toplevel to create a new window that isn't app
        Toplevel.__init__(self, master)
        # configuring the pop up window
        self.title("K-means clustering")
        self.geometry('400x600')

        #CONFIGURING GRID GEOMETRY OF WINDOW
        self.columnconfigure(0, weight=1)

        #LABEL at the top of the textfield
        self.label_sel_img= Label(self, text="Select image:", font="lucida 14 underline")
        self.label_sel_img.grid(column=0, row=0, pady=(15, 5))

        #OPTION MENU
        self.iM_var = StringVar()
        self.imageMenu= OptionMenu(self, self.iM_var, *self.imgDB_names)
        self.imageMenu.grid(column=0, row=1, sticky=N, padx=10, pady=5)

        #CONFIRM SELECTION
        self.confirm_bt = Button(self, text='Confirm Selection', command=self.get_sel_img)
        self.confirm_bt.grid(column=0,row=2, pady=(5,0))

        #ENTRY WIDGET
        self.input_widget = Entry(self)
        self.input_widget.grid(column=0,row=4, pady=20)

        # add text inside the box of the input field
        self.placeholder = "Enter number of clusters" #Used as instruction text for entry widget
        self.add() #Display instruction text inside the box
        self.input_widget.bind('<FocusIn>',self.erase) #Used to remove the text when clicked
        self.input_widget.bind('<FocusOut>',self.add)


        #PREVIEW BUTTON
        self.buttonPreview = ttk.Button(self,text='Preview', command = self.preview)
        self.buttonPreview.grid(column=0, row=5, sticky=S, padx=10, pady=10)
        #SUBMISSION BUTTON to display clustered img
        self.buttonSubmit = ttk.Button(self, text="Submit", command=self.display_clustered_img)
        self.buttonSubmit.grid(column=0, row=6, sticky=S, padx=10, pady=10)


    def get_sel_img(self):
        self.selected_img = self.imgDB[self.iM_var.get()]

    def check_input(self): #Used to check if the user puts correct input
        self.chosen_cluster_n = self.input_widget.get()
        self.chosen_cluster_n = self.chosen_cluster_n.replace(" ", "")
        if self.chosen_cluster_n =='':
            return 0
        elif self.chosen_cluster_n.isdecimal():
            self.n_cluster_int=int(self.chosen_cluster_n)
            if self.n_cluster_int >= 20: self.n_cluster_int = 20 #Maximum limit: 20 clusters
            return 1
        else:
            return 0

    def display_clustered_img(self):
        if self.check_input():
            self.clustered_img = ImageKMCluster(self.selected_img, self.n_cluster_int)
            self.clustered_img.display()
            self.imgDB[self.clustered_img.name] = self.clustered_img
            self.destroy()

    def is_imgPCA(self):
        if type(self.selected_img) is ImagePCA:
            return True

    def erase(self,event=None): #Used to erase placeholder text when clicked on the entry
        if self.input_widget.get() == self.placeholder:
            self.input_widget.delete(0,'end')
    def add(self,event=None): #Used to add placeholder text when main window is displayed
        if self.input_widget.get() == '':
            self.input_widget.insert(0,self.placeholder)

    def preview(self):
        '''
        Purpose: To display non-interactive image in the tkinter window, without any navigation tools
        '''
        if self.check_input():
            f = Figure()
            a = f.add_subplot(111)
            a.axis('off')
            self.canvas_preview = FigureCanvasTkAgg(f, self) #Used to create a canvas for preview image

            clustered_img = ImageKMCluster(self.selected_img, self.n_cluster_int)
            img_to_show = clustered_img.return_r_data()#reconstructed datapoints
            a.imshow(img_to_show)

            self.canvas_preview.draw()
            self.canvas_preview.get_tk_widget().grid(column=1, row=3,columnspan=2, rowspan=6, sticky='EW')
            self.canvas_preview.get_tk_widget().configure(bg="grey")
            self.resize()

    def resize(self): #Resize when preview is displayed 
        w = 1000
        h = 600
        self.geometry(f"{w}x{h}")
