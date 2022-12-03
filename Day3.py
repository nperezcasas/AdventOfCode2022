import string 

def repeatedRucksacks(input):
    file = open(input, 'r')

    total_priority = 0
    
    for each in file:
        n = len(each)
        compartment_one = []
        for i in range(n//2):
            compartment_one.append(each[i])
        for i in range(n//2,n):
            if each[i] in compartment_one:
                total_priority += priority(each[i])
                break
    return total_priority

def part2(input):
    file = open(input, 'r')

    total_priority = 0
    i = 0
    for each in file:
        i += 1
        if i%3 == 1:
            common = []
            for letter in each[:-1]:
                common.append(letter)
        elif i%3 == 2:
            common_two = []
            for letter in each[:-1]:
                if letter in common:
                    common_two.append(letter)
        elif i%3 == 0:
            for letter in each[:-1]:
                if letter in common_two:
                    total_priority += priority(letter)
                    break
    return total_priority

def priority(input):
    lower = list(string.ascii_lowercase)
    upper = list(string.ascii_uppercase)
    values = {}
    i = 1
    for letter in lower:
        values[letter] = i
        i += 1
    for letter in upper:
        values[letter] = i
        i += 1
    return values[input]

def main():
    print("These is the total amount of priority from the elfs: ", repeatedRucksacks('Day3Data.txt'))
    print("What is the sum of the priorities of those item types? ", part2('Day3Data.txt'))
 
if __name__ == "__main__":
    main()