'''
Write a Python program to encode a given string.
Sample Input:
aaabbcaa
Sample Output:
a3b2c1a2
'''

#code starts here
str1 = input()
s = ''
count = 1
i = 0
while(i<len(str1)):
    j = i+1
    while(j<len(str1) and str1[i]==str1[j]):
        count = count+1
        j+=1
    s=s+str1[i]+str(count)
    i = i + count
    count = 1
    
print(s)
#code ends here