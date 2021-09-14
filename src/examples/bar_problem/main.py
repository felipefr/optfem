import os, sys
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize 
from functools import partial
from mesh import Mesh
from linearsystem import LinearSystem
from FEMspace import FEMspace
from barProblem import barProblem

L = 1.0
nnod = 4
mesh = Mesh()

mesh.setCoordinates(np.linspace(0.0, L, nnod))         
for i in range(len(mesh.X) - 1):
    mesh.addElement([i,i+1])

Vh = FEMspace(mesh)

p = barProblem(Vh)

eps12_target = 0.5
eps3_target = 2.0

k_target =  eps12_target*mesh.X[2]/(eps3_target*(mesh.X[1] + 2*(mesh.X[2] - mesh.X[1])))

J = partial(p.costFunction, eps12_target = eps12_target, eps3_target = eps3_target)

out_1 = minimize(J, 1.0, method = 'Nelder-Mead')
out_2 = minimize(J, 1.0, method = 'BFGS')
out_3 = minimize(J, 1.0, method = 'CG')

print(out_1)
print(out_2)
print(out_3)


    