# Usage of Input tag - Read values from terminal
# processing and returning them in the specific format
# Variable initilization and returning the datatype.

name = input("What's your name:")
dob = int(input("What's your year of birth:"))
age = 2022 - dob
print ('Hello', name)
print ('Your Age', age)
print ("%s was born in %s and current age is %s" %(name, dob, age))

# return datatype of variables
print ('----------------------Data types---------------------')
print (type(age))
print (type(name))
print (type(dob))
