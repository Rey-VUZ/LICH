name_of_the_new_reagent = input("Название нового реактива: ")
amount_of_reagent = input("Количество реактива (целое число): ")

print(f"Реактив {name_of_the_new_reagent} поступил на склад в количестве {amount_of_reagent} шт")

f = open(r"C:\Users\Fazlizhanova_Elina\Documents\Rey\projects_2\task_2_2\inventory.txt", "w", encoding="utf-8")
print("Реактив", name_of_the_new_reagent, "поступил на склад в количестве", amount_of_reagent, "шт", file=f)