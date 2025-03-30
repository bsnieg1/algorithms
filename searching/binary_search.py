def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        middle = (left + right) // 2
        if arr[middle] == target:
            return middle
        elif arr[middle]>target:
            right=middle+1
        else:
            left=middle-1
    return -1


x = [x for x in range(10)]
print(x)
if binary_search(x, 5) == -1:
    print("Not found")
else:
    print("Element found")