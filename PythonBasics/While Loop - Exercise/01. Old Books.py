searched_book_name = input()
book_passed = 0

while True:
    current_book = input()
    if current_book == searched_book_name:
        print(f'You checked {book_passed} books and found it.')
        break
    elif current_book == 'No More Books':
        print('The book you search is not here!')
        print(f'You checked {book_passed} books.')
        break

    book_passed += 1