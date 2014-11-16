from sympy import binomial, symbols, simplify

# calculate sum (i = 1 --> n) i^k
def S(n, k):
    if k == 0:
        return n
    elif k == 1:
        return n * (n + 1) // 2
    elif k == 2:
        return (n) * (n + 1) * (2 * n + 1) // 6
    elif k >= 3:
        return ((1 + n) ** (k + 1) - 1 - sum(binomial(k + 1, i) * S(n, i) for i in range(0, k))) // (k + 1)

# var
n = symbols('n')

def SympySum(k, simpli = True):
    if k == 0:
        return n
    elif k == 1:
        return n * (n + 1) / 2
    elif k == 2:
        return (n) * (n + 1) * (2 * n + 1) / 6
    elif k >= 3:
        expr = ((1 + n) ** (k + 1) - 1 - sum(binomial(k + 1, i) * SympySum(i, simpli) for i in range(0, k))) / (k + 1)

        if simpli:
            expr = simplify(expr)

        return expr
    
