def add():
    a = int(input("Enter value 1: "))
    b = int(input("Enter value 2: "))
    return a + b

print(add())

#Internally returns none
def voidAdd():
    a = int(input("Enter value 1: "))
    b = int(input("Enter value 2: "))
    print(a+b)
    
voidAdd()
print(voidAdd())

#Parameters
def add(a, b):
    return a+b
print(add(10, 10))

#Types of parameters
def add(a, b=6):
    return a+b
print(add(6))



    