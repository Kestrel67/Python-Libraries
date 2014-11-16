# pgcd n et m
def gcd(n, m):
    while m:
        (n, m) = (m, n % m)
    return n

# greatest common divisors
def lcm(n, m):
    return n * m // gcd(n, m)

# arithmetic euclide calculation (slowest)
def euclide_div_arithmethic(n, m):
    q = 0
    while n > 0:
        n -= m
        q += 1
    return (q - 1, n + m)

# basic euclide calculation
def euclide_div_basic(n, m):
    q = n // m
    r = n - q * m

    return (q, r)

# 37% faster than euclide_div_basic (quickest)
def euclide_div(n, m):
    return (n // m, n % m)

# recursive function
def gcd_recur(n, m):
    r = n % m
    
    if r:
      return euclide_recur(m, r)
    else:
      return m
