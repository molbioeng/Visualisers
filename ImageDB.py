# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 11:54:13 2021

@author: thefr

This is a database of all of the Images saved 
"""


#Modules used
from ImageMean import ImageMean
#from ImagePCA import ImagePCA


class ImageDB(object):
    """ Image database""" 
    
    #Constructor
    def __init__(self):
        self.images = [] #List of Images
    
    def addImageMean(self, currentFile):
        """Creates and adds an image to the database"""
        self.images.append(ImageMean(currentFile))
        
# =============================================================================
#     def addImagePCA(self, currentFile):
#         """Creates and adds an image to the database"""
#         self.images.append(ImagePCA(currentFile))
# =============================================================================
    
    def plotImage(self, index):
        """Plots image"""
        self.images[index].plot()

        