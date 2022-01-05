from tkinter import *
from tkinter import filedialog
import os
import tkinter
#from tkinter import font

from tkinter import filedialog as fd
from tkinter.messagebox import showinfo

class ft_instructions(Toplevel): #Create a window
    def __init__(self, master=None):
        #using toplevel to create a new window that isn't root
        Toplevel.__init__(self, master)
        #configuring the pop up window
        self.title("How to Navigate Visualizer")
        self.geometry('460x600')

        # The following set up with frame and canvas is to enable coding of a scrollbar

        # Create Frame
        self.main_frame = Frame(self)
        # expands frames to the size of container
        self.main_frame.pack(fill=BOTH, expand=1)

        # Create a Canvas
        self.scroll_canvas = Canvas(self.main_frame)
        self.scroll_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        # Add A Scrollbar to the Canvas
        self.scrollbar = Scrollbar(self.main_frame, orient=VERTICAL, command=self.scroll_canvas.yview)
        # we have positioned this on the frame but have attached it to the canvas
        self.scrollbar.pack(side=RIGHT, fill=Y)

        # Configure the Canvas
        self.scroll_canvas.configure(yscrollcommand=self.scrollbar.set)
        # lambda e -> we are passing an event eg. mouse clicking
        self.scroll_canvas.bind('<Configure>', lambda e: self.scroll_canvas.configure(scrollregion=self.scroll_canvas.bbox("all")))

        # Create ANOTHER Frame INSIDE the Canvas
        self.second_frame = Frame(self.scroll_canvas)

        # Add that New frame to a Window in the Canvas
        self.scroll_canvas.create_window((0, 0), window=self.second_frame, anchor="nw")

        # Title at the top of the Window
        self.welcome_label = Label(self.second_frame, text="Welcome to Visualize!",
                                   font="lucida 16 bold")
        self.welcome_label.pack(pady=(15,0))

        # Instructions

        # STEP 1
        self.step1_label = Label(self.second_frame, text="Step(1): Click on the button on the top and select the file or files \n you would like to analyse",
                                 font="lucida 14")
        self.step1_label.pack(pady=(20,5), padx=5, side= TOP, anchor="w")
        self.step1_note_label = Label(self.second_frame, text="Note - The program only accepts .mat files",
                                 font="lucida 14 underline")
        self.step1_note_label.pack(padx=5)
        # STEP 2
        self.step2_label = Label(self.second_frame, text="Step(2): Click on the dropdown menu at the bottom to select the \n method you'd like to employ to visualize the data",
                                 font="lucida 14")
        self.step2_label.pack(pady=10, side= TOP, anchor="w", padx=5)
        self.step2_note_text = Label(self.second_frame,
                                 text="Note: The options available are Mean or \n PCA (Principal Component Analysis)",
                                 font="lucida 14 underline").pack(expand=True, fill=BOTH, padx=5)
        # IF PCA SELECTED
        self.pca_lf = LabelFrame(self.second_frame, text="If PCA is selected", font="lucida 14 bold", bg="Light Grey",
                                 height="100", pady=5, padx=5)
        self.pca_lf.pack(fill="both", expand="yes", padx=10, pady=10)

        self.pca_lf_1 = Label(self.pca_lf, text="When PCA is selected, a new PCA settings window will pop up.",
                              bg="Light Grey").pack(side= TOP, anchor="w")
        self.pca_lf_2 = Label(self.pca_lf, text="There are 2 main options available: ",
                              bg="Light Grey", font="lucida 13 bold").pack(side= TOP, anchor="w", pady=(1,8))
        self.pca_lf_3 = Label(self.pca_lf, text="(1) You may choose to plot data based on PCs calculated from \n a previous data set.",
                              bg="Light Grey", font="lucida 13 underline").pack(side=TOP, anchor="w")
        self.pca_lf_4 = Label(self.pca_lf, text="This option requires you to have already used the program to \n analyse a data set using PCA.",
                              bg="Light Grey").pack(expand=True, fill=BOTH, side=TOP, anchor="w")
        self.pca_lf_5 = Label(self.pca_lf, text="(2) You can plot based on PCs calculated on the current data set.",
                              bg="Light Grey", font="lucida 13 underline").pack(side=TOP, anchor="w", pady=(10,5))
        self.pca_lf_6 = Label(self.pca_lf, text="Using the checkbox you can select the number of PCs you'd like \n to use for plotting.",
                              bg="Light Grey", font="lucida 13").pack(side=TOP, anchor="w")
        self.pca_lf_7 = Label(self.pca_lf, text="To aid you in making this decision, there is a preview box on the \n right, here "
                                                "you can see what the image will look like with \n the PCs chosen.",
                          bg="Light Grey", font="lucida 13").pack(side=TOP, anchor="w")
        self.pca_lf_8 = Label(self.pca_lf, text="Once you have finalized your selection, click Submit.",
                              bg="Light Grey", font="lucida 13 underline").pack(side=TOP, anchor="w")

        # AFTER METHOD IS CHOSEN
        self.step3_label = Label(self.second_frame, text="Step(3): Navigate the Interactive Image Plot",
                                 font="lucida 14").pack(side=TOP, anchor="w", padx=5, pady=(0,10))
        self.step3_opts1_label = Label(self.second_frame, text="The interactive image will appear in a new window.",
                                      font="lucida 14").pack(side=TOP, anchor="w", padx=5)
        self.step3_opts2_label = Label(self.second_frame, text="At the top bar of the window, you can explore different "
                                                              "tools such \nas zoom.",
                                       font="lucida 14", justify=LEFT).pack(side=TOP, anchor="w", padx=5)
        self.step3_opts3_label = Label(self.second_frame, text="The image is also mouse-click sensitive, by clicking "
                                                               "on a pixel you \ncan have the raw raman spectrum "
                                                               "for that (x,y) co-ordinate \nappear in a new window.",
                                       font="lucida 14", justify=LEFT).pack(side=TOP,anchor="w", padx=5)

        #Goodbye Message

        self.ty_label = Label(self.second_frame, text="We hope you enjoy using Visualize!",
                              font="lucida 14 bold").pack(side=TOP, padx=5, pady=10)





# FOR TESTING

def openInstructions():
    a = ft_instructions(master=app)

app = Tk()
app.geometry("400x400")
b2 = Button(app, text="Open Instructions", command=openInstructions)
b2.pack()
app.mainloop()