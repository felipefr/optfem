#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 16:48:36 2021

@author: felipefr
"""

class FEMspace:
    
    def __init__(self, mesh):
        self.mesh = mesh
        self.ndof = len(mesh.X) 
    