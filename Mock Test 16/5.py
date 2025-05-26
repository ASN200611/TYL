'''
Write a Python program to decode a encoded string

Sample Input:
a2b3c1
Sample Output:
aabbbc
'''

#code starts here
str1 = input()
list1 = str1.split()
s=''
for i in range(0,len(str1),2):
    for j in range(int(str1[i+1])):
        s = s+str1[i]

print(s)

#code ends here