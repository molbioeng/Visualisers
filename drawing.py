# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 11:33:15 2021
@author: FM

Updated on Sun Jan 2 13:01 2022

"""

#Modules used

from ImageDB import ImageDB
import mat73



#In the actual program this will be passed to drawing in a different way
class drawing(object):
    def __init__(self):
        self.InputDB = ImageDB()

    def addImageMean(self, currentFile):
        """Adds image to ImageDB"""
        self.InputDB.addImageMean(currentFile)

    def addImagePCA(self, currentFile):
        """Adds image to ImageDB"""
        self.InputDB.addImagePCA(currentFile)

    def addImageKMCluster(self, currentFile):
        """Adds image to ImageKMClustering"""
        self.InputDB.addImageKMCluster(currentFile)

    def displayImage(self, index):
        """plots image of specified index in database in window"""
        self.InputDB.displayImage(index)
