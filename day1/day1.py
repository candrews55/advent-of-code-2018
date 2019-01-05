# load input data
inputNumbers = list(map(lambda x: int(x),(open('./input.txt', 'r').readlines())))

# First Part
answer = sum(inputNumbers)
print(answer)

# Second Part
currentSum = 0
previousSums = []
numbersToProcess = inputNumbers.copy()

while currentSum not in previousSums:
    if len(numbersToProcess) < 1:
        numbersToProcess = inputNumbers.copy()
    
    previousSums.append(currentSum)
    valueToAdd = numbersToProcess.pop(0)
    currentSum = currentSum + valueToAdd

print(currentSum)