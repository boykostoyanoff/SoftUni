student_name = input()
bad_grades = 0
grades_sum = 0
student_class = 1

while True:
    current_grade = float(input())

    if current_grade < 4:
        bad_grades += 1
        if bad_grades > 1:
            print(f'{student_name} has been excluded at {student_class} grade')
            break
    else:
        student_class += 1
        grades_sum += current_grade

    if student_class == 13:
        average_grade = grades_sum / 12
        print(f'{student_name} graduated. Average grade: {average_grade:.2f}')
        break
