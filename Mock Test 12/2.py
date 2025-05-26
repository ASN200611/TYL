'''
You are given a list of strings containing letters, (, ), {, }, [, ].
Write a Python program to print the strings in which parenthesis are matched.
Input Description: 
First Integer represents the length of the list.
Then the list elements are entered one below the other.
Sample Input:
4
[ra(vee{s}h)]
ra(vee{s}h)]
]ra(vee{s}h)[
[ra{vee(s)h}]
Sample Output:
[ra(vee{s}h)]
[ra{vee(s)h}]
'''

#Code starts here
def is_matched(s):
    stack = []
    for ch in s:
        if ch in '([{':
            stack.append(ch)
        elif ch in ')]}':
            if not stack or stack.pop() + ch not in ['()', '{}', '[]']:
                return False
    return not stack

n = int(input())
for _ in range(n):
    s = input()
    if is_matched(s):
        print(s)
#Code ends here 