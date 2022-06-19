bad_grades = int(input())

left_bad_grades = 0
average_score = 0
tasks = 0
last_task_name = ''
current_task_name = input()

while not current_task_name == 'Enough':
    last_task_name = current_task_name
    score = int(input())

    if score <= 4:
        left_bad_grades += 1

    if left_bad_grades == bad_grades:
        break
    average_score += score
    tasks += 1

    current_task_name = input()

if left_bad_grades == bad_grades:
    print(f'You need a break, {bad_grades} poor grades.')
else:
    average_score = average_score / tasks
    print(f'Average score: {average_score:.2f}')
    print(f'Number of problems: {tasks}')
    print(f'Last problem: {last_task_name}')