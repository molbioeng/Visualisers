"""
Created on Tue Dec  14 17:31 2021
@author: pg

Program for handling mouse events
Goals:

- the user has a main image (in our case, the raman image displayed after applying data reduction methods)
- the user wants to click on the specific part of the image and display the raman spectrum of the corresponding pixel.
- the mouse event would extract a 1D array representing a single raman spectrum from the original dataset.
- the mouse event would trigger plotting the extracted data on the figure.

"""
import cv2
import numpy as np
import mat73
import matplotlib.pyplot as plt

matFile = mat73.loadmat('tissue_t3_1_workspace.mat')
image = matFile["m"] #For the purpose of testing the function, the spectra come from different source, they are not coming from 'm' image
data = matFile['map_t3']

def printCoordinate(event,x,y,flags,params): # MOUSE CALL BACK FUNCTION, IT SHOULD TAKE 4 FOLLOWING PARAMETERS
    if event==cv2.EVENT_LBUTTONDOWN:
        strXY = '('+str(x)+','+str(y)+')'
        print(strXY) # prints x,y coordinates to terminal
        spectrum = data[x][y][:]
        title = 'spectrum of the pixel {}x{}'.format(x,y)
        plt.ion() # enables interactive mode - plots spectra on the same grap
        plt.plot(spectrum)
        plt.title(title)
        plt.show()

cv2.imshow('Image',image)

# Whenever a mouse even occurs we have to call the function:
cv2.setMouseCallback('Image', printCoordinate) #Take 2 parameters:
# - the window name on which look for the mouse event to occur,
# - the function to be called whenever the mouse event occurs

cv2.waitKey() # close the image whenever any key is pressed
cv2.destroyAllWindows()
