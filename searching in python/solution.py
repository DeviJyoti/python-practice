"""Program 6 . program for searching operations like
linear search , binary search"""

CODE:-
#program 14.
# Linear Search
def LinearSearch(array, n, k):
for i in range(0, n):
if (array[i] == k):
return i
return -1
array = [1, 3, 5, 7, 9]
k = 7
n = len(array)
print("\nWe tried to find ",k,"in",array,"using linear search :- ")
result = LinearSearch(array, n, k)
if (result == -1):
print("Element not found")
else:
print("Element found at index: ", result)
# Binary search
def BinarySearch(arr, k, low, high):
if high >= low:
mid = low + (high - low)//2
if arr[mid] == k:
return mid
elif arr[mid] > k:
return BinarySearch(arr, k, low, mid-1)
else:
return BinarySearch(arr, k, mid + 1, high)
else:
return -1
arr = [1, 3, 5, 7, 9]
k = 5
print("\n\nWe tried to find ",k,"in",arr,"using binary search :- ")
result = BinarySearch(arr, k, 0, len(arr)-1)
if result != -1:print("Element is present at index " + str(result))
else:
print("Not found")
