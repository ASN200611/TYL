'''
You are given an integer. Write a program to print the required pattern of numbers.
Sample Input:
4
Sample Output:
1 2 3 4
3 6 9 12
5 10 15 20
7 14 21 28
'''

#code starts here
n = int(input())
a = 1
for i in range(1,n+1):
    list1 = []
    for j in range(1,n+1):
        list1.append(a*j)
    print(*list1)
    a += 2
#code ends here 