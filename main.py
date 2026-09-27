import random

while True:
    print("Выбери сложность:")
    print("1 - Легкая (1-10)")
    print("2 - Средняя (1-100)")
    print("3 - Сложная (1-1000)")

    dif = input("Твой выбор: ")

    if dif == '1':
        k = 3
        r = random.randint(1, 10)
        text = "Введи число от 1 до 10: "
        print(f"Вы выбрали легкую сложность, у вас {k} попытки")
        break  # Выходим из цикла выбора сложности
    elif dif == '2':
        k = 10
        r = random.randint(1, 100)
        text = "Введи число от 1 до 100: "
        print("Вы выбрали среднюю сложность, у вас", k, "попытки")
        break
    elif dif == '3':
        k = 15
        r = random.randint(1, 1000)
        text = "Введи число от 1 до 1000: "
        print("Вы выбрали сложную сложность, у вас", k, "попытки")
        break
    else:
        print("Такой сложности нет!")


while k!=0:
    try:
        a = int(input(text))

        if r == a:
            print("Вы победили!")
            break
        elif r > a:
            print("Загаданное число больше")
        else:
            print("Загаданное число меньше")

        k -= 1
        print("Осталось попыток: ", k,"")
    except:
        print('Такого числа нет!')