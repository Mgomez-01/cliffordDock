from math import expm1
from clifford.g3 import *
import clifford as cf
from math import pi, e 
import math as math
# testing to make a script that can perform a two port analysis and make it simpler

x = e1
y = e2 
z = e3 

print("Here are a few examples of operations: \n")
print("The wedge of x and y (x^y) is a bivector e12 \nx^y = ",x^y)


u = 1*e1 + 2*e2 + 3*e3
v = 4*e1 + 5*e2 + 6*e3
u_v = u^v

uxv = u_v.dual()

print("u^v:",u_v)
print("\nThe wedge gives the bivector above, and taking its dual gives the cross product\n")
print("uxv:",uxv)

print("\nLets reflect it now across the x axis(e1)\n")
print("\nR_x(uxv) === x*(u x v)*x:",x*uxv*x)
print("\nequivalently, we can also reflect it using a sandwich multiply of the element x and its inverse\n")
print("\nR_x(uxv) === x*(u x v)*x:",x*uxv*x)
print("\nR_x(uxv) === (x)*(u x v)*(~x):",x*uxv*~x)
res = y*x*uxv*x*y
print("\nR_x(uxv) === y*x*(u x v)*x*y:",res)


print("\nrotations analagous to complex number rotations\n")
print("\ntake a rotation of pi/4 e^i*theta\n")
R1 = e**(pi/4*e12)
print("R1 = e**(pi/4*e12):",R1)
print("\nequivalent to the rotation using e12 as i, but can also be done using the other bivectors e23 and e13\n")

R2 = e**(pi/4*e23)
print("R2 = e**(pi/4*e23):",R2)
R3 = e**(pi/4*e13)
print("R3 = e**(pi/4*e13):",R3)
print("\nrotating one in the other is a simple multiplication on both sides\n")

print("\nMystery Bivector from a result of a rotation:",R1*R2*R1)

print("\nLooking at the result above, which two do you think were rotated??\n")

