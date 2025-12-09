#   for char^n in line r
#       adjacent of char^n = 
#       top = line r + 1 char^n index, line r + 1 char^n (index-1), line r + 1 char^n (index+1)
#       side = line r char^n index-1, line r char^n index+1
#       bottom = line r - 1 char^n index, line r - 1 char^n (index-1), line r - 1 char^n (index+1)
#           anything out of bounds will be a ".", maybe error catch can do this?
#    
#   compute adjacent into list, and then count papers, if < 4 papers, add to total

from dataclasses import dataclass

@dataclass
class TpRoll:
    row: int
    index: int

def computeAdjacent(filepath):
    with open(filepath, 'r') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines if line.strip()]  # Empty lines
    
    counter = 0    
    for row_number, line in enumerate(lines):
        for index, char in enumerate(line):
            if char == '@':
                tpRoll = TpRoll(row_number, index)
                
                lineAbove = tpRoll.row - 1
                lineBelow = tpRoll.row + 1
                sideLeft = tpRoll.index - 1
                sideRight = tpRoll.index + 1
                
                def getOob(row, col):
                    if row < 0 or row >= len(lines) or col < 0 or col >= len(lines[row]):
                        return '.'
                    return lines[row][col]
                
                adjacent = [
                    getOob(lineAbove, sideLeft),
                    getOob(lineAbove, tpRoll.index),
                    getOob(lineAbove, sideRight),
                    getOob(tpRoll.row, sideLeft),
                    getOob(tpRoll.row, sideRight),
                    getOob(lineBelow, sideLeft),
                    getOob(lineBelow, tpRoll.index),
                    getOob(lineBelow, sideRight)
                ]
                
                rollsTp = sum(1 for each in adjacent if each == '@')
                
                if rollsTp < 4:
                    counter += 1
    
    print(counter)
    return counter

if __name__ == '__main__':
    result = computeAdjacent('resources/rolls.txt')