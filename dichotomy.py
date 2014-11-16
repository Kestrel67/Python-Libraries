# l : une liste trié par ordre croissant
# e : élément à trouver ou à encadrer
# si e appartient à e alors le nombre retourné est l'indice de la liste ou ce trouve l'élément
# si un couple est retourné alors:
#   * couple = (0, -1) alors l'élément cherché est plus petit que le plus petit élément de la liste
#   * couple = (-1, 1) alors l'élément cherché est plus grand que le plus grand élément de la liste
#   * couple = (a, b) / a < b alors les élément l[a] et l[b] encadrent l'élément cherché 
# complexity : ln2(len(l) = n))
def dichotomy(l, e):
    size = len(l)
    (a, b) = (0, size - 1)
    
    while b - a > 1:
        m = (a + b) // 2

        if e == l[m]:
            return m
        elif e < l[m]:
            b = m
        else:
            a = m
            
    if e == l[a]:
        return a
    elif e == l[b]:
        return b
    elif l[a] < e < l[b]:
        return a, b
    elif e < l[a]:
        return (0, -1)
    else:
        return (-1, 0)
    
    return a, b
