'''
You are given a list containing stock price prediction for the next few days. Write a Python program to determine on which days an investor should buy and sell stocks to maximize the profit.
Sample Input:
90,100,80,94,110,85,60
Sample Output:
3,5
'''

#Code starts here
x = [int(i) for i in input().split(',')]

profit = 0

for i in range(len(x)-1):
    for j in range(i+1,len(x)):
        if x[j]-x[i]>profit:
            profit = x[j]-x[i]
            buy = i+1
            sell = j+1
print(buy, sell, sep=',')
#Code ends here 