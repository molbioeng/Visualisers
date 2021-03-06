from ImageDB import ImageDB
from ArrayDB import ArrayDB
import fileList as fL
from ErrorPopupWindows import ErrorPopup
from PrincipalComponentDB import PrincipalComponentDB
from pcaPop import pcaPop
from KMClusterPop import KMClusterPop
from ImageMean import ImageMean
from ImageViewerPop import *


# FRAME 3 - PLOTTING

"""
The final frame on the main app window. Allows user to display an interactive image, generated based on selections made
in previous frames, as well as from pop up setting windows. Each image displayed is stored in the
image database (ImageDB).

The frame contains a button that opens a window where the user can view all images contained in the image database.
"""


class filenamewindow3(LabelFrame):
    #Constructor
    def __init__(self, container, controller):
        super().__init__(container)
        self.frame3 = LabelFrame(container, text = "2D image", bg = "white", padx=120, pady=50, width=300)
        self.frame3.grid(row=4, column=0, sticky="nsew")

        # configuration of grid on frame
        self.frame3.grid_columnconfigure(0, weight=1)
        self.frame3.grid_columnconfigure(1, weight=1)


        self.b1 = Button(self.frame3, text="Show Image", command=self.show_plot).grid(column=0, row=0, columnspan=2)

        # Setting up arrays
        self.imgdb = ImageDB()

        self.pcdb = PrincipalComponentDB().principalComponents

        self.b2 = Button(self.frame3, text="Show All Images", command=self.open_img_viewer).grid(column=0, row=1, columnspan=2)


    def open_img_viewer(self):
        """ If the user has already produced images using the program, it will open the image viewer
            pop up window.
        """
        if not self.imgdb.images:
            fL.ErrorMessage = "No images have been produced yet."
            self.popup_window() # Error pop up
        else:
            self.img_viewer_pop = imgviewPop(self.imgdb.images)


    def popup_window(self):
        ErrorPopup(self.frame3)


    def show_plot(self):
        """ Plots based on selections made by user in previous frames. Accordingly, it will
         create settings pop up windows.
        """
        if fL.arrdb.current_array:
            array = (fL.arrdb.current_array, fL.arrdb.arrays[fL.arrdb.current_array])
            if fL.method == "Mean":
                img_mean = ImageMean(array)
                self.imgdb.addImage(img_mean)
                self.imgdb.displayImage(img_mean)

            elif fL.method == "PCA":
                self.pcaPop = pcaPop(self.pcdb, array,draw=self.imgdb)

            elif fL.method == "K-Means Clustering":
                if bool(self.imgdb.images):
                    self.KMClusterPop = KMClusterPop(self.imgdb.images)
                else:
                    fL.ErrorMessage = "No images in memory. \n Please apply reduction method before KM-Clustering."
                    self.popup_window()
                    #To display erroPopup window if there is no image class which user can apply KMClustering method to
        else:
            fL.ErrorMessage = "Please select a 3D array and method of analysis."
            self.popup_window()
