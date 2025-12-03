import re



def findCombo(startingDigit, filepath):
    currentSpot = startingDigit
    zeroCounter = 0
    instruction = 0

    with open(filepath, 'r') as file:
        lines = file.readlines()
        for line in lines:
            match = re.match(r'([LR])(\d+)', line)
            if match:              
                instruction = int(match.group(2)) * (-1 if match.group(1) == 'L' else 1)
                print(f"{currentSpot} before change of instruction: {instruction}")
                currentSpot += instruction 

                if currentSpot > 99:
                    currentSpot = currentSpot % 100 #had +99 here for longest time causing wrong answer
                if currentSpot < 0:
                    while currentSpot < 0:
                        currentSpot = 100 + currentSpot

                print(line, currentSpot )

                if currentSpot == 0:
                    zeroCounter += 1

    print(zeroCounter)



    


findCombo(50,'resources/L23.txt')