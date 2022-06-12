product = input()
product_type = 'unknown'
fruits = ['banana', 'apple', 'kiwi', 'cherry', 'lemon', 'grapes']
vegetables = ['tomato', 'cucumber', 'pepper', 'carrot']

if product in fruits:
    product_type = 'fruit'
elif product in vegetables:
    product_type = 'vegetable'

print(product_type)
