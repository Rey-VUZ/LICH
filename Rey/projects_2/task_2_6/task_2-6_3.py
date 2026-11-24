donor_blood_type = input("Введите группу крови донора (I, II, III, IV): ").strip().upper()
patient_blood_type = input("Введите группу крови пациента (I, II, III, IV): ").strip().upper()

if donor_blood_type == patient_blood_type or donor_blood_type == "I":
    print("Группа крови донора подходит для переливания")
else:
    print("Группа крови донора не подходит для переливания")
