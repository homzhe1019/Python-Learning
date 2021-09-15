motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
motorcycles.append('ducati')
print(motorcycles)

motorcycles = ['honda','yamaha','suzuki']
motorcycles.insert(0,'ducati')
print(motorcycles)

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

del motorcycles[1]
print(motorcycles)

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
popped_motorcycles = motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)

motorcycles = ['honda','yamaha','suzuki']
last_owner = motorcycles.pop()
print(f'The last motorcycles I owned was a {last_owner.title()}.')

motorcycles = ['honda','yamaha','suzuki']
first_owner = motorcycles.pop(0)
print(f'The first motorcycles I owned was a {first_owner.title()}.')

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
motorcycles.remove('yamaha')
print(motorcycles)

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)
too_expensive = 'yamaha'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f'\nA {too_expensive} is too expensive for me.')

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles[2])

