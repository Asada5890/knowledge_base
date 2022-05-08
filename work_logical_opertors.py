gender = input("Ваш пол (М или Ж): ").strip().upper() 

# while gender != "М" and gender != "Ж":
while gender not in ("М", "Ж", ""):
    print("Некорректное значение!")
    gender = input("Попробуйте еще раз: ")

age = int(input("Ваш возраст: "))
if (gender == "М" or gender == "Ж") and 18 <= age <= 27:
    print("Кандидант подходит")
else:
    print("Кандидант не подходит")
