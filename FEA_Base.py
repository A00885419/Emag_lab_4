# Finite element analysis base for lab 4 uses the Vec3 Class

from Vec3 import *
import math
g_e0 = 8.854e-12
g_k = 1/(4*math.pi*g_e0)
# an infintismal point charge of Q coulombs and zero volume
class Charge:   
    def __init__ (self, _Q, vect):
        self.q = _Q
        self.pos = vect
    
    def field(self, vect): # electric fiel at point as a result of this charge
        return (self.pos^vect)*(g_k*self.q/((self.pos//vect)**2))*-1
    
    def __lshift__(self, charge):
        return charge.field(self.pos)*self.q
    
