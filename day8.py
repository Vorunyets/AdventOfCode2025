# sort list by closest
# for each, find and store/key nearest neighbor, add a score
# closer to difference of 0 = more similar
# to find/count all circuits, need trace through all neighbors, finding tracing through all trees, like would do on the ceiling.


import numpy as np

vector1 = np.array([10,10,10])  #np.array([17501,13816,60954]) 
vector2 = np.array([5,5,5]) #np.array([14182,69525,69278])



def calulateScore(coords1, coords2):
    score = abs(coords1[0] - coords2[0]) + abs(coords1[1] - coords2[1]) + abs(coords1[2] - coords2[2])
    return score
    

def jumperApp():
    data = []
    with open('resources/junction.txt','r') as file:
        for line in file:
            coords = tuple(map(int, line.strip().split(',')))
            data.append(coords)

    neighbors = {}

    # for every entry, run the function over the entire list
    for idx, each in enumerate(data):       
        lowestScore = float('inf')
        lowestIDIdx = None
        for index, everyOther in enumerate(data):      
            if idx == index:
                continue       
            score = calulateScore(each,everyOther)
            # store lowest score
            if score < lowestScore:
                lowestScore = score
                lowestIDIdx = index
            
        neighbors[idx] = (lowestIDIdx,lowestScore)

    # would select lowest 1000, then have list of matches.
    # countCircuit():
    #    

    



jumperApp()