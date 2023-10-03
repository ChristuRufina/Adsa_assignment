# Input list
arr = [5, 2, 9, 1, 5, 6]

n = len(arr)

# Selection Sort
for i in range(n):
    minindex = i
    for j in range(i + 1, n):
        if arr[j] < arr[minindex]:
            min_index = j
    arr[i], arr[minindex] = arr[minindex], arr[i]

# Sorted array
sortedarray = arr
print(sortedarray)

"""

Time Complexity:
Selection Sort has a worst-case and average-case time complexity of O(n^2), where 'n' is the number of elements in the array. Like Bubble Sort, it is not efficient for large datasets.

Stability:
Selection Sort is not stable. It may change the relative order of equal elements.

Performance on Different Input Data:
1)Already Sorted: Selection Sort performs similarly on nearly sorted data as it does on completely random data. It doesn't have a specific advantage on nearly sorted data.
2)Reverse Sorted: Selection Sort also performs similarly on reverse sorted data as it does on random data.
3)Random Data: Selection Sort has consistent performance characteristics but is not efficient for large datasets.

Comparison with Bubble Sort:
1)Selection Sort and Bubble Sort have the same time complexity of O(n^2).
2)Both algorithms are generally not suitable for large datasets due to their quadratic time complexity.
3)If you need to choose between Selection Sort and Bubble Sort, they have similar performance characteristics, but Selection Sort is considered slightly more efficient due to fewer swaps.
4)For larger datasets, more efficient sorting algorithms like Quick Sort or Merge Sort are recommended.


"""
