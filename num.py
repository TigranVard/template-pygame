import random 


zif1 = 0
zif = random.randint(0, 50)

while zif1 < 10:
    number = input()
    if number.isdigit():
        number = int(number)
        if number < zif:
            print("Число больше загаданного")
        elif number > zif:
            print("Число меньше загаданного")
        else:
            print(f"Вы угадали число - {zif}")
            break
        zif1 += 1
    else:
        print("Введено не число")
else:
    print(f"Число: {zif} так и не было угадано")

