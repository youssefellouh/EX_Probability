
# La variable aléatoire X suit une loi de Bernoulli de probabilité p, si X vaut 1 ou 0 avec les probabilités respectives p et 1-p. On a alors :
# E(X) = p, E(X2) = p2,
# V(X) = p(1 − p), o(X) = √p(1 − p)
from math import sqrt
def esperance(X, P) :
    E = 0
    for i in range(6) :
        E += X[i] * P[i]
    return E
def variance(X, P) :
    n = 0
    s = 0
    for i in X:
        n += 1
        s += (i - esperance(X, P)) ** 2
    return s/n

X = [1, 2, 3, 4, 5, 6]
P = [1/6, 1/6, 1/6, 1/6, 1/6, 1/6]
    
print("Esperance :", esperance(X, P))
print("Variance :", variance(X, P))
print("Écart-type :", sqrt(variance(X, P)))