import heapq

def heapsort(iterable):
    ans = []
    while iterable:
        ans.append(heapq.heappop(iterable))
    return ans

myList = [5, 3, 8, 6, 2]
print(heapsort(myList))
# Output: [2, 3, 5, 6, 8]