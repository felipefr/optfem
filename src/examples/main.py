import os, sys
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize 
from functools import partial

sys.path.insert(0,'../femlib/')
from mesh import Mesh
from linearsystem import LinearSystem
from FEspace import FEspace
from barproblem import barProblem
from barproblem_opt import barProblemOptimiser, barProblemOptimiser_withJacobian

    

L = 1.0
nnod = 4
mesh = Mesh()

mesh.setCoordinates(np.linspace(0.0, L, nnod))         
for i in range(len(mesh.X) - 1):
    mesh.addElement([i,i+1])

Vh = FEspace(mesh)

p = barProblem(Vh)

eps12_target = 0.5
eps3_target = 2.0
dof1 = 0
dof2 = 2
dof3 = 3
opt = barProblemOptimiser(p,np.array([eps12_target,eps3_target]), [dof1, dof2, dof3])

opt_jac = barProblemOptimiser_withJacobian(p,np.array([eps12_target,eps3_target]), [dof1, dof2, dof3])


k_target =  eps12_target*mesh.X[2]/(eps3_target*(mesh.X[1] + 2*(mesh.X[2] - mesh.X[1])))

out_1 = minimize(opt.costFunction, 1.0, method = 'Nelder-Mead')
out_2 = minimize(opt.costFunction, 1.0, method = 'BFGS')
out_3 = minimize(opt.costFunction, 1.0, method = 'CG')

print(out_1)
print(out_2)
print(out_3)


    