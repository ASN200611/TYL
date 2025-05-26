'''
You are given two integer arrays. Array-1 represents denominations of coins. Array-2 represents number of coins of each denomination. 
You are allowed to pick any three heaps of coins.
Write a python program to determine the index of heaps to be collected so that you can maximize the amount of money collected
Sample Input:
1,2,5,10,20
10,3,5,2,1
Sample Output:
2,3,4
'''

#Code starts here
list1 = [int(i) for i in input().split(',')]
list2 = [int(i) for i in input().split(',')]
list3 = []

for i in range(len(list1)):
    list3.append(list1[i]*list2[i])

sum1 = 0

for i in range(len(list1)-2):
    for j in range(i+1, len(list1)-1):
        for k in range(j+1, len(list1)):
            if (list3[i]+list3[j]+list3[k])>sum1:
                index1 = i
                index2 = j
                index3 = k
                sum1 = list3[i]+list3[j]+list3[k]

print(index1, index2, index3, sep=',')
#Code ends here 