'''
In a tree plantation, trees are planted in a row. Some places in the row are empty.
You are given an array of 0s and 1s. Then you are given an integer 'n.
1 indicates that there is already a tree, 0 indicates that there is an empty space to plan a tree sapling.
You are given 'n' tree saplings. 
You have to plant the tree saplings such that adjacent places are empty.

Write a Python program to output the status of plantation in terms of 1s and 0s after the number of saplings as planted. 
If such an allocation is not possible, your program should print False.
Sample Input:
1,0,1,0,0,0,1,0,0
2
Sample Output:
1,0,1,0,1,0,1,0,1
'''

#Code starts here
list1 = [int(i) for i in input().split(',')]
n = int(input())

if list1[0] == 0 and list1[1]==0:
    list1[0] = 1
    n = n-1

for i in range(1,len(list1)-1):
    if n == 0:
        break
    else:
        if list1[i-1]==0 and list1[i]==0 and list1[i+1]==0:
            list1[i] = 1
            n = n-1

if n>0 and list1[-1]==0 and list1[-2]==0:
    list1[-1]=1
    n = n-1

if n>0:
    print(False)
else:
    print(*list1,sep=',')
#Code ends here
