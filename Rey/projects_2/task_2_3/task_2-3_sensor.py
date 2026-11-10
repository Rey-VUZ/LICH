operator_name = input("Введите имя оператора: ")
pressure_sensor_reading = input("Введите текущее значение давления (Па): ")

with open("sensor_log.txt", "w", encoding="utf-8") as testimony:
    testimony.write(f"Имя оператора:\t {operator_name}\n")
    testimony.write(f"Текущее значение давления (Па)::\t {pressure_sensor_reading}\n")

print("Данные успешно сохранены в sensor_log.txt")