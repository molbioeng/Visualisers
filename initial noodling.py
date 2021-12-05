# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import matplotlib.pyplot as plt
import mat73 

#mat = mat73.loadmat('.tissue_t3')

# =============================================================================
# #initialising array of random numbers
# arr = np.random.rand(4,5)
# arr2 = np.random.rand(10)
# 
# #Find average value in the array
# mean = np.average(arr)
# 
# #Plotting an array
# graph = plt.plot(arr2)
# plt.title("A plot")
# plt.show()
# 
# =============================================================================

### IN 2D ###
# =============================================================================
# def find_mean(array, row):
#     return np.average(array[row])
# 
# def plot_spectrum(array, row):
#     return plt.plot(array[row])
# 
# arr = [[1,2,3],[4,5,6],[7,8,9]]
# #arr = np.random.rand(50,70)
# r = 0
# m = find_mean(arr, r)
# plot_spectrum(arr, r)
# =============================================================================

# =============================================================================
# 
# ### IN 3D ###
# def find_mean(array, row, col):
#     return np.average(array[row][col])
# 
# def find_means(array, row, col_size):
#     l = [np.average(array[row][i][:]) for i in range(col_size)]
#     print(l)
#     return l
# 
# def plot_spectrum(array, row, col):
#     return plt.plot(array[row][col])
# 
# 
# #arr = np.random.rand(50,70,30)
# arr3 = [[[1,2,3],[4,5,6],[7,8,9]],
#         [[11,12,13],[14,15,16],[17,18,19]],
#         [[21,22,23],[24,25,26],[27,28,29]]]
# 
# arr1 = [1,2,3]
# arr2 = [[1,2,3],[4,5,6],[7,8,9]]
# 
# r = 0
# c = 2
# i = 0
# #m = find_mean(arr3, r, c)
# #a = find_means(arr3, r, 3)
# plot_spectrum(arr3, r, c)
# plt.title("Spectrum from 3D")
# plt.show()
# 
# =============================================================================

# =============================================================================
# ### Now trying to display an array as an image ###
# arr = np.random.rand(50,70)
# imgplot = plt.imshow(arr)
# 
# =============================================================================

###Let's load the .mat file

def reduce_img(data, x_size, y_size):
    img = np.empty([x_size, y_size])
    for j in range(x_size):
        for i in range(y_size):
            img[i][j] =  np.average(data[i][j][:])
    print(img)
    return img

#mat = mat73.loadmat('./tissue_t3_1_workspace.mat')
#data = mat["map_t3"]
#lis = reduce_img(data, 200, 200) #dont hardcode in the future!!
    
mean = np.mean(lis)
sd = np.std(lis, axis = None) 

fig, ax = plt.subplots()
im = ax.imshow(lis, interpolation='nearest', vmin=mean-(2*sd), vmax=mean+(sd))
fig.colorbar(im)
plt.show()

#array = np.random.rand(200,200,1024)
#size = array.shape
#img = reduce_img(array, size[0], size[1])
#imgplot = plt.imshow(img)

