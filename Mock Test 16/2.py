'''
Given an array of integers which represents the daily temperatures, return an array such that ith number represents the number of days you have to wait after the ith day to get a warmer temperature.
If there is no future day for which this is possible, entry should be 0.
Sample Input:
25,26,24,28,27
Sample Output:
1,2,1,0,0
'''

#Code starts here
list1 = [int(i) for i in input().split(',')]
list2 = []

for i in range(len(list1)-1):
    d = 0
    flag = 0
    for j in range(i+1, len(list1)):
        if list1[j]>list1[i]:
            d = d+1
            flag = 1
            break
        else:
            d = d+1
    if flag == 0:
        list2.append(0)
    else:
        list2.append(d)
list2.append(0)

print(*list2, sep=',')

#Code ends here 