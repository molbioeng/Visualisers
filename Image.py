# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 12:02:45 2021

@author: FM

Image class - abstract class for reduced Raman images
"""

from abc import ABC
import numpy as np
import matplotlib.pyplot as plt
from plotInteract import PlotInteract
import os
import fileList as fL

class Image(ABC):

    def __init__(self, array):
        self.data = array #data passed into the image
        self.img = np.empty(shape=(np.shape(array)[0:2])) #Flattened Raman data
        filename = (os.path.basename(fL.File)).rsplit(".", 1)[0]
        self.name = str(filename)+ '/' + str(fL.Array_name)

    def __repr__(self):
        """Used later in calling the class by its name"""
        return self.name

    def display(self):
        """Module allows for plot interaction"""
        #Create the figure and plot
        fig, ax = plt.subplots()
        fig.suptitle(self.name)
        plt.imshow(self.img)
        plt.colorbar()

        #Plot interaction and connect to event manager
        show = PlotInteract(ax, self.data)
        show.connect()
        plt.show()
