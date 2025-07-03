def ternary(arr, x):
    def search(l, r):
        if r < l:
            return -1
        mid1 = l + (r - l) // 3
        mid2 = r - (r - l) // 3

        if arr[mid1] == x:
            return mid1
        if arr[mid2] == x:
            return mid2

        if x < arr[mid1]:
            return search(l, mid1 - 1)
        elif x > arr[mid2]:
            return search(mid2 + 1, r)
        else:
            return search(mid1 + 1, mid2 - 1)

    return search(0, len(arr) - 1)


     

arr = [1, 2, 4, 8, 16, 32, 64, 128, 256]
ternary(arr, 64)
print("Element found at index:", ternary(arr, 64))