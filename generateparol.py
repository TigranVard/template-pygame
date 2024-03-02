from random import randint
# for i in range(0,255):

#     symbol = chr(i)
#     if i % 3 == 0:
#         print(symbol)
#     else:
#         print(symbol, end=" ")

# password = ""
# for i in range(0,10):
#     password += chr(randint(65, 122))
#     if i % 10 == 0:
#         password += "_"

def GeneratePassword(max,sep):
    password = ""
    for i in range(0,max):
        password += chr(randint(33, 90))
        if i % 10 == 0:
            password += sep
    return password

pass1 = GeneratePassword(10,"---")
print(pass1)

print(GeneratePassword(20,"==="))

