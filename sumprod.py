from functions import iterable

# iterables and numbers
# sum(1, 2, [3, 4, [5, [[[6]]]], 7]) = sum(1, 2, 3, 4, 5, 6, 7) = 28
def sum(*args):
  s = 0
  for elem in args:
    if iterable(elem):
      s += sum(*elem)
    else:
      s += elem
  return s

# iterables and numbers
# prod(1, 2, [3, 4, [5, [[[6]]]], 7]) = sum(1, 2, 3, 4, 5, 6, 7) = 5040
def prod(*args):
  p = 1
  for elem in args:
    if iterable(elem):
      p *= prod(*elem)
    else:
      p *= elem
  return p


if __name__ == '__main__':
  factorial = lambda n: prod(j for j in range(1, n + 1))
  suminv = lambda n: sum(1/j for j in range(1, n + 1))
  suminvsquared = lambda n: sum(1/j**2 for j in range(1, n + 1))

  print(factorial(3), factorial(4), factorial(5), factorial(6))

  print(suminv(1), suminv(10), suminv(100), suminv(1000), suminv(10000))

  print(suminvsquared(10000) - 3.14159**2 / 6)
