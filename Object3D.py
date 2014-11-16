try:
  from sympy import sqrt, acos, asin, pi
except:
  from math import sqrt, acos, asin, pi, floor, ceil

import math

def CheckType(obj, cla, error = True):
  if isinstance(obj, cla):
    return True
  elif error:
    raise Exception("L'objet {} n'est pas de la classe {}".format(obj, cla))
  else:
    return False
    

class Object3D:
  def __init__(self, x = 0, y = 0, z = 0):
    self.setCoords(x, y, z)

  def setCoords(self, x = 0, y = 0, z = 0):
    (self.x, self.y, self.z) = (x, y, z)

  def getCoords(self):
    return (self.x, self.y, self.z)

  def __repr__(self):
    return "({}, {}, {})".format(*self.getCoords())



class Point(Object3D):
  def distance(self, P):
    CheckType(P, Point)
    return sqrt((P.x - self.x) ** 2 + (P.y - self.y) ** 2 + (P.z - self.z) ** 2)

  def __repr__(self):
    return "Point " + super(Point, self).__repr__()

  def confused(self, P):
    CheckType(P, Point)
    return P.getCoords() == self.getCoords()



class Vector(Object3D):
  def __init__(self, xA = 1, yB = 0, z = 0):
    if CheckType(xA, Point, False) and CheckType(yB, Point, False):
      self.x = yB.x - xA.x
      self.y = yB.y - xA.y
      self.z = yB.z - xA.z
    else:
      super(Vector, self).__init__(xA, yB, z)

  def __add__(self, V):
    CheckType(V, Vector)
    return Vector(V.x + self.x, V.y + self.y, V.z + self.z)

  #def __radd__(self, V):
  #  return self.__add__(V)

  def __pos__(self):
    return self

  def __neg__(self):
    return Vector(-self.x, -self.y, -self.z)

  def __sub__(self, V):
    CheckType(V, Vector)
    return Vector(V.x - self.x, V.y - self.y, V.z - self.z)

  def __mul__(self, Obj):
    if CheckType(Obj, Vector, False):
      return self.product(Obj)
    else:
      return Vector(Obj * self.x, Obj * self.y, Obj * self.z)
  
  def __rmul__(self, scalar):
    return self.__mul__(scalar)

  def __div__(self, scalar):
    return self.__mul__(1 / scalar)

  def __eq__(self, V):
    CheckType(V, Vector)
    return self.getCoords() == V.getCoords()

  def __round__(self, n):
    return Vector(*[round(i, n) for i in self.getCoords()])

  def __floor__(self):
    return Vector(*[math.floor(i) for i in self.getCoords()])

  def __ceil__(self):
    return Vector(*[math.ceil(i) for i in self.getCoords()])

  def __xor__(self, V):
    return self.cross(V)

  def length(self):
    return sqrt(sum(i ** 2 for i in self.getCoords()))

  def product(self, V):
    CheckType(V, Vector)
    return V.x * self.x + V.y * self.y + V.z * self.z

  def cross(self, V):
    CheckType(V, Vector)
    return Vector(self.y * V.z - self.z * V.y, self.z * V.x - self.x * V.z, self.x * V.y - self.y * V.x)

  def collinear(self, V):
    CheckType(V, Vector)
    return self.angle(V) % pi == 0

  def orthogonal(self, V):
    return V * self == 0

  def angle(self, V):
    CheckType(V, Vector)
    return acos(V * self / (V.length() * self.length()))
    
  def __repr__(self):
    return "Vector " + super(Vector, self).__repr__()

class Line(Object3D):
  def __init__(self, A = Point(0, 0, 0), u = Vector(1, 0, 0)):
    CheckType(A, Point)
    CheckType(u, Vector)

    if u.length() == 0:
      raise Exception("Le vecteur doit être différent du vecteur nul")

    self.point = A
    self.vector = u

  def __repr__(self):
    s = "{} * t + {}"
    return "Line : \n" + s.format(self.vector.x, self.point.x) + "\n" + s.format(self.vector.y, self.point.y) + "\n" +  s.format(self.vector.z, self.point.z)


def middle(A, B):
  return Point((A.x + B.x) / 2, (A.y + B.y) / 2, (A.z + B.z) / 2)


if __name__ == "__main__":
  O = Point(0, 0, 0)

  S1 = Point(1, 0, 0)
  S2 = Point(0, 1, 0)
  S3 = Point(0, 0, 1)

  i, j, k = Vector(O, S1), Vector(O, S2), Vector(O, S3)
  z = Vector(1, 1, 1)
  A = Point(2, 2, 0)
  B = Point(3, 2, 3)
  C = Point(-2, 1, 1)
  D = Point(3, 3, 3)

  u = 2*i + 4*j
  v = -i + 3*j + 2*k
  w = i + j - k

  print(u * v, u.product(v))
  print(u.angle(v))
  print(u.collinear(2*u))
  print(i^j, i.cross(j))
  print(i.orthogonal(j))
  
  
