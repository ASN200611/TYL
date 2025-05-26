'''
You are given an array of integers.
Write a Python program to find the longest contiguous increasing subarray.
'''

#Code starts here
x = [int(i) for i in input().split(',')]

def increasing(x):
    for i in range(len(x)-1):
        if x[i]>=x[i+1]:
            return False
    return True

max_length = 0
for i in range(len(x)):
    for j in range(i+1, len(x)):
        temp_array = x[i:j+1]
        if increasing(temp_array) and len(temp_array)>max_length:
            required_array = temp_array
            max_length = len(required_array)

print(*required_array, sep = ',')
#Code ends here 
