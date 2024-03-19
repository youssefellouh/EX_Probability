# On lance un dé équilibré de 6 faces numérotées de 1 à 6 (1,
# 2, 3, 4, 5 et 6) 2 fois et on note le nombre obtenu de chaque lancement.
# On veut faire une simulation ainsi que calculer la
# probabilité d'obtention de la somme des 2 nombres égales à
# 6.




import random

def proba(nombre):
    compteur = 0
    for _ in range(nombre):
        l1 = random.randint(1,6)
        l2 = random.randint(1,6)
        # print("( T1 :", l1, ", T2 :", l2, ")")
        if(l1 + l2 == 6):
            compteur += 1
    return compteur / nombre

nombre = int(input("Donnez un nombre de tentative : "))
print("Probabilité :", proba(nombre))