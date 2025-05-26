'''
You are given a string.
Write a Python program to find the longest substring without any repeating character
Sample Input:
abcabcbb
Sample Output:
abc
'''

#Code starts here
str1 = input()
max_length = 0
for i in range(len(str1)):
    for j in range(i, len(str1)):
        substring = str1[i:j+1]
        if len(substring) == len(set(substring)) and len(substring)>max_length:
            required_substring = substring
            max_length = len(required_substring)

print(required_substring)
#Code ends here 