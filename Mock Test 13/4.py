'''
You are given an array of positive and negative integers.
Write a Python program to determine the subarray with maximum sum.
Sample Input:
2,-1,3,-2,1,-2
Sample Output:
2,-1,3
'''

#Code starts here
x = [int(i) for i in input().split(',')]
max_sum = 0

for j in range(len(x)):
    for i in range(j+1, len(x)+1):
        subarray = x[j:i]
        if sum(subarray)>max_sum:
            required_array = subarray
            max_sum = sum(required_array)

print(*required_array, sep = ',')
#Code ends here 