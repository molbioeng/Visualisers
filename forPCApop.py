

from tkinter import *
from tkinter import filedialog
import os
import tkinter
#from tkinter import font
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo


##########PG
import tkinter as tk
from tkinter import ttk
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt


##########PG
import mat73
from Image import Image
from PrincipalComponent import PrincipalComponent
import numpy as np
from ImagePCA import ImagePCA


class pcaPop(Toplevel): #Create a window
    def __init__(self, master=None):
        #using toplevel to create a new window that isn't root
        Toplevel.__init__(self, master)
        #configuring the pop up window
        self.title("PCA Settings")
        self.geometry('800x600')

        # CONFIGURING GRID GEOMETRY OF WINDOW
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=2)

        # TITLE ON WINDOW AND SUBMIT BUTTON
        #msg = 'PCA SETTINGS'
        #self.toplabel = Label(self, text=msg)
        #self.toplabel.grid(column=1,row=0,sticky=N, padx=10, pady=10)

        # self.button = Button(self, text="Submit", command=self.destroy)
        # self.button.grid(column=0,row=10, columnspan=3, sticky=S, padx=10, pady=10)

        buttonX = ttk.Button(self,text="Submit", command=self.destroy)
        buttonX.grid(column=0,row=10, columnspan=3, sticky=S, padx=10, pady=10)

        ### FOR TESTING SIMPLE IMAGE
        # f = Figure(figsize=(5,5),dpi=100)
        # a = f.add_subplot(111)
        # a.plot([1,2,3,4,5,6,7,8],[5,1,2,6,3,3,7,1])
        #
        # canvas = FigureCanvasTkAgg(f,self)
        # canvas.draw()
        # # canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True )
        # canvas.get_tk_widget().grid(column=0,row=11, columnspan=3, sticky=S, padx=10, pady=10)

        # DROP DOWN MENU - CODE FOR SELECTING OPTION AND CONFIRMING IT
        # variable that stores index for array of drop down options
        lst = [ 'phone','laptop','car','plane','digger']
        self.var = tk.StringVar()
        # self.var.set(app.lst[0])
        self.var.set(lst[0])

        # label for drop down menu
        drop_down_text = "If you would like to use PCs from a previous image please select:"
        self.dd_label = Label(self, text=drop_down_text, font="lucida 14")
        self.dd_label.grid(column=0, row=0, columnspan=2, sticky=N, padx=10, pady=(15,5))

        self.drop = OptionMenu(self, self.var, *lst)
        # self.drop = OptionMenu(self, self.var, *app.lst)
        self.drop.grid(column=0, row=1, columnspan=2, sticky=N, padx=10, pady=5)
        self.cfm_opt_btn = Button(self, text="Confirm Selection", command=lambda: print(self.var.get()))
        self.cfm_opt_btn.grid(column=2,row=1,sticky=N, pady=10, padx=10)

        # LINE TO SEPARATE MENU IN TWO SECTIONS
        self.canvas_line = Canvas(self, height=10, bd=0)
        self.canvas_line.grid(column=0, row=2, columnspan=3, sticky='EW')
        self.canvas_line.create_line(15, 5, 785, 5, dash=(8,3))

        # PC CHECK LIST CODE
        # label at the top of the check list
        self.cl_label = Label(self, text="Select PC to be included in the image:", font="lucida 14 underline")
        self.cl_label.grid(column=0, row=3, pady=(15,5))

        # variables to store on/off value of checkbox
        self.cl_var1 = IntVar()
        self.cl_var2 = IntVar()
        self.cl_var3 = IntVar()
        #
        # matFile = mat73.loadmat('tissue_t3_1_workspace.mat') # .mat file must be in the same local directory
        # my_data = np.array(matFile["map_t3"])
        # pca_t3 = PrincipalComponent(my_data)
        # image = ImagePCA(my_data,pca_t3)
        # f = Figure()
        # a = f.add_subplot(111)
        # a.axis('off')


        # checkboxes
        self.cb_1 = Checkbutton(self, text="PC 1", variable=self.cl_var1, command= lambda: self.displayxxx())
        self.cb_1.grid(column=0, row=4)

        self.cb_2 = Checkbutton(self, text="PC 2", variable=self.cl_var2, command= lambda: self.displayxxx())
        self.cb_2.grid(column=0, row=5)

        self.cb_3 = Checkbutton(self, text="PC 3", variable=self.cl_var3, command= lambda: self.displayxxx())
        self.cb_3.grid(column=0, row=6)


        # PREVIEW BOX
        #title
        self.pb_label = Label(self, text="Preview Image", font="lucida 13 bold")
        self.pb_label.grid(column=1, row=3, columnspan=2, sticky='N', pady=(15,0))

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


    def displayxxx(self):
        f = Figure(figsize=(5,5),dpi=100)
        a = f.add_subplot(111)
        self.canvas_preview2 = FigureCanvasTkAgg(f,self)
        if self.cl_var1.get()==1:
            print('Var1 is 1')
            # plt.cla()
            a.plot([1,2,3,4,5,6,7,8],[5,1,2,6,3,3,7,1])
            self.canvas_preview2.draw()
            self.canvas_preview2.get_tk_widget().grid(column=1,row=4, columnspan=2,rowspan=6, sticky='EW')
            self.canvas_preview2.get_tk_widget().configure(bg="grey")
        elif self.cl_var1.get()==0:
            print('Var1 is 0')
        if self.cl_var2.get()==1:
            print('Var2 is 1')
            # plt.cla()
            a.plot([1,2,3,4,5,6,7,8],[7,2,2,4,3,3,4,8])
            self.canvas_preview2.draw()
            self.canvas_preview2.get_tk_widget().grid(column=1,row=4, columnspan=2,rowspan=6, sticky='EW')
            self.canvas_preview2.get_tk_widget().configure(bg="grey")
        elif self.cl_var2.get()==0:
            print('Var2 is 0')
        if self.cl_var3.get() ==1:
            print('Var3 is 1')
            # plt.cla()
            a.plot([1,2,3,4,5,6,7,8],[9,1,2,2,5,1,6,8])
            self.canvas_preview2.draw()
            self.canvas_preview2.get_tk_widget().grid(column=1,row=4, columnspan=2,rowspan=6, sticky='EW')
            self.canvas_preview2.get_tk_widget().configure(bg="grey")
        elif self.cl_var3.get()==0:
            print('Var3 is 0')

        else:
            print('error')


# FOR TESTING
def openSettings():
    # a = pcaPop(master=app)
    a=pcaPop()

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
