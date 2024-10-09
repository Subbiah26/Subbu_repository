# Comments
# 1.single line comment=>(Example of single line comment= "#")
# 2.multi line comment ("""hello"""  or '''world''')
"""
This is a 
multiple line 
comments
Example
"""
"""
#  Python Keywords
# True,False,None =>(Should be capital)
# python is acase sensitive languag
"""
# Python Variables
#Rules:
"""
1.Starts with Alphabets or underscore ( a-z, A-Z, _ )
2.Can be a combination of Alphabets, Underscore & Number
3.Cannot be Keywords
"""
# Valid variables
"""
a = 100
A = "hai"
a1 = "Python"
_1 = "hello"
__ = 400
c_d = 50.55
_and = 600
"""
# Python Data Types

"""
# Integer - 1, 1244, -1234
a = 100
a1 = -100
# Float - 1.0, 123.324
b = 50.55
b1 = -50.55
# complex - 1+0j
# c = 100j
# string - “Hello world”, “a”, 'a'
d = "hello world"
d1 = "500"
#boolean - True, False
e = True
e1 = False
print(e1,type(e1))
"""
#  print() - Python standard function
"""
print(100+20)
print("hello world")
"""
# Escape sequencen

#print("Hello\\World\\")  # Hello\World\ => \\
#print('I\'m Manjunathan') # \' = print ='
#print("\"Hello\"\"world\"")  # "Hello""World" =>\"
#print("Hello\nWorld")  # Hello #World \n new line
#print("Hello\tworld")  # \t = tab

# end , sep
"""
print(1,2,3,4,5,sep="*")
print(6,7,8,9,10)
"""
#end
"""
print(1,2,3,4,5,end=" ")
print(6,7,8,9,10)
"""
# Trio : value, id, type
"""
a = 100
print(a,type(a),id(a))
"""
# Type casting
"""
a = float(800)
b = int(50.66)
c = bool("Hello")
c1 = int("500")
d = bool(" ")
d1 = bool(0)
d2 = bool("")  # ("" or 0)=> False
print(d2,type(d2))
"""
# Input from user
"""
num = 100
print("The value of num = ",num)
print("The value of num = ",num)
"""
"""
print("Enter a numbar :")
num = input()
print("The value of num =",num)
"""
"""
num = input("Enter a numbar :")
print("The value of num =",num)
"""
# Addition of two numbers

"""
num1 = input("Enter a numbar :")
x = int(num1)
print("The value of num1 =",x,type(x))

num2 = int(input("Enter a numbar :"))
print("The value of num2 =",num2,type(num2))

Total = x+num2
print("The Sum of =",Total)
"""
# del
"""
a = 100
b = 200
c = a+b
print(a)
del a,b
"""
"""
print("The value of c =",c)
print()
print("The value of a =",a)
print("The value of b =",b)
"""
"""
num1 = input("Enter a numbar :")
x = int(num1)
del num1
print("The value of x =",x,type(x))
print()
print("The value of num1 =",num1,type(num1))
"""
# Operators
# Arithmetic
# +,-,*,/,**,//,%
"""
print(10 + 3)   # 13
print(10 - 3)   #  7
print(10 * 3)   # 30
print(10 / 3)   # 3.333...
print(10 ** 3)  # Pow 10*10*10 = 1000
print(10 // 3)  # Q = 3
print(10 % 3)   # R = 1
"""
# Assignment Oprater
# =,+=,-=,*=,/=,**=,//=,%=
"""
a = 10
print(a)
a += 5    # a = a + 5=>   10 + 5= 15
print(a)
a *= 2   # 15 * 2 = 30
print(a)
b = 5
b += 10
print(b)
a %= 4
print(a)
"""

