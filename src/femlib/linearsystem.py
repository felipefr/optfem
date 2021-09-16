#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 16:48:52 2021

@author: felipefr
"""

import numpy as np


class LinearSystem:
    
    def __init__(self, Vh): 
        self.Vh = Vh    
        self.A = np.zeros((self.Vh.ndof, self.Vh.ndof))
        self.b = np.zeros(self.Vh.ndof)
    
    def assembly(self, mat):
        self.A.fill(0.0)
        self.b.fill(0.0)
        
        E = np.array([1,-1, -1, 1])
        indI = lambda z : np.array([z[0], z[0], z[1], z[1]])
        indJ = lambda z : np.array([z[0], z[1], z[0], z[1]])
        
        for i, e in enumerate(self.Vh.mesh.Elem):
            hi = self.Vh.mesh.X[e[1]] - self.Vh.mesh.X[e[0]]
            self.A[indI(e),indJ(e)] += (mat[i]/hi)*E
    
    def applyDirichletBCs(self, BCs):
        for bc in BCs:
            self.applyDirichletBC(*bc)
            
    def applyDirichletBC(self, i,ubar):   
        self.A[i,:] = 0.0
        self.A[i,i] = 1.0
        self.b[i] = ubar
        
    def solve(self): 
        return np.linalg.solve(self.A,self.b)
        