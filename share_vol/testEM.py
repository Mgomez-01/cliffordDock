
from clifford.g3c import *
from clifford.tools.g3c import*
from clifford.g4 import *
from pyganja import *
from math import e,pi
from cmath import *
import time


E = e1 + e2 + e3
B = e12 + e13 + e23

print("E field has unit components in every direction:",E)

print("B Bi-vector-field has :",B)

#Rotor describing a lossless transmission line
l = [0,10,100,1000]

x = 1
b = 1
j = 0
res = {}
for i in l:
    res[i] = i/2*(((x+b)*e12) + ((x-b)*e24))
    j=j+1

print("Lossless line rotor for swr circles:",res)


x = .01
b = 1000
n = 1
for i in l:
    res[i] = (((x*n+b)*(e12)) + ((x*n-b)*e24))
    n=n*10

print("if x > b. the line is no longer lossless, and we get constant resistance circles with the impedance getting closer to an infinite impedance on the smithchart:",res)
b = 1
x = 1

#print out some transmission line rotations to show the impedance of the line over distance l in the lossless case
theta = 0
ZL = 50+25*e23
# normalize to 50 ohm line
zL = ZL/50

# rotating the line by using the e23 plane as the imaginary unit. This generator gives back the rotated impedance. This shows the magnitude stays the same, and the only thing happening is a rotation as we would expect using j or i.

# To show this, we will use cmath to import the complex plane and methods for computing vector quantities
equivalent_Z = 50 + 25j
equivalent_zL = equivalent_Z/50


while 1:
    res = zL*e**((-theta*pi/180)*(e23))
    res2 = equivalent_zL*e**(-1j*theta*pi/360)
    print("GA version:\nRotation angle degrees: {}\nResult: {}\nMagnitude: {}\nProjection from G4 into complex impedance plane: {}\n\n".format(theta,res,res.__abs__(),res(2)))
    print("Conventional:\nRotation angle degrees: {}\nResult: {}\nMagnitude: {}\n\n".format(theta,res2,abs(res2)))
    theta = 0 if (theta == 360) else theta + 1 
    time.sleep(.1)
