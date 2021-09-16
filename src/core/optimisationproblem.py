#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 15:11:04 2021

@author: felipefr
"""

class optimisationProblem:
    
    def __init__(self, fp, targets):
        self.fp = fp # foward problem
        self.targets = targets

    def getMeasurements(self, newparam):
        
        self.fp.setParam(newparam)
        self.fp.solve()
        
        return self.measurements(self.fp.u)
        
    def measurements(self, u):
        pass

    def costFunction(self, k):
        pass 



