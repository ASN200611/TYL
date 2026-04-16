# =============================================================================
# all_programs.py
# A combined collection of all Python programs from the TYL repository.
# Sections: 1.Input-Output, 2.Perfect Squares, 3.Leap Years, 4.Prime Numbers,
#           5.Number Based, 6.Number Based, 7.String Based, 8.String Based,
#           9.String Based, 10.Regular Expressions, 11.Classes and Objects,
#           Mock Test 12 through Mock Test 18
# Total files: ~120 Python programs covering input/output, number theory,
#              string manipulation, regular expressions, OOP, and mock tests.
# =============================================================================

##############################################################################
# SECTION: 1.Input-Output
##############################################################################

# ============================================================
# File: 1.Input-Output/1.py
# PURPOSE: Print only even numbers from a space-separated list of integers
# SAMPLE INPUT:  1 2 3 4 5 6
# SAMPLE OUTPUT: 2 4 6
# ============================================================

str1= input()
list1= str1.split()
list1 = [int(i) for i in list1]
list2=[]

for i in list1:
    if (i%2==0):
        list2.append(i)

print(*list2)

# ============================================================
# File: 1.Input-Output/2.py
# PURPOSE: Print only even numbers from a comma-separated list, output separated by commas
# SAMPLE INPUT:  1,2,3,4,5,6
# SAMPLE OUTPUT: 2,4,6
# ============================================================

str1=input()
list1=str1.split(',')
list1=[int(i) for i in list1]

even=[]

for i in list1:
    if (i%2==0):
        even.append(i)
    
print(*even,sep=',')

# ============================================================
# File: 1.Input-Output/3.py
# PURPOSE: Print only even numbers from a list entered one per line, output one per line
# SAMPLE INPUT:  4\n1\n2\n3\n4
# SAMPLE OUTPUT: 2\n4
# ============================================================

n = int(input())
list1=[]
for i in range(n):
    list1.append(int(input()))

even=[]

for i in list1:
    if (i%2==0):
        even.append(i)

print(*even,sep='\n')

# ============================================================
# File: 1.Input-Output/4.py
# PURPOSE: Print only odd-length words from a space-separated list of words
# SAMPLE INPUT:  Rohit Virat Hardik Bumra
# SAMPLE OUTPUT: Rohit Virat Bumra
# ============================================================

str1=input()
list1 = str1.split()

words=[]

for i in list1:
    if (len(i)%2!=0):
        words.append(i)

print(*words)

# ============================================================
# File: 1.Input-Output/5.py
# PURPOSE: Print only odd-length words from a comma-separated list, output separated by commas
# SAMPLE INPUT:  Rohit,Virat,Hardik,Bumra
# SAMPLE OUTPUT: Rohit,Virat,Bumra
# ============================================================

str1=input()
list1 = str1.split(',')

words=[]

for i in list1:
    if (len(i)%2!=0):
        words.append(i)

print(*words,sep=',')

# ============================================================
# File: 1.Input-Output/6.py
# PURPOSE: Print only odd-length words entered one per line, output one per line
# SAMPLE INPUT:  4\nRohit\nVirat\nHardik\nBumra
# SAMPLE OUTPUT: Rohit\nVirat
# ============================================================

n = int(input())
list1=[]
for i in range(n):
    list1.append(input())

odd=[]

for i in list1:
    if (len(i)%2!=0):
        odd.append(i)

print(*odd,sep='\n')

##############################################################################
# SECTION: 2.Perfect Squares
##############################################################################

# ============================================================
# File: 2.Perfect Squares/1.py
# PURPOSE: Check whether a given integer is a perfect square; return True or False
# SAMPLE INPUT:  9
# SAMPLE OUTPUT: True
# ============================================================

n=int(input())
def Is_Square(n):
    n1=n**0.5
    n2=int(n1)
    n3=n2**2
    if (n3==n):
        return True
    else:
        return False
print(Is_Square(n))

# ============================================================
# File: 2.Perfect Squares/2.py
# PURPOSE: Print only perfect squares from a comma-separated list; print 'NIL' if none
# SAMPLE INPUT:  1,2,3,4,5,6,7,8,9,10
# SAMPLE OUTPUT: 1\n4\n9
# ============================================================

str1=input()
list1=str1.split(',')
list1=[int(i) for i in list1]

def Is_Square(n):
    n1=n**0.5
    n2=int(n1)
    n3=n2**2
    if (n3==n):
        return True
    else:
        return False

list2=[]
for i in list1:
    if (Is_Square(i)==True):
        list2.append(i)

if len(list2)==0:
    print ('NIL')
    
print(*list2,sep='\n')

# ============================================================
# File: 2.Perfect Squares/3.py
# PURPOSE: Generate all perfect squares within a given interval; print 'NIL' if none
# SAMPLE INPUT:  10,50
# SAMPLE OUTPUT: 16\n25\n36\n49
# ============================================================

def Is_Square(n):
    n1=n**0.5
    n2=int(n1)
    n3=n2**2
    if (n3==n):
        return True
    else:
        return False

str1=input()
list1=str1.split(',')
list1=[int(i) for i in list1]
list2=[]

for  i in range(list1[0],list1[1]+1):
    if (Is_Square(i)==True):
        list2.append[i]

if len(list2)==0:
    print('NIL')
else:
    print(*list2,sep='\n')

# ============================================================
# File: 2.Perfect Squares/4.py
# PURPOSE: Generate the next 10 perfect squares starting from a given number
# SAMPLE INPUT:  9
# SAMPLE OUTPUT: 9,16,25,36,49,64,81,100,121,144
# ============================================================

def Is_Square(x):
    import math
    if int(math.sqrt(x))==(x**0.5):
        return True
    else:
        return False

n=int(input())
list1=[]

while len(list1)<10:
    if Is_Square(n):
        list1.append(n)
    n+=1

print(*list1,sep=',')

##############################################################################
# SECTION: 3.Leap Years
##############################################################################

# ============================================================
# File: 3.Leap Years/1.py
# PURPOSE: Check whether a given year is a leap year; return True or False
# SAMPLE INPUT:  100
# SAMPLE OUTPUT: False
# ============================================================

def is_leap(year):
    if (year % 400 == 0) and (year % 100 == 0):
        return True
    elif (year % 4 ==0) and (year % 100 != 0):
        return True 
    else:
        return False

print(is_leap())

# ============================================================
# File: 3.Leap Years/2.py
# PURPOSE: Print only leap years from a comma-separated list; print 'NIL' if none
# SAMPLE INPUT:  100,104,108,400,404,408
# SAMPLE OUTPUT: 104,108,400,404,408
# ============================================================

str1=input()
list1=str1.split(',')
list1=[int(i) for i in list1]  

def is_leap(year):
    if (year % 400 == 0) and (year % 100 == 0):
        return True
    elif (year % 4 ==0) and (year % 100 != 0):
        return True 
    else:
        return False

list2=[]
for i in list1:
    if (is_leap(i)==True):
        list2.append(i)

if len(list2)==0:
    print('NIL')
   
print(*list2,sep=',')

# ============================================================
# File: 3.Leap Years/3.py
# PURPOSE: Find all leap years in a given interval [lower, upper]
# SAMPLE INPUT:  100\n120
# SAMPLE OUTPUT: 104\n108\n112\n116\n120
# ============================================================

lower=int(input())
upper=int(input())
def leap(year):
    if (year%4!=0):
        return False
    else:
        if (year%400==0):
            return True
        elif (year%100==0):
            return False
        else:
            return True
        
for i in range(lower,upper+1):
    if (leap(i)==True):
        print(i)

# ============================================================
# File: 3.Leap Years/4.py
# PURPOSE: Print the next 10 leap years starting from a given year
# SAMPLE INPUT:  100
# SAMPLE OUTPUT: 104,108,112,116,120,124,128,132,136,140
# ============================================================

n=int(input())
list1=[]

def leap(year):
    if (year%4!=0):
        return False
    else:
        if (year%400==0):
            return True
        elif (year%100==0):
            return False
        else:
            return True
        
while (len(list1)<10):
    if (leap(n)==True):
        list1.append(n)
    n+=1

print(*list1,sep=',')

##############################################################################
# SECTION: 4.Prime Numbers
##############################################################################

# ============================================================
# File: 4.Prime Numbers/1.py
# PURPOSE: Check whether a given number is prime; return True or False
# SAMPLE INPUT:  5
# SAMPLE OUTPUT: True
# ============================================================

num=int(input())

def Fun_Prime(num):
    if num<2:
        return False
    elif (num==2):
        return True
    else:
        for i in range (2,num):
            if (num%i==0):
                return False
        return True
        
print(Fun_Prime(num))

# ============================================================
# File: 4.Prime Numbers/2.py
# PURPOSE: Print only prime numbers from a comma-separated list; print 'NIL' if none
# SAMPLE INPUT:  1,2,3,4,5,6,7,8
# SAMPLE OUTPUT: 2,3,5,7
# ============================================================

str1=input()
list1=str1.split(',')
list1=[int(i) for i in list1]
list2=[]

def Prime(num):
    if num<2:
        return False
    elif (num==2):
        return True
    else:
        for i in range (2,num):
            if (num%i==0):
                return False
        return True
    
