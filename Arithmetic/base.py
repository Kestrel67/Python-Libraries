# don't forget : bin (0b...), hex (0x...) , oct(0o...), int('...', frombase) -> to decimal base

# alphabet = [str(i) for i in range(10)] + [chr(65 + i) for i in range(26)]
alphabet = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# extended_alphabet = [str(i) for i in range(10)] + [chr(65 + i) for i in range(26)] + [chr(97 + i) for i in range(26)]

# maximal representable base
maxbase = len(alphabet)

# display base identificator
baseID = True

# convert n in base 10 to another base
# n (int) base 10
def dec2base(n, tobase=16):

    n = int(n)

    assert 2 <= tobase <= maxbase

    # case q nul
    if n == 0:
        return 0

    # to base 10
    if tobase == 10:
        return n

    out = ""
    
    while n:
        n, remainder = divmod(n, tobase)
        
        out = alphabet[remainder] + out

    # base identificator
    if baseID:
        if tobase == 2:
            return '0b' + out
        elif tobase == 8:
            return '0o' + out
        elif tobase == 16:
            return '0x' + out

    return out

# convert n in a certain base to base 10
# n (int | str) frombase
def base2dec(n, frombase = 16):

    assert 2 <= frombase <= maxbase
    
    n = str(n)

    # from base 10
    if frombase == 10:
        return int(n)

    power = 0
    dec = 0

    for char in n[::-1]:
        dec += alphabet.index(char) * frombase ** power
        power += 1

    return dec

# convert n in base (frombase) to base (tobase) (stupid method)
def dummybase(n, frombase=2, tobase=16):
    return dec2base(base2dec(n, frombase), tobase)

# convert n in base (frombase) to base (tobase)
def base(n, frombase=2, tobase=16):

    assert 2 <= frombase <= maxbase
    assert 2 <= tobase <= maxbase

    if frombase == tobase:
        return n
    elif frombase == 10:
        return dec2base(n, tobase)
    elif tobase == 10:
        return base2dec(n, frombase)

    n = str(n)

    out = ""
    
    raise Exception('Error')

    return out
