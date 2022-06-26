students_count = int(input())
students_over_5 = 0
students_over_4 = 0
students_over_3 = 0
students_over_2 = 0
grades_sum = 0

for _ in range(students_count):
    current_student_grade = float(input())
    grades_sum += current_student_grade
    if current_student_grade < 3:
        students_over_2 += 1
    elif current_student_grade < 4:
        students_over_3 += 1
    elif current_student_grade < 5:
        students_over_4 += 1
    elif current_student_grade <= 6:
        students_over_5 += 1

result = students_over_5 / students_count * 100
print(f'Top students: {result:.2f}%')
result = students_over_4 / students_count * 100
print(f'Between 4.00 and 4.99: {result:.2f}%')
result = students_over_3 / students_count * 100
print(f'Between 3.00 and 3.99: {result:.2f}%')
result = students_over_2 / students_count * 100
print(f'Fail: {result:.2f}%')
result = grades_sum / students_count
print(f'Average: {result:.2f}')