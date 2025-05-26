'''
You are given an integer. Write a program to print the required pattern of numbers.
Sample Input:
5
Sample Output:
*
* *
* * *
* * * *
* * * * *
'''

#code starts here
n = int(input())
list1 = []
for i in range(n):
    list1.append('*')
    print(*list1)
#code ends here 