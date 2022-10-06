from math import expm1
from clifford.g4 import *
import clifford as cf
from math import pi, e 
import math as math

# impedance Z is a vector related to Y and S in CGA-G4
# this is a 4 dimensional space with a metric allowing for complex number
# calculations. Related to the choices made for the Riemannian metric

theta = pi/4
sin45 = math.sin(theta)
print("sin(pi/4):",sin45)
Z = 50 + 25*(1*e12)

# reactance plane
X = (e12) - (e24)

# impedance plane
R = (e34) - (e13)

# conductance plane 
G = (e34) + (e13)

# susceptance plane
B = (e12) + (e24)

print("Some complex load impedance Z:",Z)

print("Think of e12 as the complex plane itself, or as the imaginary unit i or j. The operations to follow will make sense from that perspective.")

print("normalize the impedance and obtain the representative complex number in the smith chart realm.\n")

print("Z/Z_0 where Z_0 is 50 Ohms\n")
print("script_z:",Z/50)
zl = Z/50
print("The reflection at the load should be the following:")

print("Gamma = (Z_L - Z_0)/(Z_0 + Z_L)")
gamma = (50 - Z)*((50 + Z).inv())
print("Gamma: ", gamma)
print("|Gamma| = ",gamma.__abs__())

print("When matched, the reflection coefficient is the following:")
Z = 50
zl = Z/50
print("Gamma = (Z_L - Z_0)/(Z_0 + Z_L)")
gamma = (50 - Z)*(50 + Z)
print("Gamma: ", gamma)
print("|Gamma| = ",gamma.__abs__())



Z = 25 + 75*(1*e12)
print("The generator for obtaining the function transforming the impedance is a negative angle rotating about the e23 plane.")

Rot = e**((theta/2)*(e23))
Rotm = e**((-theta/2)*(e23))

print("Rotating Z, R(theta*e23)Z~R(-theta*e23):",(Rot*Z*Rotm)(e12))


print("sin(pi/4)*<Z>_2:",Z.value[5] * sin45)

print("\n Instead of having to split the complex quantity Z and multiply only its imaginary component with the sin of pi/4, we can effectively do the same thing using the rotation of pi/8 one dimension up, rotating in the e23 plane with the sandwich multiply.")

print(X*R)
