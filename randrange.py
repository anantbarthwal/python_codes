import random 
import math  
# Using randrange() to generate numbers from 0-100 
print ("Random number from 0-100 is : ",end="") 
print (random.randrange(100)) 
  
# Using randrange() to generate numbers from 50-100 
print ("Random number from 50-100 is : ",end="") 
print (random.randrange(50,100)) 
  
# Using randrange() to generate numbers from 50-100 
# skipping 5 
print ("Random number from 50-100 skip 5 is : ",end="") 
print (random.randrange(50,100,5)) 

def power(n):
    if n==0:
        return 1;
    else:
        return n*power(n-1);

print(power(5)) 