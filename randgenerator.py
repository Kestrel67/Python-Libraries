import random

"""Generate a random list of n elements, if uniq == True, 
each elements appears only one time, else it can appears many times"""
def genList(n, uniq = True):
  if not uniq:
    return [random.randint(0, n + 1) for i in range(n)]
  else:
    rl = list(range(n))
    random.shuffle(rl)
    return rl
    
