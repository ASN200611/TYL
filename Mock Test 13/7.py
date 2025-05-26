'''
You are given an array of integers and a target number.
Write a Python program to find two numbers such that their sum is equal to the target number.
If there is no such pair, then print 'NO'
Sample Input:
2,6,5,8,1
9
Sample Output:
8,1
'''

#Code starts here 
list1 = [int(i) for i in input().split(',')]
n = int(input())
flag = 0

for j in range(len(list1)-1):
    for i in range(j+1, len(list1)):
        if list1[j]+list1[i]==n:
            print(list1[j],list1[i], sep = ',')
            flag = 1

if flag == 0:
    print('NO')
#Code ends here