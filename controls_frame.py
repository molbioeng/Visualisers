import tkinter as tk
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter import filedialog

class controls_frame(Frame):
    # Constructor
    def __init__(self, container):
        super().__init__(container)
        # setting the grid layout of the frame
        self.columnconfigure(0, weight=1)
        self.columnconfigure(0, weight=3)
        self.configure(borderwidth=5)

        # load file dialog box
        self.filename = filedialog.askopenfilename(initialdir="/Users/Aron", title="Select a File",
                                                    filetypes=(("PNG files", "*.png"), ("all files", '')))

        # label
        self.label = Label(self, text='Hello, Tkinter!')
        self.label.grid(row=0, column=0)

        # button
        self.button = Button(self, text='Click Me')
        self.button['command'] = self.button_clicked
        self.button.grid(row=1, column=0)

        # packing the frame onto container - app
        self.grid(column=0, row=0)

    def button_clicked(self):
        showinfo(title='Information', message='Hello, Tkinter!')

