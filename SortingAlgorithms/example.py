# external libraries
import sys
_root = 'C:/Users/Lucas/Documents/Python/Libraries'
_externallib = [_root, _root + '/Arithmetic', _root + 'MathsFuncs', _root + 'pygraph', _root + 'SortingAlgorithms']
sys.path += _externallib

from insertionsort import *
from mergesort import *
from quicksort import *
from bubblesort import *

from functions import count

from randgenerator import *

from time import sleep

import matplotlib.pyplot as plt

N = 128   # taille initiale de la liste
B = 1   # nombre de liste de taille N à trier
M = 10   # coefficient multiplicateur
L = 10  # temps limite d'execution du programme (en seconde)

ALGO = {"Quicksort":quicksort, "Mergesort":mergesort} # , "Insertionsort":insertionsort, "Bubblesort":bubblesort, 

ABSISSA = []
PLOT = {"Quicksort":[], "Mergesort":[]} # , "Bubblesort":[], "Insertionsort":[]

while ALGO:

    ABSISSA.append(N) # pour N
    
    print(list(ALGO.keys()))    # algorithmes restant
    print('(size * lists) = {} * {}'.format(N, B))          # taille de la liste par le nombre de liste à trier
    
    p = len(ALGO) # nb d'algos restant

    l = [genList(N) for j in range(B)] # on crée B listes à trier

    todel = [] # algo à supprimer

    for algo in ALGO:

        print(algo)

        avg = sum([count(ALGO[algo], list(l[i]))[1] for i in range(B)]) / B # on fait la moyenne sur les B liste sà trier (les memes pour chaque algo)

        PLOT[algo].append(avg) # on ajoute la valeur

        print(avg, 'seconds')

        if avg >= L: # si l'algo est trop long on le supprime
            print("This algorithme took too much time and will be remove")
            todel.append(algo)

    for algo in todel: # on supprime les algo trop lents
        del ALGO[algo]

    N *= M # on passe à la taille suivante
    
    print("===========================================\n\n")
    sleep(1)
        

# plot
for l in PLOT.values():
    plt.plot(ABSISSA[0:len(l)], l)

plt.grid(True)

plt.xscale('log') # opt
plt.yscale('log') # opt

plt.show()
            
