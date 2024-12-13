import random

mylist = list(range(10))

for i in range(1, 10, 1):
    mylist[i] = random.randrange(10)
    print(mylist[i])

mojiretu = ""

for h in range(1, 10, 1):
    mojiretu += str(mylist[h])

mojiretu = int(mojiretu)
mojiretu += 1
print (mojiretu)
