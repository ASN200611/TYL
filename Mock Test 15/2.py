'''
You are given an integer. Write a python program to print the required pattern of numbers.
Sample Input:
4
Sample Output:
1 2 3 4 
1 2 3
1 2
1
'''

#code starts here
n = int(input())
list1 = []
for i in range(1,n+1):
    list1.append(i)
for i in range(n,0,-1):
    list1.append(i)
    print(*list1[0:i])
#code ends here 