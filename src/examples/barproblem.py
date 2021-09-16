#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 16:49:21 2021

@author: felipefr
"""
import sys
import numpy as np
sys.path.insert(0,'../femlib/')
sys.path.insert(0,'../core/')

from linearsystem import LinearSystem
from forwardproblem import ForwardProblem
    
class barProblem(ForwardProblem):
    
    def __init__(self, Vh):
        super(barProblem,self).__init__(Vh)
        
        self.E0 = 1.0        
        self.ubar = np.max(Vh.mesh.X)
        
        self.param = np.array([self.E0, 0.5*self.E0, self.E0])
        self.BCs = [(0, 0.0), (-1, self.ubar)]
    
    def setParam(self, newparam):
        self.param[2] = newparam*self.E0