# Comparision Opreters  (T OR F)
# ==,!=,>,>=,<,<=
"""
print(10 == 10)  # T
print(10 != 10)  # F
print(10 > 10)   # F
print(10 >= 10)  # T
print(10 < 10)   # F
print(10 <= 10)  # T
"""
# Logocal Opreters
# and , or , not
"""
print(10 == 10 and 6 > 4)  # T and T = T
print(10 != 10 and 6 > 4)  # F and T = F
print(10 == 10 and 6 < 4)  # T and F = F
print(10 != 10 and 6 < 4)  # F and F = F

print(10 == 10 or 6 > 4)  # T or T = T
print(10 != 10 or 6 > 4)  # F or T = T
print(10 == 10 or 6 < 4)  # T or F = T
print(10 != 10 or 6 < 4)  # F or F = F

print(not 10 == 10)       # F
"""
# Python Collections
# List is a collection which is ordered and changeable. Allows duplicate  members. Denoted by []
"""
#          0   1    2     3      4     5     6  7      8     19  10  11 12  --- Index
mylist = [10,20.55,True,"hello",False,"hai",10,20.55,"hello",20.55,10,10,10]  # Allows duplicate 

print(mylist,type(mylist))
print(mylist[3])  # ordered
mylist[5]= "Welcome"
print(mylist)
"""
# Tuple is a collection which is ordered and unchangeable. Allows  duplicate members. Denoted by ()
"""
#          0   1    2     3      4     5     6  7      8     19  10  11 12  --- Index
mytuple = (10,20.55,True,"hello",False,"hai",10,20.55,"hello",20.55,10,10,10)
print(mytuple,type(mytuple))
print(mytuple[3])  # ordered
mytuple[5]= "Welcome"  # unchangeable
print(mytuple)
"""
# Set is a collection which is unordered and unindexed. No duplicate  members. Denoted by {}
"""
myset = {"A","A",10,10,20.55,20.55,False,True,False,True,10,"A"}  # No duplicate
print(myset)
"""

# If ,Else,Elif  (Decision  statement)

#Syntax:
   #1. If <condition>:
   #2. Elif <condition>:
   #3. else:
# Indentation
"""
a = 10
if a > 100:
    print(a,"is bigger then 100") 
    print("Hello If")
    print("code inside if condition")
print("This line Always works")
"""
"""
a = 100
if a > 100:
    print(a,"is bigger then 100") 
    print("Hello If")
    print("code inside if condition")

else:
    print(a,"is smaller then 100")
    print("code inside if condition")

print("This line Always works")
"""
"""
a = 101
if a > 100:
    print(a,"is bigger then 100") 
    print("Hello If")
    print("code inside if condition")
elif a == 100:
    print(a,"is equal to 100")

else:
    print(a,"is smaller then 100")
    print("code inside if condition")

print("This line Always works")
"""
"""
a = 10
if a > 50:
    print("a is bigger")
elif a == 20:
    print("a is 20")
elif a == 30:
    print("a is 30")
else:
    print("a is smaller")
"""
# While loop

# Syntax:
   #while <codition>:
"""
a = 1 # Start
while a <= 10:  # end
    print(a,end = " ")
    a += 1  # Jump
print("\nLoop Over")
"""
"""
a = 1
while a <= 5:
    print(a,end=" ")
    a += 1
print("\nLoop Over")
"""
# For loop
# Syntax:
 # for <v_Name> in <str/list/tuple/set>:
"""
for x in "hello world":   # letter by letter
    print(x,end="")
"""
"""
for x in [10,20,30.55,"hello","world"]: # Itam by itam
    print(x)
"""
# range() - Function
"""
for x in range(101):  # end before
print(x,end=" ")
"""   
"""
for x in range(10,21): # start wit end
    print(x,end=" ")
"""
"""
for x in range(50,101,10): # Jump
    print(x,end=" ")
"""
# Function  (User defind Function)
# Syntax:
# def <func_name>():
"""
def happy():
    print("I\'m Happy")
    print("Code reusebilty")
happy()
happy()
"""
"""
def happy():
    print("I\'m Happy")
    print("Code reusebilty")
def sad():
    print("I\'m sad")
    print("Code reusebilty")
sad()
happy()
sad()
"""
# Parameters
"""
def myfunc(x = 0,y = 0):  # x,y => Parameters
    print("X =",x)
    print("y =",y)
    print("The sum of =",x+y)

myfunc(10,20) # 10,20 => arguments
myfunc(y = 300)

myfunc(500,600)
"""
# mylist1 = [1,2,3,4,5]  # 120
# mylist2 = [5,6,7,8,9]

"""
def my_fact(mylist):
    x = 1
    for i in mylist:
        x = i*x
    return x
ans = my_fact(mylist1)
print(ans)

print(my_fact([5,6,7,8,9]))
print(my_fact([8,9,10,12]))
"""

# Modules & Library
# math
"""
import math
ans = math.factorial(10)
print(ans)
"""

"""
import math as m

print(m.sqrt(40))
print(m.sqrt(60))
"""
"""
from math import sqrt,factorial

print(sqrt(75))
print(factorial(4))
"""
import math
print(math.sqrt())
