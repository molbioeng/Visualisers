# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 12:03:29 2021

@author: thefr

Updated on Sun Jan 2 13:01 2022
@author: pg

Class for all of the Raman images reduced by mean
"""

from Image import Image
import numpy as np
import matplotlib.pyplot as plt
import os
import fileList as fL


class ImageMean(Image):
    def __init__(self, array):
        """Initiates + reduces the image in one step"""

        super().__init__(array)

        for j in range(np.shape(self.img)[0]):
            for i in range(np.shape(self.img)[1]):
                self.img[i][j] =  np.average(self.data[i][j][:])

        filename = (os.path.basename(fL.File)).rsplit(".", 1)[0]
        self.name = str(filename)+ '/' + str(fL.Array_name)+'/'+'mean'

    def __repr__(self):
        return self.name
