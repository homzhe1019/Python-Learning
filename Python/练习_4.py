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
