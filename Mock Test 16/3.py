'''
You  are given an integer array whose ith number represents the number of candies the ith kid has.
Also you are given an integer that represents the number of extra candies you have.
Write a Python program which returns a boolean array result, where result[i] is true if, after giving the ith kid all the extra candies, they will have the greatest number of candies among all the kids, or false otherwise.
Note that multiple kids can have the greatest number of candies.
Sample Input:
2,3,5,1,3
3
Sample Output:
True,True,True,False,True
'''

#Code starts here
list1 = [int(i) for i in input().split(',')]
n = int(input())
list2 = []
for i in list1:
    if (i+n) >= max(list1):
        list2.append(True)
    else:
        list2.append(False)

print(*list2,sep=',')
#Code ends here 