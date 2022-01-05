from tkinter import *
from newuser_instructions import *

class newuser_pop(Toplevel): #Create a window
    def __init__(self, master=None):
        #using toplevel to create a new window that isn't root
        Toplevel.__init__(self, master)
        self.title("Welcome")
        self.geometry('300x120')

        # CONFIGURING GRID GEOMETRY OF WINDOW
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

        self.label = Label(self, text="Would you like to see instructions \non how to navigate the program?")
        self.label.grid(column=0, columnspan=2, padx=10, pady=10)

        # NO BUTTON
        self.no_btn = Button(self, text="No", command=self.destroy)
        self.no_btn.grid(column=0, row=1, padx=10, pady=10)

        # YES BUTTON
        self.yes_btn = Button(self, text="Yes", command=self.openInstructions)
        self.yes_btn.grid(column=1, row=1, padx=10, pady=10)

    def openInstructions(self):
        b = ft_instructions()
        self.destroy()


# FOR TESTING

#app = Tk()
#app.geometry("400x400")
#a = newuser_pop(master=app)
#a.wm_attributes("-topmost", 1)
#app.mainloop()