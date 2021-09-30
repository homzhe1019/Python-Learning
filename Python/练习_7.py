# 练习7-1
car = input('What car you want.')
print(f'Lets me see if i can find you a {car}')

# 练习7-2
place = input('How many people?')
place = int(place)

if place > 8:
    print('The place was full')
else:
    print('Have some place')

# 练习7-3
number = input('Enter a number, I will tell you if its can multiple full by 10.')
number = int(number)

if number % 10 == 0:
    print(f'The number can multiple full by 10')
else:
    print(f'\nThe number cannot multiple full by10 ')

# 练习7-4
pizza = 'Enter the food wanted in pizza'
pizza += 'Enter quit after finish'

while True:
    pizza = input(pizza)

    if pizza == 'quit':
        break
    else:
        print(f'we will add {pizza} in pizza.')

# 练习7-5
# 不會


# 练习7-6
pizza = 'Enter the food wanted in pizza'
pizza += 'Enter quit after finish'

while True:
    pizza = input(pizza)

    if pizza == 'quit':
        break
    else:
        print(f'we will add {pizza} in pizza.')

pizza = 'Enter the food wanted in pizza'
pizza += 'Enter quit after finish'

active = True
while active:
    pizza = input(pizza)

    if pizza == 'quit':
        active = False
    else:
        print(f'we will add {pizza} in pizza.')

pizza = 'Enter the food wanted in pizza'
pizza += 'Enter quit after finish'
msg = ""
while msg != 'quit':
    msg = input(f'I will add {msg}')

    if msg == 'quit':
        print(msg)

# 還有7-5的但是不會


# 练习7-7
x = 1
while x <= 5:
    print(x)

