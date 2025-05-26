'''
You are given a list of integers sorted in ascending order. Write a Python function to search for a given element in the list using Binary Search method.
Input Description:
First line contains list elements in ascending order seperated by comma.
Second line contains the element to be searched for in the list.
Print "Not Found" if the element is not found in the list 
Sample Input:
2,4,6,8,10,12,14,16,18,20,22,24,26
20
Sample Output:
9
'''

#Code starts here
list1 = [int(i) for i in input().split(',')]
n = int(input())

def binary_search(list1, n):
    lower_index = 0
    upper_index = len(list1)-1
    while(lower_index<=upper_index):
        mid_index = (lower_index+upper_index)//2
        if list1[mid_index]==n:
            return mid_index
        elif list1[mid_index]<n:
            lower_index = mid_index+1
        elif list1[mid_index]>n:
            upper_index = mid_index+1
    return("Not Found")

print(binary_search(list1,n))
#Code ends here 