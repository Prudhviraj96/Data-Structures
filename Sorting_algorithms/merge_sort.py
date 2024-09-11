'''Merge Sort in Python is a popular and efficient sorting algorithm that works on the concept of divide and conquer.
This technique involves dividing a problem into multiple sub-problems. 
Each sub-problem is then solved individually. Finally, sub-problems are combined to form the final solution.'''

# Time Complexity: O(n*log(n))
# Auxiliary Space: O(n)

arr = [99,44,6,2,1,5,63,87,283,4,0]

def mergesort(arr):
  if len(arr) == 1:
    return arr
  length = len(arr)
  mid = length // 2
  left = arr[:mid]
  right = arr[mid:]
  print('Left {}'.format(left))
  print('Right {}'.format(right))

  return merge(mergesort(left),mergesort(right))

def merge(left,right):
  result = []
  leftindex = 0
  rightindex = 0
  while leftindex < len(left) and rightindex < len(right):
    if left[leftindex] < right[rightindex]:
      result.append(left[leftindex])
      leftindex += 1
    else:
      result.append(right[rightindex])
      rightindex += 1
  print(left,right)
  print( result + left[leftindex:] + right[rightindex:] )
  return result + left[leftindex:] + right[rightindex:]


x = mergesort(arr)
print(x)