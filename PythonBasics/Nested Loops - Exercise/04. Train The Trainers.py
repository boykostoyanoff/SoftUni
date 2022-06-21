juri = int(input())
all_grades = 0
sum_grades = 0
while True:
    current_assessment_grades_sum = 0
    assessment_name = input()

    if assessment_name == 'Finish':
        current_grade = sum_grades / all_grades
        print(f"Student's final assessment is {current_grade:.2f}.")
        break

    for grade in range(juri):
        current_assessment_grades_sum += float(input())
    sum_grades += current_assessment_grades_sum
    all_grades += juri
    current_grade = current_assessment_grades_sum / juri
    print(f'{assessment_name} - {current_grade:.2f}.')