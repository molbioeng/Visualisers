from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from controls_frame import controls_frame


class App(Tk):
    # Constructor
    def __init__(self):
        super().__init__()
        # configure the root window
        self.title('Visualize')
        self.geometry('850x600')
        #self.iconbitmap('window_icon.ico')
