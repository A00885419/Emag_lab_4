# Finite element analysis base for lab 4
import math
# general purpose 3d vector class based on my old 2d vector
class Vec3: 
    def __init__ (self, ix, iy, iz):
        self.x = float(ix)
        self.y = float(iy)
        self.z = float(iz)
        
    # vector operations
    
    # Vector Addition (+)
    def __add__ (self, vect):
        return (Vec3(self.x + vect.x, self.y + vect.y, self.z + vect.z))

    # Vector Dot/ multiplication Product (*)
    def __mul__ (self, vect):
        if(isinstance(vect, self.__class__)):
            return float(self.x*vect.x+self.y*vect.y+self.z*vect.z)
        elif(isinstance(vect,float) or isinstance(vect,int)): # multiplying a scalar
            return Vec3(self.x*vect, self.y*vect, self.z*vect)
    # Vector Subtraction (-)
    def __sub__ (self, vect):
        return (self + vect*(-1))
    # Scalar division
    def __truediv__ (self, scal):
        return self*(1/scal)
         
    # Vector Distance to (//) (Position vectors only)
    def __floordiv__ (self, vect):
        return math.sqrt((vect.x- self.x)**2 + (vect.y - self.y)**2 + (vect.z - self.z)**2)
    # Vector Direction to (^)
    def __xor__(self, vect):
        return ((vect - self)/(self//vect))
    
    def crossp(self, vect):
        return Vec3((self.y*vect.z - self.z*vect.y),(self.z*vect.x - self.x*vect.z), (self.x*vect.y-self.y*vect.x))
        
# Cylindrical Conversion accessors
    
    # Radial Component
    
    def rho(self):
        return(math.sqrt(self.x**2+self.y**2))
    # Cylindrical angle
    def phi(self):
        return math.atan2(self.y, self.x)
# Spherical Conversion Accessors
    
    #def r(self):
    def r(self):
        return(math.sqrt(self.x**2+self.y**2 + self.z**2))
    #def theta(self):
    def theta(self):
        return(math.acos(self.z/self.r()))
    
    def __str__ (self):
        return "[" + str(self.x) + ", " + str(self.y) + ", "+ str(self.z) +"]"
