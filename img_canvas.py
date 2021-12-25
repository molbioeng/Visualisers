from tkinter import *
from tkinter.messagebox import showinfo

class img_canvas(Canvas):
    # Constructor
    def __init__(self, container):
        super().__init__(container)
        # defining grid layout
        self.columnconfigure(0, weight=1)
        self.columnconfigure(0, weight=3)
        self.configure(borderwidth=5)

        # label
        self.label = Label(self, text='Hello, Tkinter!')
        self.label.grid(row=0, column=0)

        # button
        self.button = Button(self, text='Click Me')
        self.button['command'] = self.button_clicked
        self.button.grid(row=1, column=0)

        # pack it onto container
        self.pack(side='right', fill='both', expand=1)

    def button_clicked(self):
        showinfo(title='Information', message='Hello, Tkinter!')