exam_hour = int(input())
exam_minute = int(input())
arrive_hour = int(input())
arrive_minute = int(input())

exam_in_minute = exam_hour * 60 + exam_minute
arrive_in_minute = arrive_hour * 60 + arrive_minute

diff_time = exam_in_minute - arrive_in_minute

if diff_time < 0:
    print('Late')
elif 0 <= diff_time <= 30:
    print('On time')
elif diff_time > 30:
    print('Early')


if diff_time <= -60:
    print(f'{(diff_time * -1) // 60}:{(diff_time * -1 % 60):02} hours after the start')
elif -60 < diff_time < 0:
    print(f'{diff_time * -1} minutes after the start')
elif 0 <= diff_time < 60:
    print(f'{diff_time} minutes before the start')
elif diff_time >= 60:
    print(f'{(diff_time // 60)}:{(diff_time % 60):02} hours before the start')
