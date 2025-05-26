'''
You are given two arrays. One array contains the name of batters and the other contains the runs scored by them.
Write a Python program to print the names of top three batters and their runs
Sample Input:
Rohit,Shubhman,Virat,Shreyas,Rahul,Hardik, Ravindra
45,60,125,40,20,8,4
Sample Output:
Virat,125
Shubhman,60
Rohit,45
'''

#Code starts here
list1 = input().split(',')
list2 = [int(i) for i in input().split(',')]
list3 = sorted(list2)

max1 = list3[-1]
max2 = list3[-2]
max3 = list3[-3]

index1 = list2.index(max1)
index2 = list2.index(max2)
index3 = list2.index(max3)

print(list1[index1],max1,sep=',')
print(list1[index2],max2,sep=',')
print(list1[index3],max3,sep=',')
#Code ends here
