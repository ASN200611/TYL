'''
Given an array of integers and an integer k, find the contiguous subarray of length k such that sum of its elements is maximum.
Sample Input:
-1,2,3,3,4,5,-1,3
Sample Output:
3,4,5
'''

#Code starts here
x = [int(i) for i in input().split(',')]
k = int(input())
max_sum = 0
for i in range(len(x)-k+1):
    if sum(x[i:i+k])>max_sum:
        max_sum = sum(x[i:i+k])
        required_array = x[i:i+k]

print(*required_array, sep=',')
#Code ends here