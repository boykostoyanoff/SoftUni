video_card_price = 250
processor_price = 0.35
ram_price = 0.10

budged = float(input())
video_card_count = int(input())
processor_count = int(input())
ram_count = int(input())

total_price = video_card_price * video_card_count
total_price += total_price * (processor_price * processor_count + ram_count * ram_price)
if video_card_count > processor_count:
    total_price -= total_price * 0.15

if budged - total_price >= 0:
    print(f'You have {(budged - total_price):.2f} leva left!')
else:
    print(f'Not enough money! You need {(total_price - budged):.2f} leva more!')

