import time

# return True if obj is iterable
def iterable(obj):
  try:
    iter(obj)
    return True
  except:
    return False

# @decorator : count the execution time of the function
def DECOcount(func):
  def f(*args, **kargs):
    start = time.time()
    ret = func(*args, **kargs)
    end = time.time()

    print(end - start, "seconds")

    return ret
  return f

# function : count the execution time of the function
def count(func, *args, **kargs):
  start = time.time()
  ret = func(*args, **kargs)
  end = time.time()

  return (ret, end - start)

# contraint le type des paramètres d'une fonction
def constrainType(*types):
    # init
    allowedtypes = []
    ltypes = len(types)
    for t in types:
        if type(t) not in (tuple, list):
            allowedtypes.append((t, ))
        else:
            allowedtypes.append(tuple(t))

    # decorateur
    def func(f):
        def call(*args, **kargs):
            largs = len(args)

            #assert largs <= ltypes

            for i in range(min(largs, ltypes)):
                t = type(args[i])
                    
                if t not in allowedtypes[i]:
                    raise Exception('Le {}ème paramètre doit être du type {}'.format((i + 1), allowedtypes[i]))

            return f(*args, **kargs)
        return call
    return func


##############################
####### DIR FUNCTIONS ########
##############################

# file or dir exists
def existsFD(location):
    return os.path.exists(location)

# is file
def isF(location):
    return os.path.isfile(location)

# is dir
def isD(location):
    return os.path.isdir(location)

# file exists
def existsF(location):
    return existsFD(location) and isF(location)

# dir exists
def existsD(location):
    return existsFD(location) and isD(location)


# example
if __name__ == "__main__":
    @constrainType((int, float, complex), int)
    def power(x, n):
            return x**n

    @constrainType((int, float, complex), (int, float, complex), int)
    def x(z1, z2, n):
        return (n * z1 + z2) * (z1 - n * z2) ** n
