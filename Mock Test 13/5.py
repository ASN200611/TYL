'''
You are given an array of N integers.
Write a Python program to find the longest sequence of consecutive numbers.
Sample Input:
2,8,7,9,3
Sample Output:
7,8,9
'''

#Code starts here
x = [int(i) for i in input().split(',')]
x = sorted(x)

def continuous_array(x):
    for i in range(len(x)-1):
        if x[i+1]!=x[i]+1:
            return False
    return True

max_len = 0
for i in range(len(x)):
    for j in (i+1, len(x)):
        temp_array = x[i:j+1]
        if continuous_array(temp_array) and len(temp_array)>max_len:
            required_array = temp_array
            max_len = len(temp_array)

print(*required_array,sep=',')
#Code ends here