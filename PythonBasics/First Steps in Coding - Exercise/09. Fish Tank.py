length = int(input())
width = int(input())
height = int(input())
percentage_sand = float(input())

aquarium_volume = length * width * height / 1000
water_volume = aquarium_volume * (1 - percentage_sand / 100)

print(water_volume)