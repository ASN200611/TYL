'''
You are given an array of integers. Write a Python program to check whether the difference between adjacent elements goes on increasing.
Print 'True' if yes. Otherwise print 'False'.
For example, 
[5,6,7,8] -> This is an increasing array. But this is not an expanding array because difference between adjacent elements is not increasing. So your program should return 'False'.
[5,6,9,13,18] -> This is an expanding array. Because difference between adjancent elements is increasing. So your program should return 'True'.
'''

#Code starts here
x = [int(i) for i in input().split(',')]

def function(x):
    for i in range(2, len(x)):
        diff1 = x[i]-x[i-1]
        diff2 = x[i-1]-x[i-2]
        if diff1<=diff2:
            return False
    return True

print(function(x))
#Code ends here 