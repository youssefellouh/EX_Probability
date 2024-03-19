# 1. Écrire une fonction binomiale (n,p,k) qui
# retourne la valeur de P(X = k) pour une variable aléatoire X suivant une loi
# binomiale B(n,p).
# 2. Écrire une fonction binomiale_inf(n,p,k) qui retourne la valeur P(X ≤ k) pour une
# variable aléatoire suivant une loi
# binomiale B(n,p).
# 3. Écrire une fonction binomiale_sup (n,p,k)
# qui retourne la valeur P(X ≥ k), pour
# une variable aléatoire suivant une loi
# binomiale B(n,p).


from math import comb

def binomiale(n, p, k) :
    return comb(n, k) * (p ** k) * ((1 - p) ** (n - k))

def binomiale_inf(n, p, k) :
    sum = 0
    for i in range(k + 1) :
        sum += binomiale(n, p, i)
    return sum

def binomiale_sup(n, p, k) :
    return 1 - binomiale_inf(n, p, k-1)

print("Binomiale :", binomiale(10, 1/2, 2))
print("Binomiale (X <= k) :", binomiale_inf(10, 1/2, 2))
print("Binomiale (X >= k) :", binomiale_sup(10, 1/2, 2))