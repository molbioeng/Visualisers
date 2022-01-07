from tkinter import *
from tkinter import filedialog
import os
import tkinter
#from tkinter import font

from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

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
        self.button = Button(self, text="Submit", command=self.destroy)
        self.button.grid(column=0,row=10, columnspan=3, sticky=S, padx=10, pady=10)

        # DROP DOWN MENU - CODE FOR SELECTING OPTION AND CONFIRMING IT
        # variable that stores index for array of drop down options
        self.var = StringVar()
        self.var.set(app.lst[0])

        # label for drop down menu
        drop_down_text = "If you would like to use PCs from a previous image please select:"
        self.dd_label = Label(self, text=drop_down_text, font="lucida 14")
        self.dd_label.grid(column=0, row=0, columnspan=2, sticky=N, padx=10, pady=(15,5))

        self.drop = OptionMenu(self, self.var, *app.lst)
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
        cl_var1 = IntVar()
        cl_var2 = IntVar()
        cl_var3 = IntVar()

        # checkboxes
        self.cb_1 = Checkbutton(self, text="PC 1", variable=cl_var1)
        self.cb_1.grid(column=0, row=4)

        self.cb_2 = Checkbutton(self, text="PC 2", variable=cl_var2)
        self.cb_2.grid(column=0, row=5)

        self.cb_3 = Checkbutton(self, text="PC 3", variable=cl_var3)
        self.cb_3.grid(column=0, row=6)

        # PREVIEW BOX
        #title
        self.pb_label = Label(self, text="Preview Image", font="lucida 13 bold")
        self.pb_label.grid(column=1, row=3, columnspan=2, sticky='N', pady=(15,0))

        # setting up canvas
        self.canvas_preview = Canvas(self, height=400, bd=0, bg='Grey')
        self.canvas_preview.grid(column=1, row=4, columnspan=2, rowspan=6, sticky='EW')

        # PREVIEW BOX CODE




# FOR TESTING

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

