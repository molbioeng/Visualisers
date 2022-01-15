# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 11:54:13 2021

@author: FM

Updated on Sun Jan 2 13:01 2022
@author: pg

This is a database of all of the Images saved
"""

class ImageDB(object):
    """ Image database used to store plots that the user has created, and may 
    want to access again."""

    def __init__(self):
        self.images = {} #List of Images, used a dict so images could be accessed by name

    def addImage(self, currentImg):
        """Creates and adds an image to the database"""
        self.images[currentImg.name] = currentImg

    def displayImage(self, img):
        """Displays image"""
        self.images[img.name].display()
