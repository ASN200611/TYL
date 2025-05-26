'''
Given an integer n, write a Python program to print the first n row of Pascal's triangle.
In the Pascal's triangle, each number is the sum of the two numbers directly above.
Sample Input:
4
Sample Output:
1,3,3,1
'''

#Code starts here
n = int(input())
list1 = [1]
list2 = [1,1]
if n==1:
    print(*list1,sep=',')
elif n==2:
    print(*list2,sep=',')
else:
    for i in range(2,n):
        list3 = []
        for j in range(i+1):
            list3.append(1)
        for j in range(1,i):
            list3[j]=list2[j]+list2[j-1]
        list2 = list3
print(*list3,sep=',')
#Code ends here 
