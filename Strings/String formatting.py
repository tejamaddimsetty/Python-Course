"""
Similar to C's printf
<formatted string>% <elements to insert>
Can usually just use %s for everything, it will convert the object to its String representation.
"""

print("Current year is %s"%(2020))

print("%s was born in %s"%('John', 2000))

# Another type of representation
a = 2020
b = 'Raja'

print ("%s was born in %s"%(b, a))

# By using Input tag
a = int(input('Enter DOB:'))
b = input('Enter Name:')
# print current age
age = 2022 - a
print ("%s was born in %s and his/her age is %s"%(b, a, age))