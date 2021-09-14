#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 16:49:21 2021

@author: felipefr
"""

import numpy as np
from linearsystem import LinearSystem
    
class barProblem:
    
    def __init__(self, Vh):

        self.Vh = Vh
        
        self.E0 = 1.0        
        self.ubar = np.max(Vh.mesh.X)
        
        self.nel = 3
        self.nnod = self.ndof = self.nel + 1 
        self.mat = np.array([self.E0, 0.5*self.E0, self.E0])
    
        self.LS = LinearSystem(self.Vh)
        
    def updateMaterial(self, k):
        self.mat[2] = k*self.E0
        
    def solve(self):

        self.LS.assembly(self.mat)
        self.LS.applyDirichletBCs(0, 0.0)
        self.LS.applyDirichletBCs(-1, self.ubar)
        
        self.u = self.LS.solve()
        
    def getStrains(self, k):
        
        self.updateMaterial(k)
        self.solve()

        eps12 = (self.u[2] - self.u[0])/(self.Vh.mesh.X[2] - self.Vh.mesh.X[0])
        eps3 = (self.u[3] - self.u[2])/(self.Vh.mesh.X[3] - self.Vh.mesh.X[2])

        return eps12, eps3


    def costFunction(self, k, eps12_target, eps3_target):
        
        eps12, eps3 = self.getStrains(k)
        
        J = 0.5*(eps12 - eps12_target)**2 + 0.5*(eps3 - eps3_target)**2
        
        return J