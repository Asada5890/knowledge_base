print("Добро пожаловать в программу 'Умножение на 2")
choice1 = input("Введите 'Да', чтобы начать: ")
choice = choice1.upper()
while True:
    if choice == "ДА":
        break
    else:
        choice = input("Введите 'Да', чтобы начать: ")
num = int(input("Какое число умножить: "))
print("2 x", num, "=", num *2)