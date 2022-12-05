def craters(input):
    file = open(input, 'r')

    # Hardcoding the initial 9 stacks for simplicity.
    """
        [H]         [D]     [P]        
    [W] [B]         [C] [Z] [D]        
    [T] [J]     [T] [J] [D] [J]        
    [H] [Z]     [H] [H] [W] [S]     [M]
    [P] [F] [R] [P] [Z] [F] [W]     [F]
    [J] [V] [T] [N] [F] [G] [Z] [S] [S]
    [C] [R] [P] [S] [V] [M] [V] [D] [Z]
    [F] [G] [H] [Z] [N] [P] [M] [N] [D]
    1   2   3   4   5   6   7   8   9 
    """
    stacks = {
    1 : ["F", "C", "J", "P", "H", "T", "W"],
    2 : ["G", "R", "V", "F", "Z", "J", "B", "H"],
    3 : ["H", "P", "T", "R"],
    4 : ["Z", "S", "N", "P", "H", "T"],
    5 : ["N", "V", "F", "Z", "H", "J", "C", "D"],
    6 : ["P", "M", "G", "F", "W", "D", "Z"],
    7 : ["M", "V", "Z", "W", "S", "J", "D", "P"],
    8 : ["N", "D", "S"],
    9 : ["D", "Z", "S", "F", "M"]}

    for each in file:
        numbers = ""
        for char in each:
            if char.isnumeric(): 
                #Putting all the numeric values in a string, that will be 3/4 char. 
                # Since there's only 9 stacks the last two values will be the single digits.
                numbers += str(char)
        toStack = int(numbers[-1])
        numbers = numbers[:-1]
        fromStack = int(numbers[-1])
        numbers = int(numbers[:-1])

        i = 0
        while i < numbers:
            stacks[toStack].append(stacks[fromStack].pop())
            i += 1
    tops = ""
    for i in range(1,10):
        tops += str(stacks[i].pop())
    return tops

def CrateMover9001(input):
    file = open(input, 'r')

    # Hardcoding the initial 9 stacks for simplicity.
    """
        [H]         [D]     [P]        
    [W] [B]         [C] [Z] [D]        
    [T] [J]     [T] [J] [D] [J]        
    [H] [Z]     [H] [H] [W] [S]     [M]
    [P] [F] [R] [P] [Z] [F] [W]     [F]
    [J] [V] [T] [N] [F] [G] [Z] [S] [S]
    [C] [R] [P] [S] [V] [M] [V] [D] [Z]
    [F] [G] [H] [Z] [N] [P] [M] [N] [D]
    1   2   3   4   5   6   7   8   9 
    """
    stacks = {
    1 : ["F", "C", "J", "P", "H", "T", "W"],
    2 : ["G", "R", "V", "F", "Z", "J", "B", "H"],
    3 : ["H", "P", "T", "R"],
    4 : ["Z", "S", "N", "P", "H", "T"],
    5 : ["N", "V", "F", "Z", "H", "J", "C", "D"],
    6 : ["P", "M", "G", "F", "W", "D", "Z"],
    7 : ["M", "V", "Z", "W", "S", "J", "D", "P"],
    8 : ["N", "D", "S"],
    9 : ["D", "Z", "S", "F", "M"]}


    for each in file:
        numbers = ""
        temp = []
        for char in each:
            if char.isnumeric(): 
                #Putting all the numeric values in a string, that will be 3/4 char. 
                # Since there's only 9 stacks the last two values will be the single digits.
                numbers += str(char)
        toStack = int(numbers[-1])
        numbers = numbers[:-1]
        fromStack = int(numbers[-1])
        numbers = int(numbers[:-1])

        i = 0
        
        while i < numbers:
            temp.append(stacks[fromStack].pop())
            i += 1

        while len(temp) != 0:
            stacks[toStack].append(temp.pop())

    tops = ""
    for i in range(1,10):
        tops += str(stacks[i].pop())
    return tops

def main():
    print("These are the top elements for each stack after we iterate: ",craters('Day5Data.txt'))
    print("These are the top elements for each stack after we iterate with CrateMover 9001: ",CrateMover9001('Day5Data.txt'))
 
if __name__ == "__main__":
    main()