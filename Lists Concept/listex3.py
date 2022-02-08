"""
Create a list called list1 having 8 elements in it with 4 different datatypes.
create sub list named list2 from list1 by excluding the first 2 and last 2 elements of list 1
create list3 by giving some random values
create list4 by combining elements of list 1 and list 3
"""

list1=[1,2,3.1,4.1,'hello', 'python', [1,6], [7,8]]
list2 = list1[2:6]
print (list2)
list3=[11,41, 'HYD']
list4=list1+list3
print(list4)