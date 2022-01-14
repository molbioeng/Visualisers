import tkinter as tk
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
#from tkinter.messagebox import showinfo
import requests

import mat73
import scipy
import scipy.io as sio
import numpy as np


class ArraySelectionPopup():

    def __init__(self, master):
        window = tk.Toplevel(master)

        window.title("Warning")

        label = tk.Label(window, text = "Please open a MATLAB file and confirm your selection.")
        label.pack(fill = 'x', padx=50, pady=5)

        button_close = tk.Button(window, text = "Close", command = window.destroy)
        button_close.pack(fill = 'x')

class FileSelectionPopup():

    def __init__(self, master):
        window = tk.Toplevel(master)

        window.title("Warning")

        label = tk.Label(window, text = "Please open a MATLAB file.")
        label.pack(fill = 'x', padx=50, pady=5)

        button_close = tk.Button(window, text = "Close", command = window.destroy)
        button_close.pack(fill = 'x')

class ImagePopup():

    def __init__(self, master):
        window = tk.Toplevel(master)

        window.title("Warning")

        label = tk.Label(window, text = "Please open a MATLAB file, select an array, and choose an analysis method.")
        label.pack(fill = 'x', pady=5)

        button_close = tk.Button(window, text = "Close", command = window.destroy)
        button_close.pack(fill = 'x')

class NoImageForKMCPopup():

    def __init__(self,master):
        window = tk.Toplevel(master)
        window.title("Warning")

        label = tk.Label(window,text="No images in memory.\nPlease apply reduction method before KM-Clustering.")
        label.pack(fill='x', padx=50,pady=10)

        button_close = tk.Button(window,text='Close',command=window.destroy)
        button_close.pack()
