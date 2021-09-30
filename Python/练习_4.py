# 练习4-1
pizzas = ['normal pizza', 'domino', 'tomato pizza']
for pizza in pizzas:
    print(pizza.title())
    print(f'I like {pizza.title()}.\n')
print('I really love pizza！')

# 练习4-2
animals = ['cat', 'dog', 'dolphin']
for animal in animals:
    print(animal.title())
    print(f'A {animal.title()} would make a great pet.\n')
print('Any of these animals would make a great pet')

# 练习4-3
for numbers in range(1, 21):
    print(numbers)

# 练习4-4
numbers = list(range(1, 1_000_000))
for numbers in range(1, 1_000_000):
    print(numbers)

# 练习4-5
digital = list(range(1, 1_000_000))
print(min(digital))
print(max(digital))
print(sum(digital))

# 练习4-6
odd_numbers = list(range(0, 20, 1))
for odd_numbers in range(0, 20, 1):
    print(odd_numbers)

# 练习4-7
numbers3 = []
for numbers3 in range(3, 30, 3):
    print(numbers3)

# 练习4-8
squares = []
for value in range(1, 11):
    squares.append(value**3)
print(squares)

# 练习4-9
squares = [value**3 for value in range(1, 11)]
print(squares)

# 练习4-10
fruit = ['Apple', 'Watermelon', 'Orange', 'Kiwi', 'Pear', 'Pineapple', 'Lemon']
print('The first three items in the list are:')
print(fruit[:3])

print('Three items from the middle of the list are:')
print(fruit[2:5])

print('The last  three items in the list are:')
print(fruit[4:])

# 练习4-11
my_pizzas = ['cheese pizza', 'mango pizza']
friend_pizzas = my_pizzas[:]

my_pizzas.append('normal pizza')
friend_pizzas.append('tomato pizza')

print('My favorite pizza are:')
for my_pizza in my_pizzas:
    print(my_pizza)

print("\nMy friend's favorite pizza are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)

# 练习4-12
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
for my_food in my_foods:
    print(my_food)

print("\nMy friend's favorite foods are:")
for friend_food in friend_foods:
    print(friend_food)

# 练习4-13
foods = ('rice', 'noodle', 'drink', 'soup', 'mee')
for food in foods:
    print(food)

foods = ('rice', 'noodle', 'water', 'soup', 'ice')
print('Modified dimensions:')
for food in foods:
    print(food)
