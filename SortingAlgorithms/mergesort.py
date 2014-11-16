from quicksort import quicksort

def mergesort(n, size = 10):
  L = len(n)
  if L < size:
    return quicksort(n)
  else:
    a = mergesort(n[:L//2], size)
    b = mergesort(n[L//2:], size)

    return merge(a, b)

def merge(a, b):
  u, v = len(a), len(b)
  i, j = 0, 0
  o = []

  while i < u and j < v:
    if a[i] < b[j]:
      o.append(a[i])
      i += 1
    else:
      o.append(b[j])
      j += 1

  if i < u:
    o += a[i:]
  else:
    o += b[j:]

  return o
