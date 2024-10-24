from numpy.random import permutation
from numpy.random import randint
#from numpy.random import roll
from numpy import base_repr

def ternary(x):
    return base_repr(x,3).zfill(3)

def parse(x):
    return int(x,3)

def rotate(s, n):
    return s[n:] + s[:n]

def random_permutation(n):
    return list(permutation(n))

def random_ternary_string():
    s = ""
    for i in range(27):
        s += str(randint(3))
    return s

def display(s):
    for i in range(len(s)):
        match s[i]:
            case "0": print("O ", end = "")
            case "1": print("| ", end = "")
            case "2": print("2 ", end = "")
    print()



def inverse(f):
    g = [0]*27
    for i in range(len(f)):
        g[i] =f.index(i)
    return g

def permute(s,f):
    t = ""
    for i in range(len(s)):
        t += s[f.index(i)]
    return t

def encode_row(x,f):
    d = dec_from_bin(x)
    y = []
    for i in range(len(d)):
        y.append(f[d[i]])
    y = bin_from_dec(y)
    y = rotate(y, y.count(1))
    return y

def advance(x,f):
    y = ""
    s = 0
    for i in range(0,27,3):
        c = parse(x[i:i+3])
        s += c
        y += ternary(f[c])
    return y

def code(s):
    c = 0
    for i in range(len(s)):
        c += parse(s[i])
    return c % 3

def encode_block(x,f,g, show=False):
    y = x
    for i in range(len(f)):
        y = advance(y,f)
        y = permute(y,g)
        y = rotate(y,code(y))
        f = rotate(f,1)
        g = rotate(g,1)
        if show:
            display(y)
    return y

def decode_block(x,f,g,show=False):
    y = x
    for i in range(len(f)):
        y = rotate(y,-code(y))
        f = rotate(f,-1)
        g = rotate(g,-1)
        y = permute(y,inverse(g))
        y = advance(y,inverse(f))
        if show:
            display(y)
        
    return y

f = random_permutation(27)
g = random_permutation(27)
print("f = ",f )
print("g = ",g )
for i in range(1):
    x = random_ternary_string()
    y = encode_block(x,f,g, show=True)
    print()
    z = decode_block(y,f,g, show=True)
    print()
    display(x)
    display(y)
    display(z)
    print(x == z, "\n")


