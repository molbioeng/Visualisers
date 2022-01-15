"""

Globals file, prevents them from being initialised more than once, but can be used among different files

"""
from ArrayDB import ArrayDB

def init():
    global List #list of .mat files (file names) uploaded by the user
    List = []

    global File #file name selected by the user for analysis
    File = None

    global method #data reduction method selected by the user
    method = "Mean"
    
    global Data #selected MATLAB file data
    global arrdb 
    arrdb = ArrayDB()
    global Data
    global ErrorMessage #error popup window messages