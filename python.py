import random

n = int(input("donner nombre deteration"))
comp = 0
for i in range(n):
    x = random.randint(1, 6)
    y = random.randint(1, 6)

    if x + y == 6:
        comp += 1
res = comp / n
print(res)
