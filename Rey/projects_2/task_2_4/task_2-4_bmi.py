weight = float(input("Введите вес (кг): "))
height = float(input("Введите рост (м): "))

bmi = weight / (height ** 2)
print("---Отчёт о состоянии здоровья---")
print(f"Рост:\t {height}\nВес:\t {weight}\n")
print(f"Индекс массы тела пациента: {bmi:.2f}")