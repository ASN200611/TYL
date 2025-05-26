'''
You are given a list of integers seperated by space in a single line.
Write a Python function 'Bubble_Sort()' to sort the list in ascending order
Sample Output:
10,8,6,4,2
Sample Input:
2,4,6,8,10
'''

#Code starts here
list1 = [int(i) for i in input().split(',')]

def Bubble_Sort(list1):
    for j in range(len(list1)-1):
        for i in range(len(list1)-1):
            if list1[i]>list1[i+1]:
                list1[i], list1[i+1] = list1[i+1], list1[i]
    print(*list1, sep = ',')

#This line cannot be edited
Bubble_Sort(list1)
#Code ends here