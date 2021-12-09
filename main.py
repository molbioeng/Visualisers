from tkinter import *
from app import app
from controls_frame import controls_frame
from img_canvas import img_canvas

if __name__ == "__main__":
    App = app()
    frame = controls_frame(App)
    frame2 = img_canvas(App)
    App.mainloop()