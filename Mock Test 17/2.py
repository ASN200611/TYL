'''
You are about to cross a river. There are stones placed at different positions in the river. You want to cross the river without stepping into water.
Write a Python program to check whether it is possible to cross the river without stepping into the water.
If yes, your program should print 'True'.
Otherwise, your program should print 'False'
Input Description:
You are given a comma seperated integer array which represents the position of stones in the river. For example, 
0,2,4,5,7,10
Next, you are given an integer which represents the maximum length you can jump at once. For example, 
3
If it is possible to cross the river without stepping into water.
So your program should return True.
Sample Input:
0,3,5,8,10,13
3
Sample Output:
True
'''

#code starts here
list1 = [int(i) for i in input().split(',')]
d = int(input())
for i in range(len(list1)-1):
    if (list1[i+1]-list1[i])>d:
        print(False)
        break
else: #else will excecute only when break statement is not excecuted.
    print(True)
#code ends here