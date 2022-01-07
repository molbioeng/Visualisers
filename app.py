from tkinter import *
from tkinter import ttk
from controls_frame import controls_frame


class App(Tk):
    # Constructor
    def __init__(self):
        super().__init__()
        # configure the root window
        self.title('Visualizer')
        self.geometry('500x500')
