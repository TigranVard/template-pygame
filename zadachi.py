# for i in range(1, 101):
#     print(i, end=' ')


# a = 1
# b = 10

# for i in range(a, b):
#     print(i, end=' ')

# for i in range(1, 102):
#     if i % 3 ==0:
#         print(i)

# s = 0
# while True:
#     n = int(input("Введите число"))
#     if n == 0:
#         break
#     print("вы ввели число", n)
#     if n % 3 == 0 or n % 4 == 0 or n % 6 ==0:
#         s = s + n
# print(s)

pi = 3

a = 2
for i in range(1,16):
    
    if i%2 == 0:
        pi = pi - 4/(a*(a+1)*(a+2))
    else:
        pi = pi + 4/(a*(a+1)*(a+2))

    a += 2
print(pi)
