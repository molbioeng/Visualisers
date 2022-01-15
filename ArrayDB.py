# -*- coding: utf-8 -*-
"""
Stores the arrays that the user is working on (multiple images can be made from
one array)

@author: FM
"""

class ArrayDB(object):
    """ Array database used to store arrays that the user has previously selected, 
    and may want to access again."""

    def __init__(self):
        self.arrays = {} #List of Images, used a dict so images could be accessed by name
        self.current_array = None

    def addArray(self, currentArray, arrayName):
        """Creates and adds an Array to the database"""
        self.arrays[arrayName] = currentArray
        print("Current arrays in arrayDB:")
        print(self.arrays.keys())
