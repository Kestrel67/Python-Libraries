# quicksort O(n log n) =< avg =< O(n^2)
def quicksort(n):
        if len(n) <= 1:
                return n
        else:
                l, r = [], []
                p = n[-1]
                
                for i in n[:-1]:
                        if i < p:
                                l.append(i)
                        else:
                                r.append(i)
                
                return quicksort(l) + [p] + quicksort(r)

# quicksort with lambda
def qsort(n, comp = lambda a, b: a < b):
        if len(n) <= 1:
                return n
        else:
                l, r = [], []
                p = n[-1]
                
                for i in n[:-1]:
                        if comp(i, p):
                                l.append(i)
                        else:
                                r.append(i)
                
                return qsort(l, comp) + [p] + qsort(r, comp)
