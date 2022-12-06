import queue

def marker(input):
    file = open(input, 'r')
    queue = []
    for line in file:
        for i in range(len(line)):
            if len(queue) < 4:
                queue.append(line[i])
            else:
                #print(queue)
                queue.pop(0)
                queue.append(line[i])
                    
                if len(queue) == len(set(queue)):
                    return i+1
def messages(input):
    file = open(input, 'r')
    queue = []
    for line in file:
        for i in range(len(line)):
            if len(queue) < 14:
                queue.append(line[i])
            else:
                #print(queue)
                queue.pop(0)
                queue.append(line[i])
                    
                if len(queue) == len(set(queue)):
                    return i+1

def main():
    print("First marker after character: ",marker('Day6Data.txt'))
    print("First marker after character: ",messages('Day6Data.txt'))
 
if __name__ == "__main__":
    main()