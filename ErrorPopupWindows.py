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

import fileList as fL

class ErrorPopup():

    def __init__(self, master):
        window = tk.Toplevel(master)

        window.title("Warning")

        label = tk.Label(window, text = fL.ErrorMessage)
        label.pack(fill = 'x', padx=50, pady=5)

        button_close = tk.Button(window, text = "Close", command = window.destroy)
        button_close.pack(fill = 'x')
