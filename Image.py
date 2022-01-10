# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 12:02:45 2021

@author: thefr

Image class - abstract class for reduced Raman images
"""

from abc import ABC, abstractmethod
import numpy as np
import matplotlib.pyplot as plt
from plotInteract import PlotInteract
import fileList as fL
import os

class Image(ABC):

    def __init__(self, array):
        self.data = array #data passed into the image
        self.img = np.empty(shape=(np.shape(array)[0:2])) #Flattened Raman data
        
        filename = (os.path.basename(fL.File)).rsplit(".", 1)[0]
        self.name = str(filename)+ '/' + str(fL.Array_name)

    def __repr__(self):
        return self.name

    def display(self):
        """Module allows for plot interaction"""

        #for img in self.img:
        fig, ax = plt.subplots()
        imgplt = plt.imshow(self.img)
        plt.colorbar()
        plt.title(self.name)

        #Plot interaction and connect to event manager
        show = PlotInteract(ax, self.data, self.name)
        show.connect()
        plt.show()


