def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


x = [x**2 for x in range(10)]

if linear_search(x, 25) == -1:
    print("Not found")
else:
    print("Found at index", linear_search(x, 25))