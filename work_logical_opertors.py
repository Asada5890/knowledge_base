gender = input("Ваш пол (М или Ж): ")

while gender != "М" and gender != "Ж":
    print("Некорректное значение!")
    gender = input("Попробуйте еще раз: ")

age = int(input("Ваш возраст: "))
if (gender == "М" or gender == "Ж") and 18 <= age <= 27:
    print("Кандидант подходит")
else:
    print("Кандидант не подходит")
