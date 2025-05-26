'''
Given an integer n, write a Python program to print the first n row of Pascal's triangle.
In the Pascal's triangle, each number is the sum of the two numbers directly above.
Sample Input:
5
Sample Output:
1
1 1
1 2 1
1 3 3 1
1 4 6 4 1
'''

#Code Starts Here
n = int(input())
list1 = [1]
list2 = [1,1]
if n==1:
    print(*list1)
elif n==2:
    print(*list1)
    print(*list2)
else:
    print(*list1)
    print(*list2)
    for i in range(2,n):
        list3 = []
        for j in range(i+1):
            list3.append(1)
        for j in range(1,i):
            list3[j]=list2[j]+list2[j-1]
        list2 = list3
        print(*list3)
#Code Ends Here