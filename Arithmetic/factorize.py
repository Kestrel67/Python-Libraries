# external libraries
import sys
_root = 'C:/Users/Lucas/Documents/Python/Libraries'
_externallib = [_root, _root + '/Arithmetic', _root + 'MathsFuncs', _root + 'pygraph', _root + 'ArduinoInterface', _root + 'SortingAlgorithms']
sys.path += _externallib

from math import sqrt, log10, ceil

from sumprod import prod

# sympy library for FiniteSet tool
# sympy prime generator : sympy.ntheory.generate.Sieve()
from sympy import FiniteSet, prime

# diviseurs premiers de n (dummy)
# return l = [(p1, alpha1), (p2, alpha2), ... , (pn, alpha n)]
# tel que n = p1 ** alpha1 * p2 ** alpha2 * ... * pn ** alpha n
def factorize(n):
  if n <= 1:
    return []

  div = []

  f, p = 2, 0
  while not n & 1:
    n //= 2
    p += 1

  if p:
    div.append((f, p))

  f, p = 3, 0
  while n != 1 and f <= int(sqrt(n)):
    while not n % f:
      n //= f
      p += 1

    if p:
      div.append((f, p))
      p = 0

    f += 2

  if n != 1:
    div.append((n, 1))

  return div


# prime generator
def PrimeGenerator():
  i = 0
  while True:
    i += 1
    yield prime(i)

# diviseurs premiers de n (smart)
# return l = [(p1, alpha1), (p2, alpha2), ... , (pn, alpha n)]
# tel que n = p1 ** alpha1 * p2 ** alpha2 * ... * pn ** alpha n
# primeGenerator : générateur de tous les nombrs premiers comme sympy.ntheory.generate.Sieve()
# (génération par ordre croissant)
def factorizeSmart(n, primeGenerator):
  if n <= 1:
    return []

  div = []

  power = 0
  while not n & 1:
    n //= 2
    power += 1

  if power:
    div.append((2, power))

  # check
  assert next(primeGenerator) == 2
  assert next(primeGenerator) == 3

  p, power = 3, 0
  while n != 1 and p <= int(sqrt(n)):
    while not n % p:
      n //= p
      power += 1

    if power:
      div.append((p, power))
      power = 0

    p = next(primeGenerator)

  if n != 1:
    div.append((n, 1))

  return div

# valuation p-adique
# p : prime number
# l : décomposition en produit de facteurs premier d'un nombre
def p_adic_valuation(p, l):
  for c in l:
    if p == c[0]:
      return c[1]
  return 0

# retourne le nombre de divisieurs
# l : décomposition en produit de facteurs premier d'un nombre
def divisors_count(l):
  return prod(p + 1 for d, p in l)

# l = (alpha1, alpha2, alpha3, ..., alpha n)
# gen all (x1, x2, ..., xn) belonging to (A1 * A2 * ... * An)
def genCoupleFromPowerList(l):
  A = FiniteSet(list(range(l[0] + 1))) # sympy.FiniteSet
  for p in l[1:]:
    A = A * FiniteSet(list(range(p + 1))) # cartesian product

  return A

# retourne la liste des diviseurs de n dont la décomposition en produit de facteurs premier est l
def divisors(l): # smart
  n = len(l)

  # liste des diviseurs de n
  d = []

  if n == 0: # case n = 0
    return 1
  elif n == 1: # case n = p1 ** alpha1
    p1 = l[0][0]
    
    for alpha1 in range(l[0][1] + 1):
      d.append(p1 ** alpha1)

    return d
      
  else: # case n = p1 ** alpha1 * p2 ** alpha2 * ... * pn ** alpha n
    (pi, alphai) = ([], []) # liste des nombres premiers avec leur puissances respectives

    # génération pi, alphai
    for p, alpha in l:
      pi.append(p)
      alphai.append(alpha)

    # on consrtuit la liste des diviseurs
    for alphai in genCoupleFromPowerList(alphai):
      di = 1
      for i in range(n):
        di *= pi[i] ** alphai[i]
        
      d.append(di)

    return d
  

# recomposition
def compose(l):
  n = 1
  for couple in l:
    prime, power = couple
    n *= prime ** power
  return n

# display
def display(l):
  n = compose(l)
  
  floor_line = top_line = ""

  for q, p in l:
    floor_line += str(q) + " " * ceil(log10(p))
    top_line += " " * ceil(log10(q)) + str(p)

    floor_line += " * "
    top_line += "   "

  print(" " * ceil(log10(n)) + "   " + top_line)
  print(str(n) + " = " + floor_line[:-2])

  return n

if __name__ == "__main__":
  display(factorize(1605700466721635106816000))
  
