'''Insertion sort is a simple sorting algorithm in Python that works by building a sorted section of the list one element at a time. 
It iteratively compares each element with its preceding elements and inserts it into its correct position within the sorted section.'''

# Time Complexity: O(N2) 
# Auxiliary Space: O(1)

def insertionsort(arr):
  length = len(arr)
  i = 1
  end = arr[0]
  while i < length:
    if arr[i] < end:
      x = arr.pop(i)
      for j in range(0,i):
        if x < arr[j]:
          arr.insert(j,x)
          break
    end = arr[i]
    i += 1
  return arr

arr = [6,5,3,1,8,7,2,4]
print(insertionsort(arr))