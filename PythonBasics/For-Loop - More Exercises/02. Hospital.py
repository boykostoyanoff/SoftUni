period = int(input())
treated_patients = 0
untreated_patients = 0
doctors = 7

for day in range(1, period + 1):
    if day % 3 == 0:
        if untreated_patients > treated_patients:
            doctors += 1
    patients = int(input())
    