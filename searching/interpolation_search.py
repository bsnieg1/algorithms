def interpolation_search(arr, x):
    low, high = 0, len(arr) - 1
    while low <= high and x >= arr[low] and x <= arr[high]:
        if arr[high] == arr[low]:
            if arr[low] == x:
                return low
            else:
                return -1
        pos = low + (x - arr[low]) * (high - low) // (arr[high] - arr[low])

        if arr[pos] == x:
            return pos
        if arr[pos] > x:
            high = pos - 1
        else:
            low = pos + 1
    return -1



arr = [1, 2, 4, 8, 16, 32, 64, 128, 256]
print("Element found at index:", interpolation_search(arr, 64))