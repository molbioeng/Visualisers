# Import the library tkinter
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os
import tkinter

# Create a GUI app
app = Tk()

# Give a title to your app
app.title("Volumetric Data")


# Constructing the first frame, frame1
frame1 = LabelFrame(app, text = "Select file", bg = "green", fg = "white", padx = 50, pady = 100)


# Displaying the frame1 in row 0 and column 0
frame1.grid(row=0, column=0)

#Openfile
frame1.filenames = filedialog.askopenfilenames(initialdir="/Users/Aron/Recents", title="Select a File",
                                           filetypes=(("PNG files", "*.png"), ("all files", '')))


################################################################################

#BUTTON 1 – FILENAME



def show():
    myLabel = Label(frame1, text=value_inside.get()).pack()

lst = list(frame1.filenames)


# Variable to keep track of the option
# selected in OptionMenu
value_inside = tkinter.StringVar(frame1)

# Set the default value of the variable
value_inside.set("Select an Option")

drop1 = OptionMenu(frame1, value_inside, *lst, command=show)
drop1.pack(side=RIGHT, anchor="ne")

btn1= Button(frame1, text = "Show Filename", command=show).pack()

################################################################################

# Constructing the second frame, frame2
frame2 = LabelFrame(app, text = "Select method", bg = "yellow", padx = 50, pady = 100)

# Displaying the frame2 in row 0 and column 1
frame2.grid(row=1, column=0)


#BUTTON 2 – METHODS (MEAN/PCA)

def show():
    myLabel = Label(frame2, text=var2.get()).pack()

options = [
    "Mean",
    "PCA"
]

var2 = StringVar()
var2.set(options[0])

drop2 = OptionMenu(frame2, var2, *options, command=show)
drop2.pack(side=RIGHT, anchor="ne")

btn2= Button(frame2, text="Show Method", command=show).pack()

################################################################################
# Constructing the third frame, frame3
frame3 = LabelFrame(app, text = "2D image", bg = "red", fg = "white", padx = 200, pady = 200)

# Displaying the frame3 in row 0 and column 0
frame3.grid(row=0, column=1, rowspan=2,  sticky='nsew')

 #Constructing the button b1 in frame1
b1 = Button(frame3, text="Apple")

# Displaying the button b1
b1.pack()

# Make the loop for displaying app
app.mainloop()
