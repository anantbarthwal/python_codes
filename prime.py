x=int(15)
flag = 0
for num in range (2,x + 1):
    for num1 in range (2,int(num/2)):
        if num%num1 == 0:
           flag = flag + 1 
           break     
    if flag == 0:
        print(num,"is a prime number")
    flag=0
