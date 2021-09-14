#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 16:48:02 2021

@author: felipefr
"""

class Mesh:
    
    def __init__(self):
        self.X = []
        self.Elem = []
    
    def setCoordinates(self,X):
        self.X = X
         
    def addElement(self,e):
        self.Elem += [e]
        