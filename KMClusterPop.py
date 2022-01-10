'''
This class will be used to display window for KMClustering
Created 9 Jan 2022
author: pg

'''

from tkinter import *
from tkinter import ttk
import os
from ImageKMCluster import ImageKMCluster
from ImagePCA import ImagePCA

class KMClusterPop(Toplevel):
    def __init__(self, imgDB, master=None):

        self.imgDB = imgDB
        self.imgDB_names = list(imgDB.keys())
        # using toplevel to create a new window that isn't root
        Toplevel.__init__(self, master)
        # configuring the pop up window
        self.title("K-means clustering")
        self.geometry('400x600')

        # CONFIGURING GRID GEOMETRY OF WINDOW
        self.columnconfigure(0, weight=1)
        # self.columnconfigure(1, weclight=1)
        # self.columnconfigure(2, weight=2)


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


        #LABEL at the top of the PC list
        self.label_sel_pc = Label(self, text="Select PC for which you want to cluster the image:", font="lucida 14 underline")
        self.label_sel_pc.grid(column=0, row=3, pady=(15, 5))


        # variables to store on/off value of radiobutton
        self.rb_var = IntVar()

        #RADIOBUTTONS
        self.rb_1 = Radiobutton(self, text="Image from PC1", variable=self.rb_var, value=0, command=lambda: self.get_pca_dataset(self.rb_var.get()))
        self.rb_1.grid(column=0, row=4)

        self.rb_2 = Radiobutton(self, text="Image from PC2", variable=self.rb_var, value=1, command=lambda: self.get_pca_dataset(self.rb_var.get()))
        self.rb_2.grid(column=0, row=5)

        self.rb_3 = Radiobutton(self, text="Image from PC3", variable=self.rb_var, value=2, command=lambda: self.get_pca_dataset(self.rb_var.get()))
        self.rb_3.grid(column=0, row=6)

        #ENTRY WIDGET
        self.input_widget = Entry(self)
        self.input_widget.grid(column=0,row=7, pady=20)
        # self.input_widget.delete()

        # add text inside the box of the input field
        self.input_widget.insert(0,"Enter number of clusters: ")


        #SUBMISSION BUTTON to display clustered img
        self.buttonSubmit = ttk.Button(self, text="Submit", command=self.display_clustered_img)
        self.buttonSubmit.grid(column=0, row=8, columnspan=2, sticky=S, padx=10, pady=10)
        
        # Label to confirm selected file 
        #self.label = Label(self.frame1, text=tkinter.String())
        #self.label.grid(column=0, row=2, columnspan=2)

    def get_sel_img(self):
        self.selected_img = self.imgDB[self.iM_var.get()]
        #self.label['text'] = "Selected image is: " + str(self.selected_img)
        print('This is selected img: '+str(self.selected_img))

    def display_clustered_img(self):
        self.chosen_cluster_n = self.input_widget.get()
        if self.chosen_cluster_n =='':
            print('nothing there')
        elif self.chosen_cluster_n.isdecimal():
            print('it is a number')
            n_cluster_int=int(self.chosen_cluster_n)
            #self.clustered_img = ImageKMCluster(data=self.selected_img.data, array=self.selected_img.img,n_clusters=n_cluster_int)
            self.clustered_img = ImageKMCluster(self.selected_img, n_cluster_int)
            self.clustered_img.display()
            self.destroy()

        else:
            print('not number')

    def is_imgPCA(self):
        if type(self.selected_img) is ImagePCA:
            return True

    def get_pca_dataset(self, rb_var):
        if self.is_imgPCA():
            if rb_var==0:
                self.selected_img.return_Image(0)
                print('selected image from PC1')
            elif rb_var==1:
                self.selected_img.return_Image(1)
                print('selected image from PC2')
            elif rb_var==2:
                self.selected_img.return_Image(2)
                print('selected image from PC3')
        else:
            print('Dataset from PCA is not passed')




##### AFTER PCApopup --> display at the same as interactive plot
        # window for pca graphs
        # window that has checkbutton
        # - Scree plot
        # - Loading plots
        # submit
        # display selected graphs
