# @author : Lucas Dietrich (alias Kestrel)
# @date 14/11/2013

from math import e

# donne une approximation de la valeur alpha pour laquelle f(alpha) = 0
# entre les bornes a et b avec une précision de 10^(-accuracy)
def dichotomy(f, a, b, accuracy = 2):
    
    assert callable(f)
    assert a < b
    assert f(a) * f(b) < 0

    while (b - a) > 10**(-accuracy):
        p = (a + b) / 2
        
        fp = f(p)

        if fp < 0:
            a = p
        elif fp > 0:
            b = p
        else:
            return p

    return [a, b]

# on tente de trouver les intervalles comprenant une racine, commançant à start, avec un increment de 1 par défaut (pour + oo)
# de -1 pour trouver les racines vers - oo, la valeur maximale maxVal et minimale minVal
def find(f, start = 0, increment = 1, maxVal = 10, minVal = -10):
    assert callable(f)

    # on repousse les bornes définies
    if start < minVal:
        minVal = start

    if start > maxVal:
        maxVal = start

    pointer = start
    
    positions = []

    # tant qu'on est encore dans l'intervalle d'étude
    while pointer <= maxVal and pointer >= minVal:

        # si on trouve une racine entre, on suppose la fonction continue
        if f(pointer) * f(pointer - increment) < 0:

            # on forme l'intervalle
            interval = (pointer - increment, pointer) if increment > 0 else (pointer, pointer - increment)
            positions.append(interval)

        # on incrémente la position du pointeur
        pointer += increment

    # on retourne les positions trouvées
    return positions
    

# fonction moyenne() sur une liste
def average(x):
    assert isinstance(x, list)
    return sum(x) / len(x)

# example 1 :  1 root
def example1():

    # fonction f sur R
    f = lambda x : x**3+3*x**2+1

    # on récupère l'intervalle
    interval = find(f, -100)[0]

    # on affiche une valeur proche de cette racine
    print("racine :", average(dichotomy(f, *interval, accuracy = 5)))

# example 2 :  3 roots
def example2():

    # fonction g sur R
    g = lambda x : x**5 - 4*x**4 + 4*x**3 - 5*x**2 + 5*x - 1

    # on récupère les intervalles
    intervals = find(g, increment = 0.01) + find(g, increment = -0.01)

    # pour chaque intervalles on applique la fonction de dichotomie pour trouver la racine
    if intervals:
        for i, (a, b) in enumerate(intervals):
            # on affiche une valeur proche de cette racine
            print("racine %a:" % (i + 1), average(dichotomy(g, a, b, 5)))

def example3():
    h = lambda x : x**3 - x - e**x + 2

    intervals = find(h, -2, 0.1, 6)

    if intervals:
        for i, (a, b) in enumerate(intervals):
            print("racine %a:" % (i + 1), average(dichotomy(h, a, b, 10)))
    
if __name__ == "__main__":
    print("fonction f(x) = x**3+3*x**2+1")
    example1()

    print("\nfonction g(x) = x**5 - 4*x**4 + 4*x**3 - 5*x**2 + 5*x - 1")
    example2()

    print("\nfonction h(x) = x**3 - x - e**x + 2")
    example3()
