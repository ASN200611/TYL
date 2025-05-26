'''
A person has made a list of songs and another list of their singers. Write a Python program to determine his favorite singer. 
The favorite singer is the one whose song appears maximum number of times in the list.
Sample Input:
song1,song2,song3,song4,song5,song6,song7,song8
sonu,arijit,vishal,arijit,sonu,arijit,sonu,sonu 
Sample Output:
sonu,4
'''

#Code starts here
list1 = input().split(',')
list2 = input().split(',')
list3 = list(set(list2))
c = 0
for i in list3:
    if list2.count(i)>c:
        c = list2.count(i)
        fav = i
print(fav, c, sep = ',')
#Code ends here 