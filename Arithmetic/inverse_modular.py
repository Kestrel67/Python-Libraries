from euclide import gcd

# decorator
def coprimes(func):
    def funcp(a, b):
        if gcd(a, b) != 1:
            raise Exception('a et b ne sont pas premiers entre eux')
        return func(a, b)
    return funcp

# equa diophantienne
# dioph(247825482538725487253872458725387254782537, 24785245872358725487253487258735872582537)
@coprimes
def dioph(a, b):
    q, r = divmod(a, b)

    #print("{} = {} * {} + {}".format(a, b, q, r))

    if r == 1:
        return (1, -q)
    else:
        alpha, beta = dioph(b, r)

        return (beta, alpha - beta * q)

# find c as n * a = 1 (mod p)
def modinvrec(n, p):
    a, q = dioph(n, p)
    if a <= 0:
        raise ValueError
    return a


# dioph
def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)

# modinv(a, b) = x / x * a congrus à 1 (mod b)
def modinv(a, m):
    g, x, y = extended_gcd(a, m)
    if g != 1:
        raise ValueError
    return x % m
