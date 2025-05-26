'''
You are given a list of integers. Write a Python program function to search for the given element in the list using Linear Search method. If the element is present in the list, print the index of the element. 
Otherwise print "Not Found".
Input Description:
In the first line, elements are entered seperated by comma
In the second line, elements to be searched for is entered.
Sample Input:
2,3,3,1,5,6
3
Sample Output:
2
'''

#Code starts here
list1 = [int(i) for i in input().split(',')]
n = int(input())

def linear_search(list1,n):
    for i in range(len(list1)):
        if list1[i] == n:
            return(i)
    return("Not Found")

print(linear_search(list1,n))
#Code ends here