#lab4test
from FEA_Base import *
import math

# Lab4 question 1.
def Voltage(charge, vect):
    return g_k*charge.q/(vect//charge.pos)

nPoints = 1000
ringRad = 1
rho_l = 2e-9

delta_q = rho_l*2*math.pi/nPoints

#Build the ring
ring = []
for i in range(0, nPoints):
    ring.append(Charge(delta_q, Vec3(math.sin(2*math.pi/nPoints), math.cos(2*math.pi/nPoints)*ringRad, 0)))

p_A = Vec3(0,0,1)
p_B = Vec3(0,0,2)
v_A = 0
v_B = 0
for dq in ring:
    v_A += Voltage(dq, p_A)
    v_B += Voltage(dq, p_B)
    
print(v_A - v_B)
