# -*- coding: utf-8 -*-
"""
This a file used for unit testing

@author: FM

"""
import unittest
from ImageMean import ImageMean
import numpy as np
import matplotlib.pyplot as plt
import mat73
import scipy.io as sio
import fileList as fL
import os
file_list = fL
file_list.File = "Booboo"
file_list.Array_name = "yaasss"

class TestDataReduction(unittest.TestCase):
    """Test that the different data reduction methods work"""
    def test_Mean(self):
        a = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
             [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
             [[19, 20, 21], [22, 23, 24], [25, 26, 27]]]
        m = [[2, 5, 8], [11, 14, 17], [20, 23, 26]]
        i = ImageMean(a)
        self.assertEqual(m, np.ndarray.tolist(i.img))
                         
# class TestDataBases(unittest.TestCase)):
#     """Tests that components have been correctly added to the databases"""
#     def test_ImageDB(self):
            
#     def test_PCDB(self):
            
# class TestFileLoad(unittest.TestCase)):
#     """Tests that files have been correctly loaded"""
#     def test_nonmat(self):
#         df
#     def test_lol(self):
        
if __name__ == '__main__':
    unittest.main()