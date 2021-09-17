import sys
import numpy as np
from scipy.optimize import minimize 

sys.path.insert(0,'../femlib/')
from mesh import Mesh
from linearsystem import LinearSystem
from FEspace import FEspace
from barproblem import barProblem
from barproblem_opt import barProblemOptimiser
  
# Creating the mesh
L = 1.0
nnod = 4
mesh = Mesh()

mesh.setCoordinates(np.linspace(0.0, L, nnod))         
for i in range(len(mesh.X) - 1):
    mesh.addElement([i,i+1])

# Creating fe space and the foward-problem 
Vh = FEspace(mesh)
p = barProblem(Vh)

# setting the targets and the optimisation problem
eps12_target = 0.5
eps3_target = 2.0
dofs = [0, 2, 3]
opt = barProblemOptimiser(p,np.array([eps12_target,eps3_target]), dofs)

#
k_target =  eps12_target*mesh.X[2]/(eps3_target*(mesh.X[1] + 2*(mesh.X[2] - mesh.X[1])))

# testing optimisation methods
out_1 = minimize(opt.costFunction, 1.0, method = 'Nelder-Mead') # heuristic
out_2 = minimize(opt.costFunction, 1.0, method = 'BFGS') # Quasi-Newton
out_3 = minimize(opt.costFunction, 1.0, method = 'CG') # No hessian

error_rel = [abs(out.x[0] - k_target)/k_target for out in [out_1, out_2, out_3]]

print(error_rel)
print(out_1)
print(out_2)
print(out_3)


    