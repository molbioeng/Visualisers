"""
Created on Wed Dec 22 17:48 2021
@author: pg
This is a database of all of the Principal components saved
"""
from PrincipalComponent import PrincipalComponent

class PrincipalComponentDB(object):
    """PCs database"""

    #Constructor
    def __init__(self):
        self.principalComponents = {} #Dictionary of principal components
        # KEYS - names of the objects
        # VALUES - objects themselves
