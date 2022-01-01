# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 11:33:15 2021

@author: FM
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
        
# =============================================================================
#     def addImagePCA(self, currentFile):
#         """Adds image to ImageDB"""
#         self.InputDB.addImagePCA(currentFile)
#         
# =============================================================================
    def plotImage(self, index):
        """plots image of specified index in database in window"""
        self.InputDB.plotImage(index)

        

mat = mat73.loadmat('./tissue_t3_1_workspace.mat')
data = mat["map_t3"]
drawing = drawing()
drawing.addImageMean(data)
drawing.plotImage(0)
