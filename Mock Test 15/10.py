'''
You are given an integer. Write a program to print the required pattern of numbers.
Sample Input:
5
Sample Output:
* * * * *
* * * *
* * *
* *
*
'''

#code starts here
n = int(input())
list1 = []
for i in range(n):
    list1.append('*')
for i in range(n, 0, -1):
    print(*list1[0:i])
#code ends here 