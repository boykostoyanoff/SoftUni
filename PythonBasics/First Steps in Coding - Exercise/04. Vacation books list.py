number_of_pages = int(input())
pages_per_hour = int(input())
day_for_read = int(input())

hours_per_day = number_of_pages // pages_per_hour // day_for_read

print(hours_per_day)