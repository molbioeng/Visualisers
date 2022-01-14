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

# for PCA testing
from numpy import array
from numpy import mean
from numpy import cov
from numpy.linalg import eig
from sklearn.decomposition import PCA
import numpy.testing as npt
from numpy.testing import assert_array_almost_equal
from numpy.testing import assert_array_equal


# for PrincipalComponentDB testing
from PrincipalComponent import PrincipalComponent
from PrincipalComponentDB import PrincipalComponentDB

# for imagePCA testing
from ImagePCA import ImagePCA

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

class TestDataBases(unittest.TestCase):
    """Tests that components have been correctly added to the databases"""
    def test_ImageDB(self):
        pass

    def test_PCDB(self):
        pc_array = [ [[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]],[[13,14,15],[16,17,18]]] #The array must be at least 3-dimensional
        pc_object = PrincipalComponent(array=pc_array) #Create an object of type PrincipalComponent

        pc_db = PrincipalComponentDB() #Create an object of type PrincipalComponentDB (database)
        pc_db.principalComponents[pc_object.name] = pc_object #Add PrincipalComponent object to database

        self.assertEqual(list(pc_db.principalComponents.values())[0], pc_object)
        # Check if the first object in database is equal to PrincipalComponent object instantiated previously


# class TestFileLoad(unittest.TestCase)):
#     """Tests that files have been correctly loaded"""
#     def test_nonmat(self):
#         df
#     def test_lol(self):


class TestPCA(unittest.TestCase):
    """Test that the PCA method works"""
    def test_PCA(self):
        # First we do PCA manually:
        # define a matrix
        A = array([[1, 2], [3, 4], [5, 6]])
        print('This is A')
        print(A)
        # calculate the mean of each column
        M = mean(A.T, axis=1)
        print('This is M')
        print(M)
        # center columns by subtracting column means
        C = A - M
        print('This is C')
        print(C)
        # calculate covariance matrix of centered matrix
        V = cov(C.T)
        print('This is V')
        print(V)
        # eigendecomposition of covariance matrix
        values, vectors = eig(V)
        print('These are vectors')
        print(vectors)
        print('These are values')
        print(values)
        # project data
        P = vectors.T.dot(C.T)
        print('This is projected data, This data will be used to compare with data from PCA')
        print(P.T)

        #  Now we can test out Principal Component Analysis on a dataset
        # using the PCA() class in the scikit-learn library.

        # eigenvalues = explained_variance_ attributes
        # principal components (loadings) = components_ attributes

        # create the PCA instance
        pca = PCA(2)
        # fit on data
        pca.fit(A)
        # access values and vectors
        print('These are components_ (vectors)')
        print(pca.components_)
        print('These are exaplained_variance_ (values)')
        print(pca.explained_variance_)
        # transform data
        B = pca.transform(A)
        print('This is B')
        print(B)

        # We can get the assertion error if two array objects are
        #  not equal up to desired precision value

        decimalPlace=5 # desired precision
        self.test  = assert_array_almost_equal(B, P.T, decimalPlace)

class TestPC(unittest.TestCase):
    def test_loadings(self):
        array = [ [[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]],[[13,14,15],[16,17,18]]]
        array = np.array(array)
        data = array.reshape(len(array)*len(array[0]),len(array[0][0])) #Convert 3D array to 2D array NxP

        init_pca = PCA(n_components=None) #all possible PCs
        fitted_pca =init_pca.fit(data)

        loadings_manual = fitted_pca.components_.T

        pc_object = PrincipalComponent(array=array)
        loadings_obj = pc_object.loadings

        self.test_loadings = assert_array_equal(loadings_obj,loadings_manual)

        ######## Now test explained variance
        explained_variance_manual = fitted_pca.explained_variance_ratio_
        explained_variance_obj = pc_object.explained_variance
        self.test_expl_var = assert_array_equal(explained_variance_obj,explained_variance_manual)


class TestImagePCA(unittest.TestCase):
    def test_scores(self):
        array = [ [[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]],[[13,14,15],[16,17,18]]]
        array = np.array(array)
        data = array.reshape(len(array)*len(array[0]),len(array[0][0])) #Convert 3D array to 2D array NxP

        init_pca = PCA(n_components=None) #all possible PCs
        fitted_pca =init_pca.fit(data)

        scores_manual = fitted_pca.transform(data)  # reconstructed data

        pc_object = PrincipalComponent(array=array)
        img_pca_obj = ImagePCA(array,pc_object)
        scores_obj = img_pca_obj.scores

        self.test_scores = assert_array_equal(scores_obj,scores_manual)

        score_manual = scores_manual[:,0] #Take first score for testing
        score_for_img_manual = np.reshape(score_manual,(len(array), len(array[0])))
        scores_for_img_obj = img_pca_obj.return_Image(1)

        self.test_scores_for_img = assert_array_equal(scores_for_img_obj,score_for_img_manual)







if __name__ == '__main__':
    unittest.main()
