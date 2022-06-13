budged = float(input())
season = input()
location = ''

where_to_rest = 'Camp' if season == 'summer' else 'Hotel'

if budged <= 100:
    location = 'Bulgaria'
    budged *= 0.30 if season == 'summer' else 0.70
elif budged <= 1000:
    location = 'Balkans'
    budged *= 0.40 if season == 'summer' else 0.80
else:
    where_to_rest = 'Hotel'
    location = 'Europe'
    budged *= 0.90

print(f'Somewhere in {location}')
print(f'{where_to_rest} - {budged:.2f}')