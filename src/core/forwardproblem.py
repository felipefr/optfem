#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 16:49:21 2021

@author: felipefr
"""
import sys
import numpy as np
sys.path.insert(0,'../femlib')
from linearsystem import LinearSystem
    
class ForwardProblem:
    
    def __init__(self, Vh):
        self.Vh = Vh
        self.LS = LinearSystem(self.Vh)
        self.param = []
        self.BCs = []
        
    def solve(self):
        self.LS.assembly(self.param)
        self.LS.applyDirichletBCs(self.BCs)
        self.u = self.LS.solve()
        
    def setParam(self, newparam):
        pass
        

        
