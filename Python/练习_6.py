# 练习6-1
Teoh = {'first_name': 'TEOH', 'last_name': 'ZHIQI', 'age': '15', 'city': 'KEDAH'}
print(Teoh['first_name'])
print(Teoh['last_name'])
print(Teoh['age'])
print(Teoh['city'])

# 练习6-2
numbers = {
    'teoh': '4',
    'tei': '8',
    'khoo': '5',
    'weerat': '6',
    'david': '3'
    }

number1 = numbers['teoh']
number2 = numbers['tei']
number3 = numbers['khoo']
number4 = numbers['weerat']
number5 = numbers['david']

print(f'teoh favorite number is {number1}.')
print(f'tei favorite number is {number2}.')
print(f'khoo favorite number is {number3}.')
print(f'weerat favorite number is {number4}.')
print(f'david favorite number is {number5}.')

# 练习6-3
python_learn = {
    '變量和簡單數據': 'print代碼',
    '列表簡介': '添加修改刪除列表中的元素',
    '操作列表': 'for range',
    'if語句': 'if elif else',
    '詞典': '儲存詞典',
    }

# 练习6-4
python_learning = {
    '變量和簡單數據': 'print代碼',
    '列表簡介': '添加修改刪除列表中的元素',
    '操作列表': 'for range',
    'if語句': 'if elif else',
    '詞典': '儲存詞典',
    'sorted()': 'abc順序',
    'del': '刪除',
    'get()': '訪問',
    'key,value': 'a：b 選擇',
    'items()': '歷遍詞典',
    }

for key, value in python_learning.items():
    print(f'\n{key}')
    print(f'{value}')

# 练习6-5

river = {
    'south china sea': 'china',
    'melaka river': 'malaysia',
    'indian ocean': 'indian',
    }

for key, value in river.items():
    print(f'The {key} through {value}')

for rivers in river.keys():
    print(rivers)
for nation in river.values():
    print(nation)

# 练习6-6
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

people = ['jen', 'sarah', 'teoh', 'david']
for name in favorite_languages.keys():
    if name in people:
        print(f'Thank for your join,{name}')
if 'teoh' not in favorite_languages.keys():
    print(f'Please join in as soon as possible,teoh')
if 'david' not in favorite_languages.keys():
    print(f'Please join in as soon as possible,david')

# 练习6-7
Teoh = {'first_name': 'TEOH', 'last_name': 'ZHIQI', 'age': '15', 'city': 'KEDAH'}
weerat = {'first_name': 'TA', 'last_name': 'WEERAT', 'age': '15', 'city': 'KEDAH'}
david = {'first_name': 'TAN', 'last_name': 'DAVID', 'age': '15', 'city': 'KEDAH'}

peoples = [Teoh, weerat, david]
for people in peoples:
    print(people)

# 练习6-8
cat = {'type': 'land', 'host': 'khoo'}
dog = {'type': 'land', 'host': 'teoh'}
fish = {'type': 'water', 'host': 'david'}

pets = [cat, dog, fish]
for pet in pets:
    print(pet)

# 练习6-9
favorite_places = {
    'teoh': ['penang', 'kedah'],
    'weerat': ['kelantan', 'thailand'],
    'khoo': ['perak', 'perlis'],
    }
for name, places in favorite_places.items():
    print(f"\n{name.title()} favorite place are:")
    for place in places:
        print(place)

# 练习6-10
numbers = {
    'teoh': ['4', '5'],
    'tei': ['8', '1'],
    'khoo': ['5', '3'],
    'weerat': ['6', '1'],
    'david': ['3', '2']
    }

for name, numbers in numbers.items():
    print(f"\n{name.title()} favorite numbers are:")
    for number in numbers:
        print(number)

# 练习6-11
cities = {
    'beijing': {
        'country': 'china',
        'population': '2170m',
    },
    'kedah': {
        'country': 'malaysia',
        'population': '216m',
    },
    'tokyo': {
        'country': 'jepan',
        'population': '1350m',
    },

}
for city, message in cities.items():
    print(f'\nCity:{city}')
    country = message['country']
    population = message['population']
    print(f'The country is: {country}')
    print(f'The population is:{population}')

# 练习6-12
for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']}{user_info['last']}"
    location = user_info['location']

    print(f"\tFull name: {full_name.title()}")
    print(f"\tlocation: {location.title()}")




