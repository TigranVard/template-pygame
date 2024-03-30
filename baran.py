import math

def formula(a,b,c):
    x1 = (math.sqrt(a+b**2)*(a**2+b**2))/(4*a*c)
    if formula == 0:
        print("НА НОЛЬ ДЕЛИТЬ НЕЛЬЗЯ")
    print(x1)
    return x1

# formula(2,4,6)
# formula(20,40,60)
# formula(200,400,600)
# formula(2000,4000,6000)
# formula(20000,40000,60000)


# a = int(input("a "))
# b = int(input("b "))
# c = int(input("c "))

# a = 5
# b = 8
# c = 3

# x1 = (math.sqrt(a+b**2)*(a**2+b**2))/(4*a*c)
# print(x1)

