first_player_time = int(input())
second_player_time = int(input())
third_player_time = int(input())

total_time = first_player_time + second_player_time + third_player_time

seconds = total_time % 60
minutes = total_time // 60

if seconds < 10:
    print(f'{minutes}:0{seconds}')
else:
    print(f'{minutes}:{seconds}')