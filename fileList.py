"""

Globals file, prevents them from being initialised more than once, but can be used among different files

"""
def init():
    global List #list of .mat files (file names) uploaded by the user
    List = []

    global File #file name selected by the user for analysis
    File = None

    global method #data reduction method selected by the user
    method = "Mean"

    global Data #selected MATLAB file data
    global Array #3D array (data) selected by the user
    global Array_name #name of 3D array selected by the user

    global ErrorMessage #error popup window messages