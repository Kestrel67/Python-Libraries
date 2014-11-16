from math import sqrt
from random import randrange

# test de primalité naif
def prime(n):
  if n <= 1 or not n & 1:
    return False

  f = 3
  while f <= int(sqrt(n)):
    if n % f == 0:
      return False
    f += 2

  return True

# test de primalité évolué (Fermat)
# primes : bases à tester (supposés premiers)
# example : fermatPrime(1267650600228402790082356974917)
# 1267650600228402790082356974917 = 1125899906842679 * 1125899906842723
def fermatPrime(n, primes = (2, 3)):

  #fermat 
  if n in primes:
    return True

  if n <= 1 or not n & 1:
    return False

  for p in primes:
    if pow(p, n - 1, n) != 1:
      return False

  f = 3
  while f <= int(sqrt(n)):
    if n % f == 0:
      return False
    f += 2

  return True

# miller rabin, _mrpt_num_trials ; number of bases to test
def MillerRabinPrime(n, _mrpt_num_trials = 5):
    assert n >= 2
    # special case 2
    if n == 2:
        return True
    # ensure n is odd
    if n % 2 == 0:
        return False
    # write n-1 as 2**s * d
    # repeatedly try to divide n-1 by 2
    s = 0
    d = n-1
    while True:
        quotient, remainder = divmod(d, 2)
        if remainder == 1:
            break
        s += 1
        d = quotient
    assert(2**s * d == n-1)
 
    # test the base a to see whether it is a witness for the compositeness of n
    def try_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2**i * d, n) == n-1:
                return False
        return True # n is definitely composite
 
    for i in range(_mrpt_num_trials):
        a = randrange(2, n)
        if try_composite(a):
            return False
 
    return True # no base tested showed n as composite
