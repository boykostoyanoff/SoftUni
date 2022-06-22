student_tickets = 0
standard_tickets = 0
kids_tickets = 0

while True:
    film_name = input()
    if film_name == 'Finish':
        break

    free_seats = int(input())
    current_student_tickets = 0
    current_kids_tickets = 0
    current_standard_tickets = 0

    for i in range(free_seats):
        ticket_type = input()
        if ticket_type == 'End':
            break
        elif ticket_type == 'student':
            current_student_tickets += 1
        elif ticket_type == 'kid':
            current_kids_tickets += 1
        elif ticket_type == 'standard':
            current_standard_tickets += 1

    standard_tickets += current_standard_tickets
    student_tickets += current_student_tickets
    kids_tickets += current_kids_tickets
    all_tickets = current_kids_tickets + current_student_tickets + current_standard_tickets
    print(f'{film_name} - {(all_tickets / free_seats * 100):.2f}% full.')

all_tickets = student_tickets + standard_tickets + kids_tickets
print(f'Total tickets: {all_tickets}')

print(f'{(student_tickets / all_tickets * 100):.2f}% student tickets.')
print(f'{(standard_tickets / all_tickets * 100):.2f}% standard tickets.')
print(f'{(kids_tickets / all_tickets * 100):.2f}% kids tickets.')