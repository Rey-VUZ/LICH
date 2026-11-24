mass_of_proteins = float(input("Введите Массу белков в продукте (г): "))
mass_of_fats = float(input("Введите Массу жиров в продукте (г): "))
mass_of_carbohydrates = float(input("Введите Массу углеводов в продукте (г): "))
caloric_content_of_a_product = mass_of_proteins*4+ mass_of_fats*9+ mass_of_carbohydrates*4

print(f"Калллорийность продукта: {mass_of_proteins}*4+ {mass_of_fats}*9+ {mass_of_carbohydrates}*4 = {caloric_content_of_a_product}")
