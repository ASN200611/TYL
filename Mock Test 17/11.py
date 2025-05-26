'''
A thief has found out how much cash is available in each house of a colony.
He wants to rob two houses adjacent to each other. Given as array of cash available in those houses.
Write a Python program to find out the index of two houses he has to select so that he can rob maximum money.
Sample Input:
100,200,150,20,10,30
Sample Output:
0,2
'''

#Code starts here 
list1 = [int(i) for i in input().split(',')]
profit = 0
for i in range(len(list1)-2):
    for j in range(i+2, len(list1)):
        if (list1[i]+list1[j])>profit:
            index1 = i
            index2 = j
            profit = list1[i]+list1[j]

print(index1, index2, sep=',')

#Code ends here 