for i in list1:
    if Prime(i)==True:
        list2.append(i)

if len(list2)==0:
    print ('Nil')
    
print(*list2,sep=',')

# ============================================================
# File: 4.Prime Numbers/3.py
# PURPOSE: Find all prime numbers within a given interval
# SAMPLE INPUT:  11 19
# SAMPLE OUTPUT: 11,13,17,19
# ============================================================

str1=input()
list1=str1.split()
list1=[int(i) for i in list1]
list2=[]
def Prime(num):
    if num<2:
        return False
    elif (num==2):
        return True
    else:
        for i in range (2,num):
            if (num%i==0):
                return False
        return True
    
for i in range(list1[0],list1[1]+1):
    if (Prime(i)==True):
        list2.append(i)

print(*list2,sep=',')

# ============================================================
# File: 4.Prime Numbers/4.py
# PURPOSE: Generate the next 10 prime numbers starting from a given number
# SAMPLE INPUT:  5
# SAMPLE OUTPUT: 5\n7\n11\n13\n17\n19\n23\n29\n31\n37
# ============================================================

n=int(input())
list1=[]

def Prime(num):
    if num<2:
        return False
    elif (num==2):
        return True
    else:
        for i in range (2,num):
            if (num%i==0):
                return False
        return True

while (len(list1)<10):
    if Prime(n)==True:
        list1.append(n)
    n=n+1
print(*list1,sep='\n')

##############################################################################
# SECTION: 5.Number Based
##############################################################################

# ============================================================
# File: 5.Number Based/1.py
# PURPOSE: Print the odd factors of a number in ascending order
# SAMPLE INPUT:  10
# SAMPLE OUTPUT: 1 5
# ============================================================

n=int(input())
list1=[]
for i in range(1,n+1):
    if (n%i==0) and (i%2!=0):
        list1.append(i)
print(*list1,sep=' ')

# ============================================================
# File: 5.Number Based/2.py
# PURPOSE: Remove duplicates, skip multiples of 3, print unique numbers in ascending order (entered one per line)
# SAMPLE INPUT:  6\n10\n11\n12\n10\n11\n12
# SAMPLE OUTPUT: 10\n11
# ============================================================

n=int(input())
list1=[]
list2=[]
for i in range(n): 
    list1.append(int(input()))
for i in list1:
    if i not in list2 and i%3!=0:
        list2.append(i)
    
print(*list2,sep='\n')

# ============================================================
# File: 5.Number Based/3.py
# PURPOSE: Print only non-repeated numbers from a list entered one per line; print "None" if all repeat
# SAMPLE INPUT:  6\n1\n2\n3\n3\n2\n4
# SAMPLE OUTPUT: 1\n4
# ============================================================

n=int(input())
list1=[]
list2=[]
for i in range(n):
    list1.append(int(input()))
for i in list1:
    if list1.count(i)==1:
        list2.append(i)
if len(list2)==0:
    print("None")
else:
    print(*list2,sep='\n')

# ============================================================
# File: 5.Number Based/4.py
# PURPOSE: Form a new number with LSD in ones place and digit count in tens place
# SAMPLE INPUT:  247
# SAMPLE OUTPUT: 37
# ============================================================

n=int(input())
l=len(str(n))
m=n%10
new=str(l)+str(m)
print(new)

# ============================================================
# File: 5.Number Based/5.py
# PURPOSE: Compute the LCM of two numbers
# SAMPLE INPUT:  6 4
# SAMPLE OUTPUT: 12
# ============================================================

str1=input()
list1=str1.split()
list1=[int(i) for i in list1]
a=list1[0]
b=list1[1]
def LCM(n1,n2):
    n3=max(n1,n2)
    n4=min(n1,n2)
    for i in range(1,(n3*n4)+1):
        if i%n3==0 and i%n4==0:
            return i
print(LCM(a,b))

# ============================================================
# File: 5.Number Based/6.py
# PURPOSE: Compute the GCD of two numbers
# SAMPLE INPUT:  12\n8
# SAMPLE OUTPUT: 4
# ============================================================

num1=int(input()) 
num2=int(input()) 
def GCD(n1,n2):
    larger=max(n1,n2)
    smaller=min(n1,n2)
    for i in range(1,smaller+1):
        if (n1%i==0) and (n2%i==0):
            gcd=i
    return gcd
            
print(GCD(num1,num2)) 

# ============================================================
# File: 5.Number Based/7.py
# PURPOSE: Check whether a given number is an Armstrong number; print True or False
# SAMPLE INPUT:  153
# SAMPLE OUTPUT: True
# ============================================================

n=int(input())
def Is_Armstrong(n):
    l=len(str(n))
    sum=0
    for i in (str(n)):
        sum=sum+(int(i)**l)
    if sum==n:
        return True
    else:
        return False
print(Is_Armstrong(n)) 

# ============================================================
# File: 5.Number Based/8.py
# PURPOSE: Check whether a given number is a Spy number (sum of digits == product of digits)
# SAMPLE INPUT:  1412
# SAMPLE OUTPUT: True
# ============================================================

n=int(input())
def Spy(n):
    s=str(n)
    sum=0
    product=1
    for i in s:
        sum=sum+int(i)
        product=product*int(i)
    if product==sum:
        print("True")
    else:
        print("False")
Spy(n) 

# ============================================================
# File: 5.Number Based/9.py
# PURPOSE: Convert a decimal number to its binary representation
# SAMPLE INPUT:  11
# SAMPLE OUTPUT: 1011
# ============================================================

n=int(input())
str1=''
while(n>0):
    r=n%2
    str1=str(r)+str1
    n=n//2
print(str1)

# ============================================================
# File: 5.Number Based/10.py
# PURPOSE: Convert a binary string to its equivalent decimal number
# SAMPLE INPUT:  1001
# SAMPLE OUTPUT: 9
# ============================================================

binary=input()
binary=binary[::-1]
decimal=0
for i in range(len(binary)):
    decimal = decimal + (int(binary[i])*(2**i))
print(decimal)

##############################################################################
# SECTION: 6.Number Based
##############################################################################

# ============================================================
# File: 6.Number Based/1.py
# PURPOSE: Generate a Fibonacci series of a given length
# SAMPLE INPUT:  5
# SAMPLE OUTPUT: 0,1,1,2,3
# ============================================================

n=int(input()) 
def Fun_Fib(n):
    if n==1:
        list1=[0]
    elif n==2:
        list1=[0,1]
    else:
        list1=[0,1]
        while(len(list1)<n):
            next=list1[-1]+list1[-2]
            list1.append(next)
    print(*list1,sep=',')

Fun_Fib(n) 

# ============================================================
# File: 6.Number Based/2.py
# PURPOSE: Generate Fibonacci series numbers up to a given value N
# SAMPLE INPUT:  5
# SAMPLE OUTPUT: 0,1,1,2,3,5
# ============================================================

n=int(input()) 
def Fun_Fib(n):
    if n==0:
        list1=[0,]
    elif n==1:
        list1=[0,1,1]
    else:
        list1=[0,1,1]
        next=list1[-1]+list1[-2]
        while(next<=n):
            list1.append(next)
            next=list1[-1]+list1[-2]
    print(*list1,sep=',')
Fun_Fib(n) 

# ============================================================
# File: 6.Number Based/3.py
# PURPOSE: Check whether a given number is a Fibonacci number; return True or False
# SAMPLE INPUT:  5
# SAMPLE OUTPUT: True
# ============================================================

n=int(input())
def Is_Fib(n):
    if n==0:
        return True
    elif n==1:
        return True
    else:
        list1=[0,1]
        next=list1[-1]+list1[-2]
        while(next<=n):
            if next==n:
                return True
            else:
                list1.append(next)
                next=list1[-1]+list1[-2]
        if next==n:
            return True
        else:
            return False
print(Is_Fib(n))

# ============================================================
# File: 6.Number Based/4.py
# PURPOSE: Print Fibonacci numbers within a given interval [lower, upper]
# SAMPLE INPUT:  5\n34
# SAMPLE OUTPUT: 5 8 13 21 34
# ============================================================

lower=int(input())
upper=int(input())
if lower==0 and upper==1:
    list1=[0,1,1]
else:
    list1=[0,1]
    next=list1[-1]+list1[-2]
    list2=[]
    while(next<=upper):
        if next>=lower:
            list2.append(next)
        next=list1[-1]+list1[-2]
        list1.append(next)  
print(*list2)

# ============================================================
# File: 6.Number Based/5.py
# PURPOSE: Find product of list based on position of 5: product of all, right-of-5, or -1
# SAMPLE INPUT:  1 2 5 3 4
# SAMPLE OUTPUT: 12
# ============================================================

str1=input()
list1=str1.split()
list1=[int(i) for i in list1]
if 5 not in list1:
    prod=1
    for i in list1:
        prod=prod*i
    print(prod)
else:
    index1=list1.index(5)
    if index1+1==len(list1):
        print(-1)
    else:
        prod=1
        for i in range(index1+1,len(list1)):
            if i!=5:
                prod=prod*i
        print(prod)

# ============================================================
# File: 6.Number Based/6.py
# PURPOSE: Print primes up to N that equal the sum of consecutive primes starting from 2
# SAMPLE INPUT:  50
# SAMPLE OUTPUT: 5\n17\n41
# ============================================================

