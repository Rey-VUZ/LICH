volume_of_the_solution = float(input("введите нужный объем раствора (в мл): "))
mass_of_salt = volume_of_the_solution * 0.009
water_volume = volume_of_the_solution

with open("recipe.txt", "w", encoding="utf-8") as recipe:
    recipe.write("+" + "-" * 60 + "+")
    recipe.write(f"\nОТЧЕТ ПО ПРИГОТОВЛЕНИЮ:\n")
    recipe.write(f"Общий объем: {volume_of_the_solution} мл\n")
    recipe.write(f"Масса соли: {mass_of_salt} г\n")
    recipe.write(f"Объем воды: {water_volume} мл\n")