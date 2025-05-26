'''
You are the manager of an auditorium. You have recieved multiple requests to rent the auditorium for specific dates. 
But some dates may be overlapping. Write a Python Program to remove all the overlapping intervals and retain only non-overlapping intervals.
Sample Input:
4
3-5
5-7
6-8
8-10
Sample Output:
3-5
6-8
'''

#code starts here
n = int(input())
list1 = []
for i in range(n):
    list1.append(input())
list2 = [list1[0]]
for i in range(1,n):
    a = list1[i]
    c = a.split('-')
    b = list2[-1].split('-')
    if (int(c[0])>int(b[-1])):
        list2.append(a)

print(*list2,sep='\n')

#code ends here