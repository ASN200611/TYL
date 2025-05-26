'''
A traveller has given you a list of cities he is planning to visit. He has mentioned the intermediate source cities and the intermediate destination cities in pairs.
Write a Python program to determine the initial source city and final destination city.
The initial source city is the one which does not appear as an intermeidate destination city. 
The final destination city is the one which does not appear as an intermediate source city.
Sample Input:
4
Delhi-Ladakh
Bombay-Jaipur
Bengaluru-Bombay
Jaipur-Delhi
Sample Output:
Bengaluru-Ladakh
'''

#Code starts here
n = int(input())
list1 = []
for i in range(n):
    list1.append(input())

source_list = []
destination_list = []

for i in list1:
    x = i.split('-')
    x1 = x[0]
    x2 = x[1]

    source_list.append(x1)
    destination_list.append(x2)

for i in source_list:
    if i not in destination_list:
        source = i
        break
for i in destination_list:
    if i not in source_list:
        destination = i
        break

print(source, destination, sep = '-')
#Code ends here 

