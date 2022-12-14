
def part1(input): 
    file = open(input, 'r')
    score = 0
    for each in file:
        for letter in each:
            if letter in ["A","B","C"]:
                elf = letter
            elif letter.isspace():
                continue
            elif letter in ["X","Y","Z"]:
                second = letter
                if letter == "X":
                    score += 1
                elif letter == "Y":
                    score += 2
                elif letter == "Z":
                    score += 3
        if (elf == "A" and second == "X") or (elf == "B" and second == "Y") or (elf == "C" and second == "Z"):
            score += 3
        elif (elf == "A" and second == "Y") or (elf == "B" and second == "Z") or (elf == "C" and second == "X"):
            score += 6
    return score


def part2(input):
    file = open(input, 'r')
    score = 0
    for each in file:
        for letter in each:
            if letter in ["A","B","C"]:
                elf = letter
            elif letter.isspace():
                continue
            elif letter in ["X","Y","Z"]:
                second = letter
                if letter == "Y":
                    score += 3
                elif letter == "Z":
                    score += 6
        if (elf == "A" and second == "Y") or (elf == "B" and second == "X") or (elf == "C" and second == "Z"):
            score += 1
        elif (elf == "A" and second == "Z") or (elf == "B" and second == "Y") or (elf == "C" and second == "X"):
            score += 2
        elif (elf == "A" and second == "X") or (elf == "B" and second == "Z") or (elf == "C" and second == "Y"):
            score += 3
    return score


def main():
    print("Your score if second column is your rock, paper scissors pick: ", part1('Day2Data.txt'))
    print("Your score if second column is if you're winning, losing or drawing: ", part2('Day2Data.txt'))

 
if __name__ == "__main__":
    main()