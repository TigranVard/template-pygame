a = ""
WhishList = []
while a != "0":
    a = input("\nчто хочешь?! 0 = свалить нахэр\n")
    if a != "0":
        WhishList.append(a)

print("Добавлено в корзину\n", WhishList)
# print(f"1.{WhishList[0]}")
# print(f"2.{WhishList[1]}")
# print(f"3.{WhishList[2]}")
# print(f"4.{WhishList[3]}")

def printlist(a):
    for i in range(0,len(a)):
        print(f"{i+1}. {a[i]}")

printlist(WhishList)

for i in range(0,10):
    removeIndex = int(input("Введите номер товара для автоматической оплаты: "))
    WhishList.pop(removeIndex-1)

printlist(WhishList)