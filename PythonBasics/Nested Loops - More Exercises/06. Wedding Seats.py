last_sector = input()
rows_in_sector = int(input())
seats_on_odd_row = int(input())
seats_on_even_row = seats_on_odd_row + 2
counter = 0
for sector in range(ord('A'), ord(last_sector) + 1):
    for row in range(1, rows_in_sector + 1):
        if row % 2 == 0:
            seats = seats_on_even_row
        else:
            seats = seats_on_odd_row
        for seat in range(ord('a'), ord('a') + seats):
            print(chr(sector) + str(row) + chr(seat))
            counter += 1
    rows_in_sector += 1
print(counter)