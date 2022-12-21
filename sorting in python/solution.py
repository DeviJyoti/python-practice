"""Program 7. program for sorting like slection
sort,bubble sort,insertion sort.
"""

CODE:-
def bubbleSort(arr,n):
for i in range(n - 1):
for j in range(n - 1 - i):
if arr[j] > arr[j + 1]:
arr[j], arr[j + 1] = arr[j + 1], arr[j]
def selectionSort(arr,n):
for i in range(n - 1):
pos_smallest = i
for j in range(i + 1, n):
if arr[j] < arr[pos_smallest]:
pos_smallest = j
arr[i], arr[pos_smallest] = arr[pos_smallest], arr[i]
def insertionSort(arr,n):
for i in range(1, n):
temp = arr[i]
j = i - 1
while (j >= 0 and temp < arr[j]):
arr[j + 1] = arr[j]
j -= 1
arr[j + 1] = temp
arr = [20,9,6,3,1]
n = len(arr)
print('\nArray before bubbleSort :- ')
print(arr)
bubbleSort(arr,n)
print('\nArray after bubbleSort :- ')
print(arr)
arr = [20,9,6,3,1]
print('\nArray before selectionSort :- ')
print(arr)
selectionSort(arr,n)
print('\nArray after selectionSort :- ')
print(arr)
arr = [20,9,6,3,1]
print('\nArray before insertionSort :- ')
print(arr)
insertionSort(arr,n)
print('\nArray after insertionSort :- ')
print(arr)
