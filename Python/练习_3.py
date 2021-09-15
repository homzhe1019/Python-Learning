# 练习3-1
names = ['teoh','tei','weerat','khoo']
print(names[0])
print(names[1])
print(names[2])
print(names[3])

# 练习3-2
message = f"Good morning {names[0]},{names[1]},{names[2]},{names[3]}"
print(message)

# 练习3-3
transport = ['car', 'motocycles', 'bus']
message = f"I would like to own a {transport[0]}"
print(message)

# 练习3-4
friend = ['teoh','weerat','tei']
message = f'Do you want to eat dinner with me,{friend[0]},{friend[1]},{friend[2]}'
print(message)

# 练习3-5
friend = ['teoh','weerat','tei']
message = f'Do you want to eat dinner with me,{friend[0]},{friend[1]},{friend[2]}'
print(message)

print(f'sorry,{friend[1]} will absent')
friend[1] = 'khoo'
message = f'Do you want to eat dinner with me,{friend[0]},{friend[1]},{friend[2]}'
print(message)

# 练习3-6
friend = ['teoh','weerat','tei']
message = f'Do you want to eat dinner with me,{friend[0]},{friend[1]},{friend[2]}'
print(message)

print(f'sorry,{friend[1]} will absent')
friend[1] = 'khoo'
message = f'Do you want to eat dinner with me,{friend[0]},{friend[1]},{friend[2]}'
print(message)

print('I found a large table')
friend.insert(0,'jiaqi')
friend.insert(2,'liming')
friend.append('david')
message = f'Do you want to eat dinner with me,{friend[0]},{friend[1]},{friend[2]},{friend[3]},{friend[4]},{friend[5]}'
print(message)

# 练习3-7
friend = ['teoh','weerat','tei']
message = f'Do you want to eat dinner with me,{friend[0]},{friend[1]},{friend[2]}'
print(message)

print(f'sorry,{friend[1]} will absent')
friend[1] = 'khoo'
message = f'Do you want to eat dinner with me,{friend[0]},{friend[1]},{friend[2]}'
print(message)

print('I found a large table')
friend.insert(0, 'jiaqi')
friend.insert(2, 'liming')
friend.append('david')
message = f'Do you want to eat dinner with me,{friend[0]},{friend[1]},{friend[2]},{friend[3]},{friend[4]},{friend[5]}'
print(message)

print('Sorry,I only can invite 2 friend')
popped_friend = friend.pop(1)
print(f'{popped_friend} I am sorry,I cannot invite you')
popped_friend = friend.pop(2)
print(f'{popped_friend} I am sorry,I cannot invite you')
popped_friends = friend.pop(2)
print(f'{popped_friends} I am sorry,I cannot invite you')
popped_friends = friend.pop(2)
print(f'{popped_friends} I am sorry,I cannot invite you')
print(f'You still in invite list,{friend[0]}')
print(f'You still in invite list,{friend[1]}')
del friend[0]
del friend[0]
print(friend)

# 练习3-8
travel = ["Japan", "China", "Korea", "Tokyo", "Beijing"]
print(travel)
print(sorted(travel))
print(travel)
print(sorted(travel, reverse=True))
print(travel)
travel.reverse()
print(travel)
travel.reverse()
print(travel)
travel.sort()
print(travel)
travel.sort(reverse=True)
print(travel)

# 练习3-9
friend = ['teoh', 'weerat', 'tei']
print(len(friend))

# 练习3-9
negeri  = ['kedah', 'perlis', 'penang','johor']
print(f'I life in {negeri[0]}')
