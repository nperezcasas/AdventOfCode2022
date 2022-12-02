
file = open('Day1Data.txt', 'r')

curr_elf = 0
temp = 0
food = {}
for each in file:
    if each != '\n':
        temp += int(each)
    else:
        curr_elf += 1
        if temp not in food:
            food[temp] = [curr_elf]
        else:
            food[temp].append(curr_elf)
        temp = 0
curr_elf += 1
if temp not in food:
    food[temp] = [curr_elf]
else:
    food[temp].append(curr_elf)

calories = max(food.keys())
print(calories)
print(food[calories])
del food[calories]

calories = max(food.keys())
print(calories)
print(food[calories])
del food[calories]

calories = max(food.keys())
print(calories)
print(food[calories])
del food[calories]
