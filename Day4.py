def fullyContained(line):

    first_elf = set()
    second_elf = set()
    num = ""

    for char in line:
        if char.isnumeric():
            num += char
        elif char == "-":
            num1 = num
            num = ""
        elif char == ",":
            for i in range(int(num1),int(num)+1):
                first_elf.add(i)
            num = ""
            num1 = "" 
    for i in range(int(num1),int(num)+1):
        second_elf.add(i)

    return (first_elf.issubset(second_elf) or second_elf.issubset(first_elf))

def someOverlap(line):

    first_elf = set()
    second_elf = set()
    num = ""

    for char in line:
        if char.isnumeric():
            num += char
        elif char == "-":
            num1 = num
            num = ""
        elif char == ",":
            for i in range(int(num1),int(num)+1):
                first_elf.add(i)
            num = ""
            num1 = "" 
    for i in range(int(num1),int(num)+1):
        second_elf.add(i)
        
    return (first_elf & second_elf)
        
def totalOverlap(input):
    file = open(input, 'r')
    total = 0
    for each in file:
        if fullyContained(each):
            total += 1
    return total

def totalSomeOverlap(input):
    file = open(input, 'r')
    total = 0
    for each in file:
        if someOverlap(each):
            total += 1
    return total

def main():
    print("These are the total number of full overlaps: ", totalOverlap('Day4Data.txt'))
    print("These are the total number of some overlap: ", totalSomeOverlap('Day4Data.txt'))
 
if __name__ == "__main__":
    main()
