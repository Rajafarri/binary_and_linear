# Searching Algorithms: Linear Search and Binary Search

In this project, I have implemented two fundamental searching algorithms: **Linear Search** and **Binary Search**. These algorithms are essential techniques for locating a specific value in a dataset, and this project helped me solidify my understanding of their concepts and time complexities.

## Purpose
The purpose of this project is to compare the simplicity and efficiency of Linear Search and Binary Search. Each algorithm has its specific use case:

- **Linear Search**: A straightforward approach to searching for a value by iterating through the array.
- **Binary Search**: A more efficient algorithm that works on sorted arrays by repeatedly dividing the search space in half.

By implementing both, I have practiced:
- Iterating through arrays effectively.
- Understanding the differences between linear and logarithmic time complexities.
- Writing clean, readable Python code.

---

## Algorithms

### Linear Search

The **Linear Search** algorithm checks each element in the array sequentially until the target value is found or the end of the array is reached.

### Code
```python
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
```

### Explanation
- **Iteration**: Loops through the array from the start.
- **Comparison**: Compares each element with the target value.
- **Result**: Returns the index of the target value if found; otherwise, returns `-1`.

### Time Complexity
- **Best Case**: O(1) – Target is the first element.
- **Worst Case**: O(n) – Target is the last element or not in the array.
- **Average Case**: O(n).

---

### Binary Search

The **Binary Search** algorithm is more efficient but requires the array to be sorted. It repeatedly divides the search space in half and compares the target value with the middle element.

### Code
```python
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
```

### Explanation
- **Initialization**: Defines the start and end of the array.
- **Middle Calculation**: Finds the middle element using integer division.
- **Comparison**: Checks if the middle element is the target. If not, adjusts the search range.
- **Result**: Returns the index of the target value if found; otherwise, returns `-1`.

### Time Complexity
- **Best Case**: O(1) – The middle element is the target.
- **Worst Case**: O(log n) – The search space is halved in each iteration.
- **Average Case**: O(log n).

---

## How to Run the Code

### Running the Linear Search
1. Copy the Linear Search code into your preferred Python editor (e.g., VS Code, PyCharm).
2. Save the file with a name like `linear_search.py`.
3. Run the file using Python:
   ```
   python linear_search.py
   ```

### Running the Binary Search
1. Copy the Binary Search code into your preferred Python editor.
2. Save the file with a name like `binary_search.py`.
3. Run the file using Python:
   ```
   python binary_search.py
   ```

---

## Conclusion
This project provided hands-on experience with both Linear Search and Binary Search algorithms. While Linear Search is simple, it becomes inefficient for large datasets. Binary Search, with its logarithmic time complexity, is much faster for sorted arrays.

By analyzing the differences between the two algorithms, I have gained insights into choosing the appropriate search technique depending on the dataset and use case.

## LinkedIn:
 Here is my linkedIn post's link:
 https://www.linkedin.com/mwlite/feed/update/activity:7286698025211617281?trk=share-post-success
