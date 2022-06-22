work_day_play = 63
free_day_play = 127
days_in_year = 365
play_minutes_normative = 30000

free_days = int(input())

minutes_for_play = free_day_play * free_days + (days_in_year - free_days) * work_day_play

if minutes_for_play <= play_minutes_normative:
    minutes_for_play = play_minutes_normative - minutes_for_play
    H = minutes_for_play // 60
    M = minutes_for_play % 60
    print('Tom sleeps well')
    print(f'{H} hours and {M} minutes less for play')
else:
    minutes_for_play = minutes_for_play - play_minutes_normative
    H = minutes_for_play // 60
    M = minutes_for_play % 60
    print('Tom will run away')
    print(f'{H} hours and {M} minutes more for play')