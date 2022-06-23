import math

days = int(input())
food = int(input())
dog_food_per_day = float(input())
cat_food_per_day = float(input())
turtle_food_per_day = float(input()) / 1000

food_needed = (dog_food_per_day + cat_food_per_day + turtle_food_per_day) * days

if food_needed <= food:
    food_left = food - food_needed
    print(f'{math.floor(food_left)} kilos of food left.')
else:
    food_needed = food_needed - food
    print(f'{math.ceil(food_needed)} more kilos of food are needed.')