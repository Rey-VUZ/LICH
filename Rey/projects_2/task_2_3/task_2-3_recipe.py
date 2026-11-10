name_of_the_culture_medium = input("Название питательной среды: ")
agar_concentration = input("Концентрация агара (%): ")
sterilization_temperature = input("Температура стерилизации: ")

with open("recipe.txt", "w", encoding="utf-8") as recipe:
    recipe.write(f"Название среды:\t {name_of_the_culture_medium}\n")
    recipe.write(f"Концентрация агара (%):\t {agar_concentration}\n")
    recipe.write(f"Температура стерилизации:\t {sterilization_temperature}\n")

print("Файл 'recipe.txt' успешно сформирован!")