'''Bubble sort is a simple sorting algorithm used in Python to arrange data in a specific order, either ascending or descending.
It works by repeatedly iterating through a list, comparing and swapping adjacent elements if they are in the wrong order.'''

# Time Complexity: O(N2)
# Auxiliary Space: O(1)



def bubblesort(arr):
  qw = 0
  while qw < len(arr):
    for i in range(0,len(arr)-1):
      if arr[i] > arr[i+1]:
        arr[i] , arr[i+1] = arr[i+1] , arr[i]
    
    qw += 1
  return arr

arr = [5,9,1,2,7,3,8,2]
print(bubblesort(arr))

    