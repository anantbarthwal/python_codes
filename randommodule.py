import random

Ar = [ 20, 30, 40, 50, 60, 70]
FROM =random.randint(1,3)  #1
TO= random.randint(2,4) #3
for k in range (FROM, TO+1):  #1 ,4
    print(Ar[k], end='#')
