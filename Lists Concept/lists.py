"""
Ordered collection of Data
Data can be of different types
Lists are mutable
Same subset operations as Strings.
"""

# Lists concept in python, Reading list, merging,
# Udpating specific location in list


list1 = [33, 44, 12]
print(list1)
list2 = list(list1)
print(list2)
list2[1] = 400
list2[2] = 7
list2[0] = 'hello'
print(list2)
print(list1)

x=[1,'hello', 3, 4, 'tej']
#print the list
print('List:',(x))
# print the following index of the list
print('2nd index of the List:',x[2])
#print the list elements from starting to specified point
print('First 2 elements of the List:',x[0:2])
#print the list elements from specific intervals
print('Specific interval of the List:',x[1:3])
#print the last list element
print('The last element of the List:',x[-1])
#print the length of the string
print('Length of the List:',len(x))

"""
List : Modifying Content
y[i] = a reassigns the value a to the ith element
The method apped also modifies the list
"""

y=[1,2,3]
print('List:',y)
y[1]=15
print('The updated list with new value in Index = 1 is: ',y)
y.append(12)
print('Append element to the updated list:',y)