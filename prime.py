x=15
flag = 0
for num in range (2,x + 1):
    if (num == 2):
        print("2 is a prime number")
        continue
    for num1 in range (2,num):
        if num%num1 == 0:
           flag = flag + 1      
    if flag == 0:
        print(num,"is a prime number")
    flag=0
