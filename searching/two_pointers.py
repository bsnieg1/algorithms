def two_pointers(arr, target):
    left, right = 0, len(arr)-1
    while left<right:
        sum = arr[left] + arr[right]
        if sum == target:
            return [arr[left], arr[right]]
        elif sum < target:
            left = left + 1
        else:
            right = right - 1
    return "not found"



arr = [50, 10, 20, 40, ]
target = 70
print(two_pointers(arr, target))  