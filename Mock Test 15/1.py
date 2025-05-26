'''
You are given an integer. Write a program to print the required pattern of numbers.
Sample Input:
5
Sample Output:
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''

#code starts here
n = int(input())
list1 = []
for i in range(1,n+1):
    list1.append(i)
    print(*list1)
#code ends here 
