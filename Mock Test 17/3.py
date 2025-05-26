'''
A biker went on an adventurous journey. He encountered different terrains of varying altitudes. The alittude gains from point 'i' to point 'i+1' were recorded in an array. 
Write a Python program to find the highest altitude the biker reached in his journey.
Sample Input:
0,5,-2,-4,3,4,-1
Sample Output:
6
'''

#code starts here
list1 = [int(i) for i in input().split(',')]
list2 = []
sum = 0
for i in list1:
    sum = sum+i
    list2.append(sum)
print(max(list2))
#code ends here