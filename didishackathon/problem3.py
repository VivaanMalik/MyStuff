from unittest import result


NumberInput = int(input("Input instance:\n"))
print("Output:\n")

def findCombinations(NumSum, MinNum4Sum, Sum, combinednumbers):

    if Sum==NumSum:
        print(str(combinednumbers).replace("[", "").replace("]", "").replace(", ", " + "))
        pass
    
    for i in range(MinNum4Sum, NumSum): #cant go more than the number needed... (3/5)
        if Sum+i<=NumSum:
            combinednumbers.append(i)
            # print(str(i) + " " + str(Sum+i) + " " + str(combinednumbers))
            findCombinations(NumSum, i, Sum+i, combinednumbers)
            combinednumbers.pop(len(combinednumbers)-1)
        else:
            return

findCombinations(NumberInput, 1, 0, []) # start from 1 with a sum of 0 and empty combined number list
print(NumberInput)
