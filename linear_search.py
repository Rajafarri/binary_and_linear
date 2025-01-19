def linearSearch(numbers, targetNum):
    for i in range(len(numbers)):
        if numbers[i] == targetNum:
            return i
    return -1

numbers = [12, 45, 23, 67, 34]
targetNum = 67

result = linearSearch(numbers, targetNum)

if result != -1:
    print("Value", targetNum, "found at index", result)
else:
    print("Value", targetNum, "not found")
