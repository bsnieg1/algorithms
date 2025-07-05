def selection_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

arr = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print("Original array:", arr)
print("Sorted array:", selection_sort(arr))