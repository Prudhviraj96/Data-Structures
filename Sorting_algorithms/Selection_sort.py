'''Selection sort is a simple and efficient sorting algorithm that works by repeatedly selecting the smallest (or largest) 
element from the unsorted portion of the list and moving it to the sorted portion of the list. 

**The algorithm repeatedly selects the smallest (or largest) element from the unsorted portion of the list and swaps it with the first element of the unsorted part. This process is repeated for the remaining unsorted portion until the entire list is sorted. 
'''

# Time Complexity:  O(N2) 
# Auxiliary Space: O(1)

def selectionsort(arr):
  i = 0
  while i < len(arr):
    min = arr[i]
    index = i
    for j in range(i+1,len(arr)):
      if arr[j] < min:
        index = j
        min = arr[j]
    arr[i] , arr[index] = arr[index] , arr[i]
    i += 1
  
  return arr

arr = [8,6,5,0,4,3,2]
print(selectionsort(arr))
        