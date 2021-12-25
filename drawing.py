# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 11:33:15 2021

@author: thefr
"""

#Modules used

from ImageDB import ImageDB



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

        

