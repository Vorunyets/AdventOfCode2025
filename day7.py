# @positionBeam
# @ObjectBelowBeam
# for @manifold grid
#   if @ObjectBelowBeam = splitter
#   @ObjectBelowBeam[@index ] -1 = beam
#   @ObjectBelowBeam[@index ] + 1 = beam
#   else:
#       @ObjectBelowBeam = beam



def loadGrid(filepath):
    with open(filepath, 'r') as file:
        return [list(line.rstrip('\n')) for line in file]

def drawBeam(filepath):
    grid = loadGrid(filepath)
    numRows = len(grid)
    beamCounter = 0
    activatedSplitters = set()  
    
    for currentRow, row in enumerate(grid):
        for index, char in enumerate(row):
            if currentRow + 1 >= numRows:
                continue
                
            if char == 'S' or char == '|':
                if index < len(grid[currentRow + 1]) and grid[currentRow + 1][index] == '.':                    
                    grid[currentRow + 1][index] = '|'
                elif grid[currentRow + 1][index] == '^':
                    if (currentRow + 1, index) not in activatedSplitters:
                        beamCounter += 1
                        activatedSplitters.add((currentRow + 1, index))
                    
                    if index - 1 >= 0 and index - 1 < len(grid[currentRow + 1]):
                        grid[currentRow + 1][index - 1] = '|'
                    if index + 1 < len(grid[currentRow + 1]):
                        grid[currentRow + 1][index + 1] = '|'
    
    print(beamCounter)
    for row in grid:
        print(''.join(row))


drawBeam('resources/manifold.txt')