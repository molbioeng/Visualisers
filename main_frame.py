from tkinter import *

"""
Frame designed to enable integration of a vertical scrollbar on main app window, as well as configuring a
grid that can be used to plot other frames onto the main app window.
"""

class main_frame(Frame):
    def __init__(self, container):
        super().__init__(container)

        # Create a Canvas
        self.scroll_canvas = Canvas(self)
        self.scroll_canvas.pack(side=LEFT, fill=BOTH, expand=1)

        # Add A Scrollbar to the Canvas
        self.scrollbar = Scrollbar(self, orient=VERTICAL, command=self.scroll_canvas.yview)
        # we have positioned this on the frame but have attached it to the canvas
        self.scrollbar.pack(side=RIGHT, fill=Y)

        # Configure the Canvas
        self.scroll_canvas.configure(yscrollcommand=self.scrollbar.set)
        # lambda e -> we are passing an event
        self.scroll_canvas.bind('<Configure>', lambda e: self.scroll_canvas.configure(scrollregion=self.scroll_canvas.bbox("all")))

        # Create ANOTHER Frame INSIDE the Canvas
        self.second_frame = Frame(self.scroll_canvas)
        # Configuration of grid on second_frame
        self.second_frame.grid_columnconfigure(0, weight=1)

        # Add that second_frame to a Window in the Canvas
        self.scroll_canvas.create_window((0, 0), window=self.second_frame, anchor="nw")

        # Expands frames to the size of container
        self.pack(fill=BOTH, expand=1)

        # Add Logo at the top of second_frame
        self.logo = PhotoImage(file='logo.png')
        self.logo_lb = Label(self.second_frame, image=self.logo).grid(row=0, column=0, columnspan=2, sticky="nsew")
