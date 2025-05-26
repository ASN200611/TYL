'''
You are given an integer. Write a program to print the required pattern of numbers.
Sample Input:
3
Sample Output:
1 1 1
2 2
3
'''

#code starts here
n = int(input())
for i in range(1, n+1):
    list1 = []
    for j in range(n+1, 0, -1):
        list1.append(i)
    print(*list1[i:])
#code ends here 

#code starts here
n = int(input())
a = n
for i in range(1, n+1):
    list1 = []
    for j in range(a):
        list1.append(i)
    print(*list1, sep=' ')
    a = a-1
#code ends here 