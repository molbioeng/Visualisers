# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 12:02:45 2021

@author: thefr

Image class - abstract class for reduced Raman images
"""

from abc import ABC, abstractmethod 
import numpy as np

class Image(ABC):
    
    def __init__(self, array):
        self.data = array #data passed into the image
        self.img = np.empty(shape=(np.shape(array)[0:2])) #Flattened Raman data



    
   
    
