'''
You have organized a coding Hackathon.
You have collected marks scored by participants in an array and time taken for submission in another array.
Write a Python Program to determine the winner.
If two candiates have scored same marks, then whoever took the least time should be selected as winner.
Sample Input:
50,80,70,80,80,75
45,35,55,50,45,35
Sample Output:
2
'''

#Code starts here
x = [int(i) for i in input().split(',')]
y = [int(i) for i in input().split(',')]
max1 = max(x)
list1 = []
list2 = []

for i in range(len(x)):
    if x[i] == max1:
        list1.append(i)
        list2.append(y[i])

mini = min(list2)
ind = y.index(mini)
print(ind+1)

#Code ends here 