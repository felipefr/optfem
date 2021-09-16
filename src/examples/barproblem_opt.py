#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 16:10:18 2021

@author: felipefr
"""
import sys
import numpy as np
sys.path.insert(0,'../femlib')
from optimisationproblem import optimisationProblem

class barProblemOptimiser(optimisationProblem):
    
    def __init__(self, fp, targets, controledDofs):
        super(barProblemOptimiser, self).__init__(fp, targets)
        self.controledDofs = controledDofs
        
    def measurements(self, u):
        i1, i2, i3 = self.controledDofs
        
        eps12 = (u[i2] - u[i1])/(self.fp.Vh.mesh.X[i2] - self.fp.Vh.mesh.X[i1])
        eps3 = (u[i3] - u[i2])/(self.fp.Vh.mesh.X[i3] - self.fp.Vh.mesh.X[i2])

        return np.array([eps12, eps3])

    def costFunction(self, newparam):
        pred = self.getMeasurements(newparam)
        
        J = 0.5*(pred[0] - self.targets[0])**2 
        # J = 0.5*(pred[1] - self.targets[1])**2 # equivalent option 
        # J = 0.5*np.linalg.norm(pred - self.targets)**2 # equivalent option
        
        return J
    
class barProblemOptimiser_withJacobian(barProblemOptimiser):
    
    def __init__(self, fp, targets, controledDofs):
        super(barProblemOptimiser_withJacobian, 
                                    self).__init__(fp, targets, controledDofs)
                                    
        LSaux = self.fp.LS
        LSaux.assembly(np.array([0.0,0.0,1.0]))
        LSaux.applyDirichletBCs(self.fp.BCs)
        
        self.rhs_adj = LSaux.A@LSaux.b # matrix x vector multiplication 
        
    def jacobian(self, newparam):
        
        # Notice the LS will be assembled for fp after next line
        pred = self.getMeasurements(newparam) 
        
        self.fp.LS.b[:] = self.rhs_adj[:]
        y = self.fp.LS.solve() 
        
        i1, i2, i3 = self.controledDofs
        X = self.fp.Vh.mesh.X
        jac = - y[i2]*(pred[0] - self.targets[0])/(X[i2] - X[i1])
        
        return jac