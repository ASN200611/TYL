'''
You are given an array of 1s and 0s. 1 represents land and 0 represents water. Wrtie a Python program to output the number of islands present in the array. Exclude first and last entries to count the number of islands.
Sample Input:
1,0,0,1,0,1,0,1,0
Sample Output:
3
'''

#code starts here
list1 = [int(i) for i in input().split(',')]
count = 0
for i in range(1, len(list1)-1):
    if list1[i-1]==0 and list1[i]==1 and list1[i+1]==0:
        count += 1

print(count)
#code ends here