def futureValue(i, n , p):
    return p * (1 + i) ** n

def PresentValue(i, n, f):
    factor = 1/(1+i)**n
    return f*factor