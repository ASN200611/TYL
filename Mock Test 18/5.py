'''
A traveller is planning to visit many places driving his car. You are given three arrays.
The first array contains the places he is planning to visit and the second array contains the amount of petrol required to visit the immediate next place and the third array contains the amount of petrol available in each gas station. Write a Python program to determine the last place he can reach before he runs out of petrol.
Sample Input:
Bengaluru,Chennai,Hyderabad,Amaravati,Bhopal,Jaipur,New Delhi
50,60,40,80,90,120
70,50,30,90,80,100
Sample Output:
Jaipur
'''

#Code starts here
list1 = input().split(',')
list2 = [int(i) for i in input().split(',')]
list3 = [int(i) for i in input().split(',')]

i = 0
sum1 = 0
sum2 = 0

while(i<len(list2)):
    sum1 = sum1 + list2[i]
    sum2 = sum2 + list3[i]
    if sum1>sum2:
        break
    else:
        i = i+1

print(list1[i])

#Code ends here 