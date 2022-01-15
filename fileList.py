# -*- coding: utf-8 -*-
"""
Created on Thu Jan  6 00:29:25 2022

@author: FM

Globals file, prevents them from being initialised more than once, but can be used among different files
"""
from ArrayDB import ArrayDB

def init():
    global List #MAYBE NOT GLOBALA CHENGE LATER
    List = []
    global File #MAKE GLOBAL FILE NAME LATERRR
    File = None
    global method
    method = "Mean"
    global arrdb 
    arrdb = ArrayDB()
    global Data
    global ErrorMessage #error popup window messages
