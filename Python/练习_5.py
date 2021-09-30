# 练习5-1
phone = 'vivo'
print("Is phone == 'vivo'?I predict True.")
print(phone == 'vivo')

print("\nIs phone == 'oppo'?I predict False.")
print(phone == 'oppo')

# 练习5-2
print('\n练习')
fuhao = '?'
print(fuhao == '?')
print(fuhao == '.')

car = 'BMW'
print(car.lower() == 'bmw')

age_1 = 17
age_2 = 20
print(age_1 > 19 and age_2 > 22)
print(age_1 > 15 or age_2 > 22)

food = ['noodle', 'rice', 'ice_cream']
food_1 = 'rice'
food_2 = 'fruit'
if food_1 in food:
    print('We have rice')
if food_2 not in food:
    print("fruit already finish")

# 练习5-3
alien_colour = ['red']
if 'red' in alien_colour:
    print('You get 5 point.')

alien_colour = ['red']
if 'blue' in alien_colour:
    print('You get 5 point.')

# 练习5-4
alien_colour1 = ['green']
if 'green' in alien_colour1:
    print('You get 5 point.')
if 'green' not in alien_colour1:
    print('You grt 10 point.')

alien_colour1 = ['green']
if 'green' in alien_colour1:
    print('You get 5 point.')
else:
    print('You grt 10 point.')

# 练习5-5
alien_colour1 = ['green']
if 'green' in alien_colour1:
    print('Its a green alien')
    print('You get 5 point.')
elif 'yellow' in alien_colour1:
    print('Its a yellow alien')
    print('You get 10 point.')
else:
    print('Its a red alien.')
    print('You grt 15 point.')

# 练习5-6
age = 17
if age < 2:
    print('This is baby.')
elif age < 4:
    print('This is a young.')
elif age < 13:
    print('This is a child.')
elif age < 20:
    print('This is a teenager.')
elif age < 65:
    print('This is a adult.')
else:
    print('This is a elder.')

# 练习5-7
favorite_fruits = ['apple', 'orange', 'watermelon']
if 'apple' in favorite_fruits:
    print(f'You really like {favorite_fruits[0]}!')
if 'grape' in favorite_fruits:
    print(f'You really like {favorite_fruits}!')
if 'orange' in favorite_fruits:
    print(f'You really like {favorite_fruits[1]}!')
if 'pear' in favorite_fruits:
    print(f'You really like {favorite_fruits}!')
if 'watermelon' in favorite_fruits:
    print(f'You really like {favorite_fruits[2]}!')

# 练习5-8
names = ['admin', 'teoh', 'weerat', 'david', 'khoo']
for name in names:
    if name == 'admin':
        print('Hello admin,would you like to see s status report?')
    else:
        print(f'Hello {name},thank you for logging in again')

# 练习5-9
names = []
if names:
    for name in names:
        if name == 'admin':
            print('Hello admin,would you like to see s status report?')
        else:
            print(f'Hello {name},thank you for logging in again')
else:
    print('We need to find some users!')

# 练习5-10
current_users = ['david', 'xianze', 'teoh', 'khoo', 'weerat']
current_users1 = ['DAVID', 'XIANZE', 'TEOH', 'KHOO', 'WEERAT']
new_users = ['david', 'sunny', 'coolwei', 'khoo', 'jieying']
for new_user in new_users:
    if new_user in current_users:
        print('You need to type another name')
    else:
        print('This name can be use')

# 练习5-11
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
    if number == 1:
        print(f'{number}st')
    elif number == 2:
        print(f'{number}nd')
    elif number == 3:
        print(f'{number}rd')
    else:
        print(f'{number}th')

