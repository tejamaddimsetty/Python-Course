"""
list2=input list
1) Print the largest elemet of the above list
2) Print the smallest element of the above list
3) sort the list above
"""

# creating empty list
list2=[]

# number of elements as input
n=int(input('Enter number of elements:'))

# iterating till the range
for i in range(0,n):
    ele = int(input())

    list2.append(ele) #adding the element


print ('List:',list2)
print ('The largest elemet of the above list:', max(list2))
print ('The smallest element of the above list:',min(list2))
print ('The sorted list is:',sorted(list2))
