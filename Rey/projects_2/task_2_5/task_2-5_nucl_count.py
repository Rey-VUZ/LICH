print("=== Анализ последовательности ДНК ===")
dna = input("Введите последовательность ДНК: ").upper()
# Подсчёт нуклеотидов
print("Подсчёт нуклеотидов:")
print(f"А: {dna.count("A")}")
print(f"Т: {dna.count("T")}")
print(f"G: {dna.count("G")}")
print(f"C: {dna.count("C")}")
print(f"Общая длина: {len(dna)} нуклеотидов")