
strings = ['a','b','c','d']
# 4*4 = 16 bytes of storage is used

print(strings[2])

#push  
strings.append('e')      # O(1)
#pop  
strings.pop() 
strings.pop()            # O(1)

#addfirstelement 
strings.insert(0,'x')    #O(n)

#splice
strings.insert(2,'alien')   #O(n)

print(strings)

#Array native python methods :-
#append()	Adds an element at the end of the list
#clear()	Removes all the elements from the list
#copy()	Returns a copy of the list
#count()	Returns the number of elements with the specified value
#extend()	Add the elements of a list (or any iterable), to the end of the current list
#index()	Returns the index of the first element with the specified value
#insert()	Adds an element at the specified position
#pop()	Removes the element at the specified position
#remove()	Removes the first item with the specified value
#reverse()	Reverses the order of the list
#ort()	Sorts the list