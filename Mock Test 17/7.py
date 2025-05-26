'''
You are given an integer array representing coins of different denominations and another integer representing a total amount of money.
Write a Python program to return the fewest number of coins that you need to make up that amount.
Note: Assume that there are sufficient number of coins of each denomination.
Input Description:
First line contains multiple integers seperated by comma. These integers represent denominations of coins.
Second line contians an integer which represents the sum of money to make up
Sample Input:
1,2,5,10
14
Sample Output:
3
'''

#Code starts here
list1 = [int(i) for i in input().split(',')]
n = int(input())
list1.sort(reverse = True)
count = 0

for i in list1:
    count = count+n//i
    n = n%i
    if n == 0:
        break

print(count)

#Code ends here
