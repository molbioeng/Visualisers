import tkinter as tk
import fileList as fL

class ErrorPopup(): #general error popup window

    def __init__(self, master):
        window = tk.Toplevel(master)

        window.title("Warning")

        #the global variable ErrorMessage contains the warning/error message
        #it is initialized for different errors every time the error popup is needed
        label = tk.Label(window, text = fL.ErrorMessage)
        label.pack(fill = 'x', padx=50, pady=5)

        button_close = tk.Button(window, text = "Close", command = window.destroy)
        button_close.pack(fill = 'x')