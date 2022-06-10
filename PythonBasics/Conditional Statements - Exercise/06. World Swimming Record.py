world_record = float(input())
distance = float(input())
time_for_one_meter = float(input())

ivan_time = distance * time_for_one_meter
delay = distance // 15 * 12.5
ivan_time += delay

if ivan_time < world_record:
    print(f'Yes, he succeeded! The new world record is {ivan_time:.2f} seconds.')
else:
    print(f'No, he failed! He was {(ivan_time - world_record):.2f} seconds slower.')