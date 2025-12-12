# 11-22 has two invalid IDs, 11 and 22.
# 95-115 has one invalid ID, 99.
# 998-1012 has one invalid ID, 1010.
# 1188511880-1188511890 has one invalid ID, 1188511885.
# 222220-222224 has one invalid ID, 222222.
# 1698522-1698528 contains no invalid IDs.
# 446443-446449 has one invalid ID, 446446.
# 38593856-38593862 has one invalid ID, 38593859.
# The rest of the ranges contain no invalid IDs.


def findIdSum(filepath):
    idCounter = 0
    numbers = []

    with open(filepath, 'r') as file:
        content = file.read()
        pairs = content.split(',')

        for pair in pairs:
            pair = pair.strip()
            if pair:
                number = pair.split('-')
                beginInt = int(number[0])
                endInt = int(number[1])

                while beginInt <= endInt:
                    numbers.append(beginInt)
                    beginInt += 1

        for num in numbers:
            if len(str(num)) % 2 == 0:
                splitpoint = len(str(num)) // 2
                idLeft = str(num)[:splitpoint]
                idRight = str(num)[splitpoint:]

                if idLeft == idRight:
                    idCounter += num

    print(idCounter)
    return idCounter


findIdSum('resources/idList.txt')

# @idCounter
# For each string in list
#   @beginInt = left of -
#   @endInt = right of -
#   while @beginInt <= @endInt
#     add @beginInt to sub-list
# .     @beginInt ++
#       For each @id in sub-list
#           if #numOfDigits is odd or left(1) ==0
#               return
#           @splitPoint = strlength / 2
#                @idLeft= left(@splitpoint)
#                @idRight = right(@splitpoint)
#               if @idLeft == @idRight
#                   @idCounter += @id
