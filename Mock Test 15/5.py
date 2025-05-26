'''
You are given an integer. Write a program to print the required pattern of numbers.
Sample Input:
4
Sample Output:
1
2 4 
3 6 9
4 8 12 16
'''

#code starts here
n = int(input())
for i in range(1,n+1):
    list1 = []
    for j in range(1, i+1):
        list1.append(i*j)
    print(*list1)
#code ends here 