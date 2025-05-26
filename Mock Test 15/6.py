'''
You are given an integer. Write a program to print the required pattern of numbers.
Sample Input:
4
Sample Output:
1 2 3 4
2 3 6
3 6
4
'''

#code starts here
n = int(input())
a = n
for i in range(1,n+1):
    list1 = []
    for j in range(1,a+1):
        list1.append(i*j)
    print(*list1)
    a -= 1
#code ends here 