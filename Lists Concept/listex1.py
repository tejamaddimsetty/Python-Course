"""
Reassign 'hello' in this nested lsit to say 'goodbye'
item in this list: list1 = [1,2,[3,4,'hello']]
expected output: [1,2,[3,4,'goodbye']]
"""
list1 =[1,2,[3,4,'hello']]
print(list1[2],[2])
list1[2][2]='goodbye'
print(list1)