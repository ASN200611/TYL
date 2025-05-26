'''
You are given an array of integers and two other integers k and n. 
Write a python program to print the kth largest element and the nth smallest element of the array.
Sample Input:
4,3,2,5,6,7
3
2
Sample Output:
5
3
'''

#Code starts here
x = [int(i) for i in input().split(',')]
k = int(input())
n = int(input())
x = sorted(x)
print(x[-k])
print(x[n-1])

#Code ends here