n=int(input())
def prime(n):
    if (n<2):
        return False
    elif (n==2):
        return True
    else:
        for i in range(2,n):
            if n%i==0:
                return False
        return True
list1=[]
for i in range(2,n+1):
    if prime(i)==True:
        list1.append(i)
list2=[]
sum=0
for i in list1:
    sum=sum+i
    if sum in list1 and sum!=2:
        list2.append(sum)
print(*list2,sep='\n')

##############################################################################
# SECTION: 7.String Based
##############################################################################

# ============================================================
# File: 7.String Based/1.py
# PURPOSE: Print names that start with R/r and end with H/h; print -1 if none found
# SAMPLE INPUT:  Raveesh,rajesh,mahesh,Rakesh
# SAMPLE OUTPUT: Raveesh\nrajesh\nRakesh
# ============================================================

str1=input()
list1=str1.split(',')
list2=[]
for i in list1:
    if i[0]=='R' or i[0]=='r':
        if i[-1]=='H' or i[-1]=='h':
            list2.append(i)   

if (len(list2)==0):
    print(-1)
else:
    print(*list2,sep='\n')

# ============================================================
# File: 7.String Based/2.py
# PURPOSE: Print only palindromes from a list of words; print "Nil" if none
# SAMPLE INPUT:  4\nradar\nnation\nteam\nmadam
# SAMPLE OUTPUT: radar\nmadam
# ============================================================

n=int(input())
list1=[]
list2=[]
for i in range (0,n):
    list1.append(input())
for i in list1:
    if i==i[::-1]:
        list2.append(i)
if len(list2)==0:
    print('Nil')
else:
    print(*list2,sep='\n')

# ============================================================
# File: 7.String Based/3.py
# PURPOSE: Count movies both people like (both 1) and both dislike (both 0) from binary strings
# SAMPLE INPUT:  101011000\n011001010
# SAMPLE OUTPUT: 2,3
# ============================================================

str1=input()
str2=input()
likes=0
dislikes=0
for i in range(len(str1)):
    if str1[i]=='1' and str2[i]=='1':
        likes+=1
    elif str1[i]=='0' and str2[i]=='0':
        dislikes+=1
print(likes,dislikes,sep=',')

# ============================================================
# File: 7.String Based/4.py
# PURPOSE: Compute net bank account balance from a transaction log of deposits and withdrawals
# SAMPLE INPUT:  4\nD 500\nD 1000\nW 200\nW 300
# SAMPLE OUTPUT: B 1000
# ============================================================

n=int(input())
list1=[]
for i in range(n):
    list1.append(input())
bal=0
for i in list1:
    if i[0]=='D':
        bal=bal+int(i[2:])
    elif i[0]=='W':
        bal=bal-int(i[2:])
print('B',bal)

# ============================================================
# File: 7.String Based/5.py
# PURPOSE: Remove spaces from a string, find the length, and output whether it is even or odd
# SAMPLE INPUT:  vtu cmrit ece
# SAMPLE OUTPUT: 11 odd
# ============================================================

str1=input()
str2=str1.split()
str3=''.join(str2)
if len(str3)%2==0:
    print(len(str3),'even')
else:
    print(len(str3),'odd')

# ============================================================
# File: 7.String Based/6.py
# PURPOSE: Print only the common words between two sentences; print "Nil" if none
# SAMPLE INPUT:  cmrit ece third sem\nvtu cmrit ece
# SAMPLE OUTPUT: cmrit ece
# ============================================================

str1=input()
str2=input()
list1=str1.split()
list2=str2.split()
list3=[]
for i in list1:
    if i in list2:
        list3.append(i)
if len(list3)!=0:
    print(*list3)
else:
    print('Nil')

# ============================================================
# File: 7.String Based/7.py
# PURPOSE: Remove repeated words of length greater than 5 from a sentence
# SAMPLE INPUT:  cmrit ece ece department department
# SAMPLE OUTPUT: cmrit ece ece department
# ============================================================

str1=input()
list1=str1.split()
list2=[]
for i in list1:
    if (i in list2 and len(i)>5):
        continue
    else:
        list2.append(i)
print(*list2)

# ============================================================
# File: 7.String Based/8.py
# PURPOSE: Remove non-repeated words of length greater than 5 from a sentence
# SAMPLE INPUT:  cmr institute institute of technology
# SAMPLE OUTPUT: cmr institute institute of
# ============================================================

str1=input()
list1=str1.split()
list2=[]

for i in list1:
    if list1.count(i)==1 and len(i)>5:
        list2.append(i)

print(*list2)

# ============================================================
# File: 7.String Based/9.py
# PURPOSE: Extract odd-length words and pad with * on right to length 10 if under 10 chars
# SAMPLE INPUT:  Hi are you going to bengaluru
# SAMPLE OUTPUT: are*******\nyou*******\ngoing*****\nbengaluru*
# ============================================================

str1=input()
list1=str1.split()

for i in list1:
    if len(i)%2!=0:
        if len(i)<10:
            i=i+('*'*(10-len(i)))
            print(i)

##############################################################################
# SECTION: 8.String Based
##############################################################################

# ============================================================
# File: 8.String Based/1.py
# PURPOSE: Count alphabetical characters, digits, spaces, and special characters in a string
# SAMPLE INPUT:  Cmrit Ece 2000 @#$
# SAMPLE OUTPUT: 8,4,3,3
# ============================================================

str1=input()
alphabet=0
digits=0
spaces=0
specialchar=0
for i in str1:
    if i.isalpha():
        alphabet+=1
    elif i.isdigit():
        digits+=1
    elif i.isspace():
        spaces+=1
    else:
        specialchar+=1
print(alphabet,digits,spaces,specialchar,sep=',')

# ============================================================
# File: 8.String Based/2.py
# PURPOSE: Count the number of vowels and consonants in a string
# SAMPLE INPUT:  Cmrit Ece 2000
# SAMPLE OUTPUT: 3,5
# ============================================================

str1=input()
counter_c=0
counter_v=0
for i in str1:
    if i.isalpha():
        if i in 'AEIOUaeiou':
            counter_v+=1
        else:
            counter_c+=1
print(counter_v,counter_c,sep=',')

# ============================================================
# File: 8.String Based/3.py
# PURPOSE: Count uppercase and lowercase letters in a string
# SAMPLE INPUT:  Cmrit Ece 2000
# SAMPLE OUTPUT: 2,6
# ============================================================

str1=input()
counter_upper=0
counter_lower=0
for i in str1:
    if i.isupper():
        counter_upper+=1
    elif i.islower():
        counter_lower+=1
print(counter_upper,counter_lower,sep=',')

# ============================================================
# File: 8.String Based/4.py
# PURPOSE: Remove vowels from every string in a list
# SAMPLE INPUT:  4\ncmrit\nece\nvtu\naecs
# SAMPLE OUTPUT: cmrt\nc\nvt\ncs
# ============================================================

n=int(input())
list1=[]
list2=[]
for i in range(0,n):
    list1.append(input())

for i in list1:
    str2=''
    for j in i:
        if j not in 'AEIOUaeiou':
            str2=str2+j
    list2.append(str2)
print(*list2,sep='\n')

# ============================================================
# File: 8.String Based/5.py
# PURPOSE: Find the word with the highest number of vowels; first word wins on tie
# SAMPLE INPUT:  4\nraveesh\nkaveesh\nmahesh\nrajesh
# SAMPLE OUTPUT: raveesh
# ============================================================

n=int(input())
list1=[]
for i in range(n):
    list1.append(input())
count_past=0
for i in list1:
    count_present=0
    for j in i:
        if j in 'AEIOUaeiou':
            count_present+=1
    if count_present>count_past:
        req_word=i
        count_past=count_present
print(req_word)

# ============================================================
# File: 8.String Based/6.py
# PURPOSE: Validate passwords: >=2 lowercase, >=2 uppercase, >=1 digit, no spaces, >=1 special char, 8-16 chars
# SAMPLE INPUT:  5\naaBB #$1\naaBB#$1\naaBB#$12\naaBB#$12345678910\nBBaa*&1234
# SAMPLE OUTPUT: aaBB#$12\nBBaa*&1234
# ============================================================

n=int(input())
list1=[]
for i in range(n):
    list1.append(input())

def pw(str1):
    if len(str1)<8 or len(str1)>16:
        return False
    else:
        c_lower=0
        c_upper=0
        c_digit=0
        c_space=0
        c_character=0
        for i in str1:
            if i.isupper():
                c_upper+=1
            elif i.islower():
                c_lower+=1
            elif i.isdigit():
                c_digit+=1
            elif i.isspace():
                c_space+=1
            else:
                c_character+=1
                c_upper+=1
        if c_lower>=2 and c_upper>=2 and c_digit>=1 and c_space==0 and c_character>=1:
            return True 
        else:
            return False

list2=[]
for i in list1:
    if pw(i)==True:
        list2.append(i)

print(*list2,sep='\n')

# ============================================================
# File: 8.String Based/7.py
# PURPOSE: Print only anagram words from a string (words with same letters as adjacent word)
# SAMPLE INPUT:  listen silent silent listen linest
# SAMPLE OUTPUT: listen silent linest
# ============================================================

