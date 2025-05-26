'''
The h-index is a metric that quantifies both the quantity and quality of an author's publications. If an author has 5 publications, each cited at least 5 times, his h-index is 5.
If an author has 10 publications, each cited at least 10 times, his h-index is 10.
You are givenan array of integers which represents the citations each publication of an author has got. Write a Python program to print the h-index of the author.
Sample Input:
2,3,4,3,4,2,4,3,4,5,5
Sample Output:
4
'''

#Code starts here
list1 = [int(i) for i in input().split(',')]
list2 = list(set(list1))
for i in list2:
    if list1.count(i)==i:
        h = i
print(h)
#Code ends here 