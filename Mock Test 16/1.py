'''
Consider the following image of a chesss board.
Wrtie a Python Program to print the color of the specified square
For example, if the square is specified as 'a1', your program should output 'Black'.
If the sqaure is specified as 'f7', your program should output 'White'

Sample Input:
d6
Sample Output:
Black
'''

#code starts here

str1 = input()
if str1[0] in 'aceg' and int(str1[1])%2==0:
    print('White')
elif str1[0] in 'aceg' and int(str1[1])%2!=0:
    print('Black')
elif str1[0] in 'bdfh' and int(str1[1])%2==0:
    print('Black')
else:
    print('White')

#code ends here