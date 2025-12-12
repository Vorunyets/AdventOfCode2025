# rows to columns
# multiple dicts with key as problem #
# then iterate over dicts for answers
# for each num in dict while key < 1001:
#   operator
#   while key < 1001
#   operator = dict[keyvalue + 4000]
#   dict[key] @op dict[key + 1000] @op dict[key + 2000] @op dict[key + 3000]


def doHomework(filepath):
    with open(filepath, 'r') as file:
        lines = file.read().split()
    numDict = {}
    for i, val in enumerate(lines):
        if val.isdigit():
            numDict[i] = int(val)
        else:
            numDict[i] = val  # Keep operators as strings

    print(numDict[0])
    print(numDict[1000])
    print(numDict[2000])
    print(len(numDict))

    grandTotal = 0
    doIt = 0
    print(numDict[doIt + 4000])

    ops = {
        '+': lambda a, b: a + b,
        '*': lambda a, b: a * b
    }

    while doIt < 1000:

        total = numDict[doIt]
        operator = numDict[doIt + 4000]

        for x in range(1, 4):
            total = ops[operator](total, numDict[doIt + (x * 1000)])

        doIt += 1

        grandTotal += total
    print(grandTotal)


doHomework('resources/math.txt')
