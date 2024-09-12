'''Quicksort is a sorting algorithm that uses a divide-and-conquer strategy to sort an array. 
It does so by selecting a pivot element and then sorting values larger than it on one side and smaller to the other side,
 and then it repeats those steps until the array is sorted. It is useful for sorting big data sets'''

'''Time Complexity
Best Case : Ω (N log (N))
Average Case: θ ( N log (N))
Worst Case: O(N ^ 2)

Auxiliary Space: O(1)'''


def quicksort(array,left,right):
    ln = len(array)
    if left < right:
        pivot = right
        partitionindex = partition(array, pivot, left, right)

        quicksort(array, left, partitionindex -1)
        quicksort(array, partitionindex +1, right)
    return array

def partition(array, pivot, left, right):
    pivotvalue = array[pivot]
    partitionindex = left

    for i in range(left,right):
        if array[i] < pivotvalue:
            swap(array, i, partitionindex)
            partitionindex += 1

    swap(array, right, partitionindex)
    return partitionindex

def swap(array, firstindex, secondindex):
    temp = array[firstindex]
    array[firstindex] = array[secondindex]
    array[secondindex] = temp


numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]

# Select first and last index as 2nd and 3rd parameters
print(quicksort(numbers,0,len(numbers)-1))