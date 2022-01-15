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

class Image(ABC):

    def __init__(self, array):
        #data passed into the image
        self.name = array[0]
        self.data = array[1]
        

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
