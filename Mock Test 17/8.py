'''
You are selling tickets for a music show. The price of each ticket is 5 rupees. You are allowed to sell only one ticket per person.
Each person may give you either 5 rupee note or 10 rupee note or 20 rupee note. Iinitially you do not have any money with you.
You are given an array of integers which represents the money given to you by customers. Write a Python program to check whether you can return exact change for all the customers or not.
Your program should print True or False depending on whether it is possible for you to return exact change for all customers or not.
Note: You cannot consider future colloections to tender exact change at present.
Sample Input:
5,5,10,5,20
Sample Output:
True
'''

#Code starts here
list1 = [int(i) for i in input().split(',')]

def change(list1):
    fives = 0
    tens = 0
    twenties = 0
    for i in range(len(list1)):
        if list1[i] == 5:
            fives = fives + 1
        elif list1[i] == 10:
            tens = tens + 1
            if fives == 0:
                return False
            else:
                fives = fives - 1
        else:
            twenties = twenties - 1

            if fives >= 3:
                return True
            elif tens>=1 and fives>=1:
                return True
            else:
                return False

print(change(list1))
#Code ends here 