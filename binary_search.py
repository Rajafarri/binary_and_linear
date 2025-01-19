def binarySearch(numbers, targetNum):
    start = 0
    end = len(numbers) - 1

    while start <= end:
        mid = (start + end) // 2

        if numbers[mid] == targetNum:
            return mid
        
        if numbers[mid] < targetNum:
            start = mid + 1
        else:
            end = mid - 1

    return -1

numArray = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
searchNum = 16

result = binarySearch(numArray, searchNum)

if result != -1:
    print("Value", searchNum, "found at index", result)
else:
    print("Target not found in array.")
