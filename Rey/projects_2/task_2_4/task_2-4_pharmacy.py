total_number_of_capsules_produced = int(input("Введите общее количество произведенных капсул: "))
capacity_of_a_single_package = int(input("Введите количество капсул в одной упаковке: "))

full_packages = total_number_of_capsules_produced//capacity_of_a_single_package
remaining_capsules = total_number_of_capsules_produced%capacity_of_a_single_package

print("---Отчёт фасовочного цеха---")
print(f"Полных упаковок:\t {full_packages}\nОстаток капсул:\t {remaining_capsules}")