import tkinter as tk
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter import filedialog

class controls_frame(Frame):
    # Constructor
    def __init__(self, container):
        super().__init__(container, bg='red')
        # setting the grid layout of the frame
        #self.columnconfigure(0, weight=1)
        #self.columnconfigure(0, weight=4)
        self.configure(borderwidth=5)

        # load file dialog box
        '''
        self.filename = filedialog.askopenfilename(initialdir="/Users/Aron", title="Select a File",
                                                    filetypes=(("PNG files", "*.png"), ("all files", '')))
        '''

        # label
        self.label = Label(self, text='Hello, Tkinter!')
        self.label.pack()

        # button
        self.button = Button(self, text='Click Me')
        self.button['command'] = self.button_clicked
        self.button.pack()

        #Drop Down Files

        options = [
            "Monday",
            "Tuesday",
            "Friday"
        ]

        var = StringVar()
        var.set(options[0])

        self.drop = OptionMenu(self, var, *options, command=self.show)
        self.drop.pack()

        # packing the frame onto container - app
        self.pack(side='left', fill='both', expand=1)

    def button_clicked(self):
        showinfo(title='Information', message='Hello, Tkinter!')

    def show(self, var):
        self.label2 = Label(self, text=var).grid(row=4, column=0)

