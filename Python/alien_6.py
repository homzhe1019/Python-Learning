alien_0 = {'color': 'green', 'point': 5}
print(alien_0['color'])
print(alien_0['point'])

alien_0 = {'color': 'green', 'point': 5}
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_0 = {}

alien_0['color'] = 'green'
alien_0['point'] = 5

print(alien_0)

alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}")

alien_0['color'] = 'yellow'
print(f"The alien is now {alien_0['color']}")

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position:{alien_0['x_position']}")

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position:{alien_0['x_position']}")

alien_0 = {'color': 'green', 'point': 5}
print(alien_0)
del alien_0['point']
print(alien_0)


