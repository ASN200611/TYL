'''
You are given an integer. Write a program to print the required pattern of numbers.
Sample Input:
5
Sample Output:
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
'''

#code starts here
n = int(input())

for i in range(1,n+1):
    list1 = []
    for j in range(1,i+1):
        list1.append(i)
    print(*list1)
#code ends here 

