from math import sqrt

def example_function(x):
    return x**2-x+2

# example : arc_length(lambda x: sqrt(1-x**2), -1, 0.9999999, 0.0000001) = 3.1415610418530173 ~= pi
def arc_length(f, start = 0, end = 1, epsilon = 0.1):
    assert start + epsilon < end;
    
    i = start

    arcLen = 0
    
    while i <= end:
        arcLen += sqrt((f(i + epsilon) - f(i)) ** 2 + epsilon ** 2)
        i += epsilon
    
    return arcLen

