'''
In an IPL auction, several teams are bidding for Virat Kohli. You are given two arrays. The first array represents the teams of IPL and the second array represents how much each are bidding for Virat Kohli.
Write a Python program to determine which team will get Virat Kohli and how much their bidding amount is.
Sample Input:
RCB,CSK,MI,KKR,GT
20,25,15,16,18
Sample Output:
CSK,25
'''

#Code starts here
list1 = input().split(',')
list2 = [int(i) for i in input().split(',')]
m = max(list2)
index1 = list2.index(m)
print(list1[index1], list2[index1], sep=',')
#Code ends here