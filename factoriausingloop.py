# 5 -> 5 * 4 * 3 * 2 * 1 
#num = 5
#fact = 1
#loop i in 5 - 1
#    fact = fact *i

num = int(input("enter any num"))
fac = 1
for i in range(num, 0, -1):
    fac = fac * i

print(fac)

