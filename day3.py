#for each line in list
#       right to left
#       get highest int, and highest int in position after
#           set as highest if > highest
#       left to right
def myFunc(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()
    
    total = 0
    for line in lines:
        line = line.strip()
        
        runningHighest = 0
        for index, char in enumerate(line):
            for index2 in range(index + 1, len(line)):
                char2 = line[index2]
                two_digit = int(f"{char}{char2}")
                runningHighest = max(runningHighest, two_digit)
        
        reversed_line = line[::-1]  
        runningHighestA = 0
        for index, char in enumerate(reversed_line):  
            for index2 in range(index + 1, len(reversed_line)):
                char2 = reversed_line[index2]
                two_digit = int(f"{char}{char2}")
                runningHighestA = max(runningHighestA, two_digit)
        
        if runningHighest > runningHighestA:
            max_joltage = runningHighest
        else:
            max_joltage = runningHighestA
        
        total += max_joltage
    
    print(total)

myFunc('resources/jolt.txt')