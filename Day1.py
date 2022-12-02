def orderedCalories(input):
    file = open(input, 'r')
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

    ordered = sorted(food.keys())
    return ordered

def top3(input):
    listOfCalories = orderedCalories(input)
    return listOfCalories[-3:]

def main():
        # function calling
    print("These are the top 3 calories that 3 different elfs carry: ",top3('Day1Data.txt'))
 
 
# main function calling
if __name__ == "__main__":
    main()
