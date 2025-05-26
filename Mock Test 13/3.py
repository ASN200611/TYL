'''
You are given an array of probabailites of raining in the next few days.
You want to organize a Cricket tournament for three consecutive days. Write a Python program to select three days such that average probabilities of raining are least.
Sample Input:
0.5,0.6,0.4,0.4,0.5,0.3,0.3
Sample Output:
5,6,7
'''

#Code starts here
list1 = [float(i) for i in input().split(',')]

avg = 1
for i in range(len(list1)-2):
    if ((list1[i]+list1[i+1]+list1[i+2])/3)<avg:
        days = [i+1,i+2,i+3]
        avg = (list1[i]+list1[i+1]+list1[i+2])/3

print(*days, sep = ',')
#Code ends here