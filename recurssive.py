#recursssive function is a function which calls itself
"""
a=int(input("enter a number= "))
res=1
for x in range(1,a+1):
    
    res=res*x

print("res=",res)
"""
def fact(num):
    if num==0:
        return 1
    else:
        return num*fact(num-1)
num=int(input("enter anynumber= "))
print("factorial of ",num,"=",fact(num))  
#print("fact sum",fact(5)+fact(4))   


"""print(pow(2,3))   

def power(n, s): #2,3
    if s== 0:
        return 1
    else:
        return n* power(n,s-1)  #2*4  #2*2  #2*1

print( power(2,3))

  """                                                                      