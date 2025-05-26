'''
You want to purchase two gift items for your friends. You have a budget of 'x' rupees.
You have an array which contains price of multiple gift items.
Write a Python program to find the price of two gift items such that total price is equal to your budget.
Input Description:
First line of input contains price of gift items by comma. 
Second line contains your budget
Sample Input:
50,110,150,200,180,230
330
Sample Output:
150,180
'''

#Code starts here
x = [int(i) for i in input().split(',')]
budget = int(input())

for i in range(len(x)-1):
    for j in range(i+1,len(x)):
        if x[i]+x[j]==budget:
            print(f'{x[i]},{x[j]}')
#Code ends here