str1=input()
list1=str1.split()
list2=[]
for i in range((len(list1))-1):
    if sorted(list1[i])==sorted(list1[i+1]):
        if list1[i] not in list2:
            list2.append(list1[i])
        if list1[i+1] not in list2:
            list2.append(list1[i+1])
print(*list2)

# ============================================================
# File: 8.String Based/8.py
# PURPOSE: Check if a string is a Heterogram (no letter appears more than once); return True or False
# SAMPLE INPUT:  the big dwarf only jumps
# SAMPLE OUTPUT: True
# ============================================================

str1=input()
a=0
for i in str1:
    if i!=' ' and str1.count(i)>1:
        a=1
        break
if a==0:
    print(True)
else:
    print(False)

##############################################################################
# SECTION: 9.String Based
##############################################################################

# ============================================================
# File: 9.String Based/1.py
# PURPOSE: Print only wonderful strings (made of exactly 3 different letters); print "None" if none
# SAMPLE INPUT:  abca pqrs tuvt xyz
# SAMPLE OUTPUT: abca tuvt xyz
# ============================================================

str1=input()
list1=str1.split()
list2=[]
for i in list1:
    if len(set(i))==3:
        list2.append(i)
if len(list2)!=0:
    print(*list2)
else:
    print('None')

# ============================================================
# File: 9.String Based/2.py
# PURPOSE: Print strings that start with "Hello" and end with a digit
# SAMPLE INPUT:  4\nHello good morning 9\nHello how are you 8\nHi Hello\nWassup 7
# SAMPLE OUTPUT: Hello good morning 9\nHello how are you 8
# ============================================================

n=int(input())
list1=[]
list2=[]
for i in range(n):
    list1.append(input())

for i in list1:
    if i.startswith("Hello") or i.endswith("0123456789"):
        list2.append(i)

print(*list2,sep='\n')

# ============================================================
# File: 9.String Based/3.py
# PURPOSE: Find the winner of a vote count; alphabetical order breaks ties; display winner and votes
# SAMPLE INPUT:  raveesh mahesh raveesh mahesh rajesh rakesh rajesh rakesh raveesh mahesh
# SAMPLE OUTPUT: mahesh,3
# ============================================================

str1=input()
list1=str1.split()
dict1={}
for i in list1:
    key=i
    dict1[key]=list1.count(i)

max_votes=max(dict1.values())
for i in sorted(dict1.keys()):
    if dict1[i]==max_votes:
        winner=i
        break

print(winner,max_votes,sep=',')

# ============================================================
# File: 9.String Based/4.py
# PURPOSE: Find the parking row with the most empty slots (0s); print "None" if no spaces
# SAMPLE INPUT:  4\n10101100\n11001111\n10000111\n10010110
# SAMPLE OUTPUT: 1
# ============================================================

n = int(input())
list1=[]
list2=[]
for i in range(n):
    list1.append(input())
for i in list1:
    c=i.count("0")
    list2.append(c)
m=max(list2)
if m==0:
    print('None')
else:
    for i in range(len(list2)):
        if m==list2[i]:
            print(i+1)
            break

# ============================================================
# File: 9.String Based/5.py
# PURPOSE: Compute engine number as sum of all digit characters in a car number plate string
# SAMPLE INPUT:  KA57AB2056
# SAMPLE OUTPUT: 25
# ============================================================

str1=input()
num=0
for i in str1:
    if i.isdigit():
        num+=int(i)
print(num)

# ============================================================
# File: 9.String Based/6.py
# PURPOSE: Extract employee name and company name from a list of email IDs
# SAMPLE INPUT:  4\nsachin@tcs.com\nvirat@infosys.com\nrohit@wipro.com\nrahul@reliance.com
# SAMPLE OUTPUT: sachin,tcs\nvirat,infosys\nrohit,wipro\nrahul,reliance
# ============================================================

n=int(input())
list1=[]
for i in range(n):
    list1.append(input())

for i in list1:
    list2=i.split('@')
    list3=list2[1].split('.')
    print(list2[0],list3[0],sep=',')

# ============================================================
# File: 9.String Based/7.py
# PURPOSE: Build a dictionary of numbers as keys and their frequency as values, sorted by key
# SAMPLE INPUT:  2,2,4,4,2,6,6,4,6,8,8,8
# SAMPLE OUTPUT: {2: 3, 4: 3, 6: 3, 8: 3}
# ============================================================

str1=input()
list1=str1.split(',')
list1=[int(i) for i in list1]
dict1={}
for i in sorted(list1):
    key=i
    dict1[key]=list1.count(i)
print(dict1)

# ============================================================
# File: 9.String Based/8.py
# PURPOSE: Convert Roman numerals to their equivalent decimal number
# SAMPLE INPUT:  IX
# SAMPLE OUTPUT: 9
# ============================================================

