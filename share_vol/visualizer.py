from numpy import e,pi
from clifford import Cl
import numpy as np
from clifford.g3c import *
from clifford.tools.g3c import *
from pyganja import *

layout, blades = Cl(3)   # create a 3-dimensional clifford algebra

locals().update(blades) # lazy way to put entire basis in the namespace


def R_euler(phi, theta,psi):
    Rphi = e**(-phi/2.*e12)
    Rtheta = e**(-theta/2.*e23)
    Rpsi = e**(-psi/2.*e12)

    return Rphi*Rtheta*Rpsi

R = R_euler(pi/4, pi/4, pi/4)
R

A = [e1, e2, e3]         # initial ortho-normal frame
B = [R*a*~R for a in A]  # resultant frame after rotation

B

# b|a is a multivector, `[()]` selects the scalar part
M = np.array([
    [(b|a)[()] for b in B]
    for a in A
])
print("M:",M)  # rows correspond to A, columns to B

X = e1+2*e2
print("X:",X)
print("R*X*~R",R*X*~R)

Xv = np.array([1, 2, 0])
print("Xv",Xv)
print("M @ Xv",M @ Xv)

# Rotation matrix to rotor
B = [M[0,0]*e1 + M[0,1]*e2 + M[0,2]*e3,
     M[1,0]*e1 + M[1,1]*e2 + M[1,2]*e3,
     M[2,0]*e1 + M[2,1]*e2 + M[2,2]*e3]
print("B:",B)

A = [e1,e2,e3]
R = 1+sum([A[k]*B[k] for k in range(3)])
R = R/abs(R)

print("R:",R)

print("R_euler(pi/4, pi/4, pi/4): ",R_euler(pi/4, pi/4, pi/4))










P1 = up(random_euc_mv()*0.1)
P2 = up(random_euc_mv()*0.1)
P3 = up(random_euc_mv()*0.1)
P4 = up(random_euc_mv()*0.1)

# The sphere is the outer product of all 4
S = (P1^P2^P3^P4).normal()

# A line is the outer product of 2 with ninf
L = P1^P2^einf

# The inversion of a line in a sphere is a circle
C = S*L*S

# The tangent to the circle at the intersection point is the reflected line
Ldash = (P1|C)^einf

# The tangent plane to the sphere at the intersection point can be easily found
Ppi = (P1|S)^einf

scene = GanjaScene()
scene.add_objects([P1,P2,P3,P4], color=Color.BLACK)
scene.add_objects([L], color=Color.BLUE
scene.add_objects([Ldash], color=Color.RED)
scene.add_objects([C], color=Color.RED)
scene.add_objects([S*einf*S], color=Color.BLACK)
scene.add_objects([S])
scene.add_objects([Ppi], color=rgb2hex((0,100,0))+int('70000000',16))

draw(scene,scale=0.5)

