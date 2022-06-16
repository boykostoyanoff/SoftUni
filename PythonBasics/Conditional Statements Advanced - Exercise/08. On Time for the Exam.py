exam_hour = int(input())
exam_minute = int(input())
arrive_hour = int(input())
arrive_minute = int(input())

exam_in_minute = exam_hour * 60 + exam_minute
arrive_in_minute = arrive_hour * 60 + arrive_minute

diff_time = exam_in_minute - arrive_in_minute

if diff_time < 0:
    print('Late')
elif 30 <= diff_time <= 0:
    print('On time')
elif diff_time <= 60:
    print('Early')
    arrive_hour = diff_time // 60
    arrive_minute = diff_time % 60
    print(f'{arrive_hour}:{arrive_minute:02} hours before the start')