str1=input()
rom={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
dec=0
for i in range(len(str1)):
    present=rom[str1[i]]
    past=rom[str1[i-1]]
    if present>past and i!=0:
        dec=dec+present-2*past
    else:
        dec=dec+present
print(dec)

# ============================================================
# File: 9.String Based/9.py
# PURPOSE: Find the largest even number that can be formed from digits in a string; print 'Nil' if not possible
# SAMPLE INPUT:  cmrit@1234
# SAMPLE OUTPUT: 4312
# ============================================================

str1 = input()
l1 = []

for i in str1:
    if i.isdigit():
        l1.append(int(i))

l1 = sorted(l1, reverse=True)

for i in range(1, len(l1) + 1):
    if l1[-i] % 2 == 0:
        even_digit = l1[-i]
        l1.remove(even_digit)
        l1.append(even_digit)
        break
else:
    print('Nil')
    exit()

n = ''.join(map(str, l1))

if int(n) % 2 == 0:
    print(n)
else:
    print('Nil')

# ============================================================
# File: 9.String Based/10.py
# PURPOSE: Compute similarity value of two strings as (2 * matching positions) / total letters
# SAMPLE INPUT:  cmrit\ncrmi
# SAMPLE OUTPUT: 0.444
# ============================================================

str1=input()
str2=input()
total=len(str1)+len(str2)
m=min(len(str1),len(str2))
similar=0
for i in range(m):
    if str1[i]==str2[i]:
        similar+=1
similarity_value=(2*similar)/total
print('%0.3f'%similarity_value)

##############################################################################
# SECTION: 10.Regular Expressions
##############################################################################

# ============================================================
# File: 10.Regular Expressions/1.py
# PURPOSE: Validate USNs from a list (format: 1 digit, 2 alpha, 2 digits, 2 alpha, 3 digits); print 'Nil' if none valid
# SAMPLE INPUT:  4\n1CR22EC285\nCR22EC285\n1CR22EC2894\n1CR22EC286
# SAMPLE OUTPUT: 1CR22EC285\n1CR22EC286
# ============================================================

import re
n=int(input())
list1=[]
list2=[]
for i in range(n):
    list1.append(input())

sp=re.compile('^(\d){1}[A-Z]{2}(\d){2}[A-Z]{2}(\d){3}$')

for i in list1:
    if sp.search(i):
        list2.append(i)

if len(list2)!=0:
    print(*list2,sep='\n')
else:
    print('Nil')

# ============================================================
# File: 10.Regular Expressions/2.py
# PURPOSE: Validate PAN numbers (5 letters + 4 digits + 1 letter) from a list; print 'Nil' if none valid
# SAMPLE INPUT:  4\nBDDCH6708X\nBDDCH6708\nBDCH6708X\nXVVFG9807T
# SAMPLE OUTPUT: BDDCH6708X\nXVVFG9807T
# ============================================================

import re
n = int(input())
list1=[]
list2=[]
for i in range(n):
    list1.append(input())

sp=re.compile('^[A-Z]{5}(\d){4}[A-Z]{1}$')

for i in list1:
    if sp.search(i):
        list2.append(i)

if len(list2)!=0:
    print(*list2,sep='\n')
else:
    print('Nil')

# ============================================================
# File: 10.Regular Expressions/3.py
# PURPOSE: Validate vehicle numbers (2 letters + 2 digits + 2 letters + 4 digits) from a list
# SAMPLE INPUT:  4\nKA63HJ2024\nKA63HJ202\nA63HJ2024\nKA63HJ2032
# SAMPLE OUTPUT: KA63HJ2024\nKA63HJ2032
# ============================================================

import re
n = int(input())
list1=[]
list2=[]
for i in range(n):
    list1.append(input())

sp=re.compile('^[A-Z]{2}(\d){2}[A-Z]{2}(\d){4}$')

for i in list1:
    if sp.search(i):
        list2.append(i)

if len(list2)!=0:
    print(*list2,sep='\n')
else:
    print('Nil')

# ============================================================
# File: 10.Regular Expressions/4.py
# PURPOSE: Extract valid phone numbers in format ddd-dddd-dddd from a sentence; print 'Nil' if none
# SAMPLE INPUT:  CMRIT Bengaluru's ECE Dept's phone number is 080-2847-4463
# SAMPLE OUTPUT: 080-2847-4463
# ============================================================

str1=input()
import re
list1=str1.split()
list2=[]
sp=re.compile('^(\d){3}\-(\d){4}\-(\d){4}$')

for i in list1:
    if sp.search(i):
        list2.append(i)

if len(list2)!=0:
    print(*list2)
else:
    print('Nil')

# ============================================================
# File: 10.Regular Expressions/5.py
# PURPOSE: Validate URLs (http/https/ftp) from a list; print 'Nil' if none valid
# SAMPLE INPUT:  6\nhttps://www.yahoo.com\nhttp://blog.hubspot.com\nhttps://www.karnatakajobs.com\nabc:\\\\www.india.com\nhttps://www.cmrit.ac.in\nftp://internet.address.edu
# SAMPLE OUTPUT: https://www.yahoo.com\nhttp://blog.hubspot.com\nhttps://www.karnatakajobs.com\nhttps://www.cmrit.ac.in\nftp://internet.address.edu
# ============================================================

n = int(input())
list1=[]
list2=[]
for i in range(n):
    list1.append(input())

import re
sp=re.compile('^(http|https|ftp)://([a-z])+(\.)([a-z])+(\.)([a-z]){2,3}(\.)?(([a-z]){2,3})?$') 
for i in list1:
    if sp.search(i):
        list2.append(i)

if len(list2)!=0:
    print(*list2,sep='\n')
else:
    print('Nil')

# ============================================================
# File: 10.Regular Expressions/6.py
# PURPOSE: Extract valid mobile numbers in format +CC-NNNNNNNNNN from a sentence; print 'Nil' if none
# SAMPLE INPUT:  CMRIT's mobile number is +91-9078912345
# SAMPLE OUTPUT: +91-9078912345
# ============================================================

str1=input()
import re
list1=str1.split()
list2=[]
sp=re.compile('^\+(\d){2}\-(\d){10}$')

for i in list1:
    if sp.search(i):
        list2.append(i)

if len(list2)!=0:
    print(*list2)
else:
    print('Nil')

# ============================================================
# File: 10.Regular Expressions/7.py
# PURPOSE: Extract valid email IDs from a sentence; print "Nil" if none found
# SAMPLE INPUT:  My email ID is sachin.t@gmail.com and my friend's email ID is virat_k@cmrit.ac.in
# SAMPLE OUTPUT: sachin.t@gmail.com\nvirat_k@cmrit.ac.in
# ============================================================

str1=input()
list1=str1.split()
list2=[]
import re 

sp=re.compile('^([a-zA-Z0-9._%-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})$')
for i in list1:
    if sp.search(i):
        list2.append(i)

if len(list2)!=0:
    print(*list2,sep='\n')
else:
    print('Nil')

# ============================================================
# File: 10.Regular Expressions/8.py
# PURPOSE: Convert dates from yyyy-mm-dd to dd-mm-yyyy format; leave dd-mm-yyyy dates unchanged
# SAMPLE INPUT:  2016-01-20 2020-05-25 12-10-2008 01-12-2007
# SAMPLE OUTPUT: 20-01-2016 25-05-2020 12-10-2008 01-12-2007
# ============================================================

import re
str1=input()
list1=str1.split()
sp=re.compile('^(\d){2}-(\d){2}-(\d){4}$')
list2=[]
for i in list1:
    if sp.search(i):
        list2.append(i)
    else:
        str2=i[8:]+'-'+i[5:7]+'-'+i[0:4]
        list2.append(str2)

print(*list2)

# ============================================================
# File: 10.Regular Expressions/9.py
# PURPOSE: Validate IP addresses (0-255 per octet, no leading zeros) from a list; print 'Nil' if none valid
# SAMPLE INPUT:  4\n192.168.0.1\n292.168.0.1\n192.168.02.1\n192.16.0.1
# SAMPLE OUTPUT: 192.168.0.1\n192.16.0.1
# ============================================================

n=int(input())
import re
list1=[]
for i in range(n):
    list1.append(input())
sp=re.compile('^((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$')
list2=[]
for i in list1:
    if sp.search(i):
        list2.append(i)

if len(list2)!=0:
    print(*list2,sep='\n')
else:
    print('Nil')

##############################################################################
# SECTION: 11.Classes and Objects
##############################################################################

# ============================================================
# File: 11.Classes and Objects/1.py
# PURPOSE: Circle class with methods to calculate area and circumference
# SAMPLE INPUT:  3
# SAMPLE OUTPUT: 28.274333882308138\n18.84955592153876
# ============================================================

class circle:
    def __init__(self,r):
        self.radius=r
    def area(self):
        import math
        A=(math.pi)*(self.radius**2)
        return A
    def circumference(self):
        import math
        C=2*(math.pi)*self.radius
        return C

r=int(input())
c=circle(r)

print(c.area())
print(c.circumference())

# ============================================================
# File: 11.Classes and Objects/2.py
# PURPOSE: Complex number class with method to add two complex numbers
# SAMPLE INPUT:  2,4\n1,3
# SAMPLE OUTPUT: 3 7
# ============================================================

class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def add(self, other):
        return Complex(self.real+other.real, self.imaginary+other.imaginary)


if __name__ == "__main__":
    r1, i1 = map(int, input().split(','))
    r2, i2 = map(int, input().split(','))
    
    result = Complex(r1, i1).add(Complex(r2, i2))
    
    print(result.real, result.imaginary)

# ============================================================
# File: 11.Classes and Objects/3.py
# PURPOSE: Complex number class with methods to find magnitude and phase (to 4 decimal places)
# SAMPLE INPUT:  2,3
# SAMPLE OUTPUT: 3.6056\n0.9828
# ============================================================

class complex:
    def __init__(self,r,i):
        self.real=r
        self.imaginary=i
    def magnitude(self):
        M=(self.real**2+self.imaginary**2)**0.5
        return round(M,4)
    def phase(self):
        import math
        P=math.atan2(self.imaginary,self.real)
        return round(P,4)

str1=input()
list1=str1.split(',')
c=complex(float(list1[0]),float(list1[1]))

print(c.magnitude())
print(c.phase())

# ============================================================
# File: 11.Classes and Objects/4.py
# PURPOSE: Student class with methods to calculate percentage and SGPA from 3 subject marks (out of 50)
# SAMPLE INPUT:  35,42,44
# SAMPLE OUTPUT: 80.67\n8.82
# ============================================================

str1=input()
list1=str1.split(',')
list1=[int(i) for i in list1]

class Student:
    def __init__(self,m1,m2,m3):
        self.marks1=m1
        self.marks2=m2
        self.marks3=m3
    def Percentage(self):
        per = (self.marks1+self.marks2+self.marks3)*(100/150)
        return round(per,2)
    def SGPA(self):
        sgpa=((self.Percentage()/10)+0.75)
        if sgpa>10:
            return 10.00
        return round(sgpa,2)


Raveesh = Student(list1[0],list1[1],list1[2])

print(Raveesh.Percentage())
print(Raveesh.SGPA())

# ============================================================
# File: 11.Classes and Objects/5.py
# PURPOSE: Employee class with methods to calculate monthly salary (90% of actual) and remaining leaves
# SAMPLE INPUT:  100000 2
# SAMPLE OUTPUT: 90000\n10
# ============================================================

str1=input()
list1=str1.split()
list1=[int(i) for i in list1]

class Employee:
    def __init__(self,s,l):
        self.salary=s
        self.leaves=l
    def Salary(self):
        month_sal=self.salary*0.9
        return int(month_sal)
    def Leaves(self):
        l = 12-self.leaves
        return l

Raveesh = Employee(list1[0],list1[1])

print(Raveesh.Salary())
print(Raveesh.Leaves())

# ============================================================
# File: 11.Classes and Objects/6.py
# PURPOSE: Rectangle class with methods to calculate area and diagonal length
# SAMPLE INPUT:  2,3
# SAMPLE OUTPUT: 6\n3.61
# ============================================================

class rectangle():
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    def area(self):
        A=self.length*self.breadth
        return round(A,2)
    def diagonal(self):
        D=(((self.length)**2)+((self.breadth)**2))**0.5
        return round(D,2)

s=input()
list1=s.split(',')
rect=rectangle(int(list1[0]),int(list1[1]))

print(rect.area())
print(rect.diagonal())

##############################################################################
# SECTION: Mock Test 12
##############################################################################

# ============================================================
# File: Mock Test 12/1.py
# PURPOSE: Stack class with push, pop, peek, size, and is_empty methods
# SAMPLE INPUT:  2,4,6,8
# SAMPLE OUTPUT: 8\n6\n3\nFalse
# ============================================================

x=[int(i) for i in input().split(',')]

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    def size(self):
        return len(self.items)

    def is_empty(self):
        return len(self.items) == 0

s=Stack()

for i in x:
    s.push(i)

print(s.pop())

print(s.peek())

print(s.size())

print(s.is_empty())

# ============================================================
# File: Mock Test 12/2.py
# PURPOSE: Print strings where parentheses ((), {}, []) are properly matched
# SAMPLE INPUT:  4\n[ra(vee{s}h)]\nra(vee{s}h)]\n]ra(vee{s}h)[\n[ra{vee(s)h}]
# SAMPLE OUTPUT: [ra(vee{s}h)]\n[ra{vee(s)h}]
# ============================================================

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

##############################################################################
# SECTION: Mock Test 13
##############################################################################

# ============================================================
# File: Mock Test 13/1.py
# PURPOSE: Determine optimal buy and sell days for maximum stock profit
# SAMPLE INPUT:  90,100,80,94,110,85,60
# SAMPLE OUTPUT: 3,5
# ============================================================

x = [int(i) for i in input().split(',')]

profit = 0

for i in range(len(x)-1):
    for j in range(i+1,len(x)):
        if x[j]-x[i]>profit:
            profit = x[j]-x[i]
            buy = i+1
            sell = j+1
print(buy, sell, sep=',')

# ============================================================
# File: Mock Test 13/2.py
# PURPOSE: Find the hackathon winner by highest marks; least time breaks ties
# SAMPLE INPUT:  50,80,70,80,80,75\n45,35,55,50,45,35
# SAMPLE OUTPUT: 2
# ============================================================

x = [int(i) for i in input().split(',')]
y = [int(i) for i in input().split(',')]
max1 = max(x)
list1 = []
list2 = []

for i in range(len(x)):
    if x[i] == max1:
        list1.append(i)
        list2.append(y[i])

mini = min(list2)
ind = y.index(mini)
print(ind+1)

# ============================================================
# File: Mock Test 13/3.py
# PURPOSE: Select 3 consecutive days with least average probability of rain for a cricket tournament
# SAMPLE INPUT:  0.5,0.6,0.4,0.4,0.5,0.3,0.3
# SAMPLE OUTPUT: 5,6,7
# ============================================================

list1 = [float(i) for i in input().split(',')]

avg = 1
for i in range(len(list1)-2):
    if ((list1[i]+list1[i+1]+list1[i+2])/3)<avg:
        days = [i+1,i+2,i+3]
        avg = (list1[i]+list1[i+1]+list1[i+2])/3

print(*days, sep = ',')

# ============================================================
# File: Mock Test 13/4.py
# PURPOSE: Find the contiguous subarray with the maximum sum
# SAMPLE INPUT:  2,-1,3,-2,1,-2
# SAMPLE OUTPUT: 2,-1,3
# ============================================================

x = [int(i) for i in input().split(',')]
max_sum = 0

for j in range(len(x)):
    for i in range(j+1, len(x)+1):
        subarray = x[j:i]
        if sum(subarray)>max_sum:
            required_array = subarray
            max_sum = sum(required_array)

print(*required_array, sep = ',')

# ============================================================
# File: Mock Test 13/5.py
# PURPOSE: Find the longest sequence of consecutive numbers in an array
# SAMPLE INPUT:  2,8,7,9,3
# SAMPLE OUTPUT: 7,8,9
# ============================================================

x = [int(i) for i in input().split(',')]
x = sorted(x)

def continuous_array(x):
    for i in range(len(x)-1):
        if x[i+1]!=x[i]+1:
            return False
    return True

max_len = 0
for i in range(len(x)):
    for j in (i+1, len(x)):
        temp_array = x[i:j+1]
        if continuous_array(temp_array) and len(temp_array)>max_len:
            required_array = temp_array
            max_len = len(temp_array)

print(*required_array,sep=',')

# ============================================================
# File: Mock Test 13/6.py
# PURPOSE: Find the longest substring without repeating characters
# SAMPLE INPUT:  abcabcbb
# SAMPLE OUTPUT: abc
# ============================================================

str1 = input()
max_length = 0
for i in range(len(str1)):
    for j in range(i, len(str1)):
        substring = str1[i:j+1]
        if len(substring) == len(set(substring)) and len(substring)>max_length:
            required_substring = substring
            max_length = len(required_substring)

print(required_substring)

# ============================================================
# File: Mock Test 13/7.py
# PURPOSE: Find two numbers in an array whose sum equals the target; print 'NO' if none
# SAMPLE INPUT:  2,6,5,8,1\n9
# SAMPLE OUTPUT: 8,1
# ============================================================

list1 = [int(i) for i in input().split(',')]
n = int(input())
flag = 0

for j in range(len(list1)-1):
    for i in range(j+1, len(list1)):
        if list1[j]+list1[i]==n:
            print(list1[j],list1[i], sep = ',')
            flag = 1

if flag == 0:
    print('NO')

# ============================================================
# File: Mock Test 13/8.py
# PURPOSE: Find three numbers in an array whose sum equals the target; print 'NO' if none
# SAMPLE INPUT:  2,6,5,8,1\n9
# SAMPLE OUTPUT: 2,6,1
# ============================================================

list1 = [int(i) for i in input().split(',')]
n = int(input())
flag = 0

for k in range(0,len(list1)-2):
    for j in range(k+1, len(list1)-1):
        for i in range(j+1, len(list1)):
            if list1[k]+list1[j]+list1[i]==n:
                print(list1[k],list1[j],list1[i], sep = ',')
                flag = 1

if flag == 0:
    print('NO')

# ============================================================
# File: Mock Test 13/9.py
# PURPOSE: Find the longest contiguous increasing subarray
# SAMPLE INPUT:  See code
# SAMPLE OUTPUT: See code
# ============================================================

x = [int(i) for i in input().split(',')]

def increasing(x):
    for i in range(len(x)-1):
        if x[i]>=x[i+1]:
            return False
    return True

max_length = 0
for i in range(len(x)):
    for j in range(i+1, len(x)):
        temp_array = x[i:j+1]
        if increasing(temp_array) and len(temp_array)>max_length:
            required_array = temp_array
            max_length = len(required_array)

print(*required_array, sep = ',')

# ============================================================
# File: Mock Test 13/10.py
# PURPOSE: Check if differences between adjacent elements are strictly increasing (expanding array)
# SAMPLE INPUT:  See code
# SAMPLE OUTPUT: True or False
# ============================================================

x = [int(i) for i in input().split(',')]

def function(x):
    for i in range(2, len(x)):
        diff1 = x[i]-x[i-1]
        diff2 = x[i-1]-x[i-2]
        if diff1<=diff2:
            return False
    return True

print(function(x))

# ============================================================
# File: Mock Test 13/11.py
# PURPOSE: Find the missing number in an array of integers from N1 to N2
# SAMPLE INPUT:  5,6,8,9
# SAMPLE OUTPUT: 7
# ============================================================

x = [int(i) for i in input().split(',')]
for i in range(x[0],x[-1]):
    if i not in x:
        print(i)

# ============================================================
# File: Mock Test 13/12.py
# PURPOSE: Find the contiguous subarray of length k with the maximum sum
# SAMPLE INPUT:  -1,2,3,3,4,5,-1,3
# SAMPLE OUTPUT: 3,4,5
# ============================================================

x = [int(i) for i in input().split(',')]
k = int(input())
max_sum = 0
for i in range(len(x)-k+1):
    if sum(x[i:i+k])>max_sum:
        max_sum = sum(x[i:i+k])
        required_array = x[i:i+k]

print(*required_array, sep=',')

# ============================================================
# File: Mock Test 13/13.py
# PURPOSE: Find the kth largest and nth smallest element in an array
# SAMPLE INPUT:  4,3,2,5,6,7\n3\n2
# SAMPLE OUTPUT: 5\n3
# ============================================================

x = [int(i) for i in input().split(',')]
k = int(input())
n = int(input())
x = sorted(x)
print(x[-k])
print(x[n-1])

# ============================================================
# File: Mock Test 13/14.py
# PURPOSE: Find two gift prices whose total equals the given budget
# SAMPLE INPUT:  50,110,150,200,180,230\n330
# SAMPLE OUTPUT: 150,180
# ============================================================

x = [int(i) for i in input().split(',')]
budget = int(input())

for i in range(len(x)-1):
    for j in range(i+1,len(x)):
        if x[i]+x[j]==budget:
            print(f'{x[i]},{x[j]}')

##############################################################################
# SECTION: Mock Test 14
##############################################################################

# ============================================================
# File: Mock Test 14/1.py
# PURPOSE: Linear search for an element in a list; print index or "Not Found"
# SAMPLE INPUT:  2,3,3,1,5,6\n3
# SAMPLE OUTPUT: 2
# ============================================================

list1 = [int(i) for i in input().split(',')]
n = int(input())

def linear_search(list1,n):
    for i in range(len(list1)):
        if list1[i] == n:
            return(i)
    return("Not Found")

print(linear_search(list1,n))

# ============================================================
# File: Mock Test 14/2.py
# PURPOSE: Binary search for an element in a sorted list; print index or "Not Found"
# SAMPLE INPUT:  2,4,6,8,10,12,14,16,18,20,22,24,26\n20
# SAMPLE OUTPUT: 9
# ============================================================

list1 = [int(i) for i in input().split(',')]
n = int(input())

def binary_search(list1, n):
    lower_index = 0
    upper_index = len(list1)-1
    while(lower_index<=upper_index):
        mid_index = (lower_index+upper_index)//2
        if list1[mid_index]==n:
            return mid_index
        elif list1[mid_index]<n:
            lower_index = mid_index+1
        elif list1[mid_index]>n:
            upper_index = mid_index+1
    return("Not Found")

print(binary_search(list1,n))

# ============================================================
# File: Mock Test 14/3.py
# PURPOSE: Sort a list of integers in ascending order using Bubble Sort
# SAMPLE INPUT:  10,8,6,4,2
# SAMPLE OUTPUT: 2,4,6,8,10
# ============================================================

list1 = [int(i) for i in input().split(',')]

def Bubble_Sort(list1):
    for j in range(len(list1)-1):
        for i in range(len(list1)-1):
            if list1[i]>list1[i+1]:
                list1[i], list1[i+1] = list1[i+1], list1[i]
    print(*list1, sep = ',')

Bubble_Sort(list1)

##############################################################################
# SECTION: Mock Test 15
##############################################################################

# ============================================================
# File: Mock Test 15/1.py
# PURPOSE: Print ascending staircase number pattern (1; 1 2; 1 2 3; ...)
# SAMPLE INPUT:  5
# SAMPLE OUTPUT: 1\n1 2\n1 2 3\n1 2 3 4\n1 2 3 4 5
# ============================================================

n = int(input())
list1 = []
for i in range(1,n+1):
    list1.append(i)
    print(*list1)

# ============================================================
# File: Mock Test 15/2.py
# PURPOSE: Print descending staircase number pattern (1 2 3 4; 1 2 3; 1 2; 1)
# SAMPLE INPUT:  4
# SAMPLE OUTPUT: 1 2 3 4\n1 2 3\n1 2\n1
# ============================================================

n = int(input())
list1 = []
for i in range(1,n+1):
    list1.append(i)
for i in range(n,0,-1):
    list1.append(i)
    print(*list1[0:i])

# ============================================================
# File: Mock Test 15/3.py
# PURPOSE: Print number pattern where row i contains i copies of i
# SAMPLE INPUT:  5
# SAMPLE OUTPUT: 1\n2 2\n3 3 3\n4 4 4 4\n5 5 5 5 5
# ============================================================

n = int(input())

for i in range(1,n+1):
    list1 = []
    for j in range(1,i+1):
        list1.append(i)
    print(*list1)

# ============================================================
# File: Mock Test 15/4.py
# PURPOSE: Print descending pattern where row i has (n-i+1) copies of i
# SAMPLE INPUT:  3
# SAMPLE OUTPUT: 1 1 1\n2 2\n3
# ============================================================

n = int(input())
a = n
for i in range(1, n+1):
    list1 = []
    for j in range(a):
        list1.append(i)
    print(*list1, sep=' ')
    a = a-1

# ============================================================
# File: Mock Test 15/5.py
# PURPOSE: Print multiplication table pattern where row i shows i*1, i*2, ..., i*i
# SAMPLE INPUT:  4
# SAMPLE OUTPUT: 1\n2 4\n3 6 9\n4 8 12 16
# ============================================================

n = int(input())
for i in range(1,n+1):
    list1 = []
    for j in range(1, i+1):
        list1.append(i*j)
    print(*list1)

# ============================================================
# File: Mock Test 15/6.py
# PURPOSE: Print upper-triangular multiplication table pattern (row i: i*1 to i*(n-i+1))
# SAMPLE INPUT:  4
# SAMPLE OUTPUT: 1 2 3 4\n2 3 6\n3 6\n4
# ============================================================

n = int(input())
a = n
for i in range(1,n+1):
    list1 = []
    for j in range(1,a+1):
        list1.append(i*j)
    print(*list1)
    a -= 1

# ============================================================
# File: Mock Test 15/7.py
# PURPOSE: Print full n x n multiplication table
# SAMPLE INPUT:  4
# SAMPLE OUTPUT: 1 2 3 4\n2 4 6 8\n3 6 9 12\n4 8 12 16
# ============================================================

n = int(input())
for i in range(1, n+1):
    list1 = []
    for j in range(1, n+1):
        list1.append(i*j)
    print(*list1)

# ============================================================
# File: Mock Test 15/8.py
# PURPOSE: Print multiplication table with odd-number row multipliers (1, 3, 5, 7...)
# SAMPLE INPUT:  4
# SAMPLE OUTPUT: 1 2 3 4\n3 6 9 12\n5 10 15 20\n7 14 21 28
# ============================================================

n = int(input())
a = 1
for i in range(1,n+1):
    list1 = []
    for j in range(1,n+1):
        list1.append(a*j)
    print(*list1)
    a += 2

# ============================================================
# File: Mock Test 15/9.py
# PURPOSE: Print ascending star triangle pattern (* ; * * ; * * * ; ...)
# SAMPLE INPUT:  5
# SAMPLE OUTPUT: *\n* *\n* * *\n* * * *\n* * * * *
# ============================================================

n = int(input())
list1 = []
for i in range(n):
    list1.append('*')
    print(*list1)

# ============================================================
# File: Mock Test 15/10.py
# PURPOSE: Print descending star triangle pattern (* * * * * ; * * * * ; ...)
# SAMPLE INPUT:  5
# SAMPLE OUTPUT: * * * * *\n* * * *\n* * *\n* *\n*
# ============================================================

n = int(input())
list1 = []
for i in range(n):
    list1.append('*')
for i in range(n, 0, -1):
    print(*list1[0:i])

# ============================================================
# File: Mock Test 15/11.py
# PURPOSE: Print right-aligned descending star triangle pattern with spaces on left
# SAMPLE INPUT:  5
# SAMPLE OUTPUT: * * * * *\n  * * * *\n    * * *\n      * *\n        *
# ============================================================

n = int(input())
list1 = []
for i in range(n):
    list1.append('*')
print(*list1)
for i in range(n):
    list1[i] = ' '
    print(*list1)

##############################################################################
# SECTION: Mock Test 16
##############################################################################

# ============================================================
# File: Mock Test 16/1.py
# PURPOSE: Determine the color of a chess board square given its coordinate (e.g. d6)
# SAMPLE INPUT:  d6
# SAMPLE OUTPUT: Black
# ============================================================

str1 = input()
if str1[0] in 'aceg' and int(str1[1])%2==0:
    print('White')
elif str1[0] in 'aceg' and int(str1[1])%2!=0:
    print('Black')
elif str1[0] in 'bdfh' and int(str1[1])%2==0:
    print('Black')
else:
    print('White')

# ============================================================
# File: Mock Test 16/2.py
# PURPOSE: For each day in a temperature array, find the number of days to wait for a warmer day
# SAMPLE INPUT:  25,26,24,28,27
# SAMPLE OUTPUT: 1,2,1,0,0
# ============================================================

list1 = [int(i) for i in input().split(',')]
list2 = []

for i in range(len(list1)-1):
    d = 0
    flag = 0
    for j in range(i+1, len(list1)):
        if list1[j]>list1[i]:
            d = d+1
            flag = 1
            break
        else:
            d = d+1
    if flag == 0:
        list2.append(0)
    else:
        list2.append(d)
list2.append(0)

print(*list2, sep=',')

# ============================================================
# File: Mock Test 16/3.py
# PURPOSE: Determine if each kid can have the most candies after receiving extra candies
# SAMPLE INPUT:  2,3,5,1,3\n3
# SAMPLE OUTPUT: True,True,True,False,True
# ============================================================

list1 = [int(i) for i in input().split(',')]
n = int(input())
list2 = []
for i in list1:
    if (i+n) >= max(list1):
        list2.append(True)
    else:
        list2.append(False)

print(*list2,sep=',')

# ============================================================
# File: Mock Test 16/4.py
# PURPOSE: Plant n tree saplings in empty spaces ensuring no adjacent plantings; print False if not possible
# SAMPLE INPUT:  1,0,1,0,0,0,1,0,0\n2
# SAMPLE OUTPUT: 1,0,1,0,1,0,1,0,1
# ============================================================

list1 = [int(i) for i in input().split(',')]
n = int(input())

if list1[0] == 0 and list1[1]==0:
    list1[0] = 1
    n = n-1

for i in range(1,len(list1)-1):
    if n == 0:
        break
    else:
        if list1[i-1]==0 and list1[i]==0 and list1[i+1]==0:
            list1[i] = 1
            n = n-1

if n>0 and list1[-1]==0 and list1[-2]==0:
    list1[-1]=1
    n = n-1

if n>0:
    print(False)
else:
    print(*list1,sep=',')

# ============================================================
# File: Mock Test 16/5.py
# PURPOSE: Decode an encoded string (e.g. "a2b3c1" -> "aabbbc")
# SAMPLE INPUT:  a2b3c1
# SAMPLE OUTPUT: aabbbc
# ============================================================

str1 = input()
list1 = str1.split()
s=''
for i in range(0,len(str1),2):
    for j in range(int(str1[i+1])):
        s = s+str1[i]

print(s)

# ============================================================
# File: Mock Test 16/6.py
# PURPOSE: Encode a string using run-length encoding (e.g. "aaabbcaa" -> "a3b2c1a2")
# SAMPLE INPUT:  aaabbcaa
# SAMPLE OUTPUT: a3b2c1a2
# ============================================================

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

##############################################################################
# SECTION: Mock Test 17
##############################################################################

# ============================================================
# File: Mock Test 17/1.py
# PURPOSE: Count the number of islands (isolated 1s flanked by 0s) in an array, excluding first and last
# SAMPLE INPUT:  1,0,0,1,0,1,0,1,0
# SAMPLE OUTPUT: 3
# ============================================================

list1 = [int(i) for i in input().split(',')]
count = 0
for i in range(1, len(list1)-1):
    if list1[i-1]==0 and list1[i]==1 and list1[i+1]==0:
        count += 1

print(count)

# ============================================================
# File: Mock Test 17/2.py
# PURPOSE: Check if it is possible to cross a river by jumping between stone positions with a max jump length
# SAMPLE INPUT:  0,3,5,8,10,13\n3
# SAMPLE OUTPUT: True
# ============================================================

list1 = [int(i) for i in input().split(',')]
d = int(input())
for i in range(len(list1)-1):
    if (list1[i+1]-list1[i])>d:
        print(False)
        break
else:
    print(True)

# ============================================================
# File: Mock Test 17/3.py
# PURPOSE: Find the highest altitude reached by a biker from an array of altitude gains
# SAMPLE INPUT:  0,5,-2,-4,3,4,-1
# SAMPLE OUTPUT: 6
# ============================================================

list1 = [int(i) for i in input().split(',')]
list2 = []
sum = 0
for i in list1:
    sum = sum+i
    list2.append(sum)
print(max(list2))

# ============================================================
# File: Mock Test 17/4.py
# PURPOSE: Remove overlapping auditorium booking intervals, keeping non-overlapping ones
# SAMPLE INPUT:  4\n3-5\n5-7\n6-8\n8-10
# SAMPLE OUTPUT: 3-5\n6-8
# ============================================================

n = int(input())
list1 = []
for i in range(n):
    list1.append(input())
list2 = [list1[0]]
for i in range(1,n):
    a = list1[i]
    c = a.split('-')
    b = list2[-1].split('-')
    if (int(c[0])>int(b[-1])):
        list2.append(a)

print(*list2,sep='\n')

# ============================================================
# File: Mock Test 17/5.py
# PURPOSE: Determine the initial source and final destination city from a list of travel pairs
# SAMPLE INPUT:  4\nDelhi-Ladakh\nBombay-Jaipur\nBengaluru-Bombay\nJaipur-Delhi
# SAMPLE OUTPUT: Bengaluru-Ladakh
# ============================================================

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

# ============================================================
# File: Mock Test 17/6.py
# PURPOSE: Find 3 coin heaps (denomination * count) that maximize total money collected
# SAMPLE INPUT:  1,2,5,10,20\n10,3,5,2,1
# SAMPLE OUTPUT: 2,3,4
# ============================================================

list1 = [int(i) for i in input().split(',')]
list2 = [int(i) for i in input().split(',')]
list3 = []

for i in range(len(list1)):
    list3.append(list1[i]*list2[i])

sum1 = 0

for i in range(len(list1)-2):
    for j in range(i+1, len(list1)-1):
        for k in range(j+1, len(list1)):
            if (list3[i]+list3[j]+list3[k])>sum1:
                index1 = i
                index2 = j
                index3 = k
                sum1 = list3[i]+list3[j]+list3[k]

print(index1, index2, index3, sep=',')

# ============================================================
# File: Mock Test 17/7.py
# PURPOSE: Find the fewest coins needed to make up a given amount using available denominations
# SAMPLE INPUT:  1,2,5,10\n14
# SAMPLE OUTPUT: 3
# ============================================================

list1 = [int(i) for i in input().split(',')]
n = int(input())
list1.sort(reverse = True)
count = 0

for i in list1:
    count = count+n//i
    n = n%i
    if n == 0:
        break

print(count)

# ============================================================
# File: Mock Test 17/8.py
# PURPOSE: Check if exact change can be given to all ticket customers (5/10/20 rupee notes)
# SAMPLE INPUT:  5,5,10,5,20
# SAMPLE OUTPUT: True
# ============================================================

list1 = [int(i) for i in input().split(',')]

def change(list1):
    fives = 0
    tens = 0
    twenties = 0
    for i in range(len(list1)):
        if list1[i] == 5:
            fives = fives + 1
        elif list1[i] == 10:
            tens = tens + 1
            if fives == 0:
                return False
            else:
                fives = fives - 1
        else:
            twenties = twenties - 1

            if fives >= 3:
                return True
            elif tens>=1 and fives>=1:
                return True
            else:
                return False

print(change(list1))

# ============================================================
# File: Mock Test 17/9.py
# PURPOSE: Find area of square formed by all matchsticks; print False if not possible
# SAMPLE INPUT:  See code
# SAMPLE OUTPUT: See code
# ============================================================

# (No implementation provided in source file)
pass

# ============================================================
# File: Mock Test 17/10.py
# PURPOSE: Print the first n rows of Pascal's triangle
# SAMPLE INPUT:  5
# SAMPLE OUTPUT: 1\n1 1\n1 2 1\n1 3 3 1\n1 4 6 4 1
# ============================================================

n = int(input())
list1 = [1]
list2 = [1,1]
if n==1:
    print(*list1)
elif n==2:
    print(*list1)
    print(*list2)
else:
    print(*list1)
    print(*list2)
    for i in range(2,n):
        list3 = []
        for j in range(i+1):
            list3.append(1)
        for j in range(1,i):
            list3[j]=list2[j]+list2[j-1]
        list2 = list3
        print(*list3)

# ============================================================
# File: Mock Test 17/11.py
# PURPOSE: Find two non-adjacent houses to rob for maximum money; return their indices
# SAMPLE INPUT:  100,200,150,20,10,30
# SAMPLE OUTPUT: 0,2
# ============================================================

list1 = [int(i) for i in input().split(',')]
profit = 0
for i in range(len(list1)-2):
    for j in range(i+2, len(list1)):
        if (list1[i]+list1[j])>profit:
            index1 = i
            index2 = j
            profit = list1[i]+list1[j]

print(index1, index2, sep=',')

##############################################################################
# SECTION: Mock Test 18
##############################################################################

# ============================================================
# File: Mock Test 18/1.py
# PURPOSE: Find the IPL team that wins Virat Kohli by having the highest bid
# SAMPLE INPUT:  RCB,CSK,MI,KKR,GT\n20,25,15,16,18
# SAMPLE OUTPUT: CSK,25
# ============================================================

list1 = input().split(',')
list2 = [int(i) for i in input().split(',')]
m = max(list2)
index1 = list2.index(m)
print(list1[index1], list2[index1], sep=',')

# ============================================================
# File: Mock Test 18/2.py
# PURPOSE: Print names and scores of top 3 batters in descending order of runs
# SAMPLE INPUT:  Rohit,Shubhman,Virat,Shreyas,Rahul,Hardik, Ravindra\n45,60,125,40,20,8,4
# SAMPLE OUTPUT: Virat,125\nShubhman,60\nRohit,45
# ============================================================

list1 = input().split(',')
list2 = [int(i) for i in input().split(',')]
list3 = sorted(list2)

max1 = list3[-1]
max2 = list3[-2]
max3 = list3[-3]

index1 = list2.index(max1)
index2 = list2.index(max2)
index3 = list2.index(max3)

print(list1[index1],max1,sep=',')
print(list1[index2],max2,sep=',')
print(list1[index3],max3,sep=',')

# ============================================================
# File: Mock Test 18/3.py
# PURPOSE: Compute the h-index of an author from an array of citation counts
# SAMPLE INPUT:  2,3,4,3,4,2,4,3,4,5,5
# SAMPLE OUTPUT: 4
# ============================================================

list1 = [int(i) for i in input().split(',')]
list2 = list(set(list1))
for i in list2:
    if list1.count(i)==i:
        h = i
print(h)

# ============================================================
# File: Mock Test 18/4.py
# PURPOSE: Print the nth row of Pascal's triangle as comma-separated values
# SAMPLE INPUT:  4
# SAMPLE OUTPUT: 1,3,3,1
# ============================================================

n = int(input())
list1 = [1]
list2 = [1,1]
if n==1:
    print(*list1,sep=',')
elif n==2:
    print(*list2,sep=',')
else:
    for i in range(2,n):
        list3 = []
        for j in range(i+1):
            list3.append(1)
        for j in range(1,i):
            list3[j]=list2[j]+list2[j-1]
        list2 = list3
print(*list3,sep=',')

# ============================================================
# File: Mock Test 18/5.py
# PURPOSE: Determine the last place a traveller can reach before running out of petrol
# SAMPLE INPUT:  Bengaluru,Chennai,Hyderabad,Amaravati,Bhopal,Jaipur,New Delhi\n50,60,40,80,90,120\n70,50,30,90,80,100
# SAMPLE OUTPUT: Jaipur
# ============================================================

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

# ============================================================
# File: Mock Test 18/6.py
# PURPOSE: Find the favorite singer (most appearances) from song and singer lists
# SAMPLE INPUT:  song1,song2,song3,song4,song5,song6,song7,song8\nsonu,arijit,vishal,arijit,sonu,arijit,sonu,sonu
# SAMPLE OUTPUT: sonu,4
# ============================================================

list1 = input().split(',')
list2 = input().split(',')
list3 = list(set(list2))
c = 0
for i in list3:
    if list2.count(i)>c:
        c = list2.count(i)
        fav = i
print(fav, c, sep = ',')
