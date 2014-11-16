from math import sqrt

# diviseurs de n (dummy)
def divisors(n, naturals = True):
    assert isinstance(n, int)
    
    if n == 1:
        return {1}
    
    d = set()
    p = 1
    n = abs(n)
    while p <= sqrt(n):
        if not n % p:
            d.add(p)
            d.add(n // p)

        p += 1

    if not naturals:
        d = d.union(set(-e for e in d))

    return d

# nb de diviseurs
def divisors_count(n):
    return len(divisors(n))
