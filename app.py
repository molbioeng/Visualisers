from tkinter import *
from tkinter import ttk
from controls_frame import controls_frame


class app(Tk):
    # Constructor
    def __init__(self):
        super().__init__()
        # configure the root window
        self.title('My Awesome App')
        self.geometry('300x100')

        # Creating grid layout on the root window
        self.columnconfigure(0, weight=4)
        self.columnconfigure(1, weight=1)
