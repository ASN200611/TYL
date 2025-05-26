'''
You are given an array of integers from N1 to N2.
Write a Python program to find the missing number.
Sample Input:
5,6,8,9
Sample Output:
7
'''

#Code starts here
x = [int(i) for i in input().split(',')]
for i in range(x[0],x[-1]):
    if i not in x:
        print(i)
#Code ends here