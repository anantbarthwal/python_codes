# add, mul ,div ,sub

def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def mul(a,b):
    return a*b

def div(a,b):
    return a/b



def main():
    ch = int(input("press 1 for add \n 2 for sub \n 3 for mul \n 4 for div \n  press 0 to exit \n"))
    while ch!=0:
        a = int(input("Enter num1 value: "))
        b = int(input("Enter num2 value: "))
        if ch == 1:
            print(add(a,b))  
        elif ch == 2:
            print(sub(a,b))
        elif ch == 3:
            print(mul(a,b))
        else:
            print(div(a,b))
        ch = int(input("press 1 for add \n 2 for sub \n 3 for mul \n 4 for div \n  press 0 to exit \n"))

main()

    


