# ANSWER 1
line1 = 'Python is a case sensitive language'
# Finding length of input string
print(len(line1))
# reversing order of string
print(line1[::-1])
# Using slice to store a part of string
line2 = line1[10:27]
print(line2)
# Replacing a specific part of string
print(line1.replace('a case sensitive', 'object oriented'))
# Printing index number of a
print(line1.index('a') + 1)
# Removing all whitespaces
print(line1.replace(' ', ''))


# ANSWER 2
na = 'Ayush Aggarwal'
sid = 21104044
dep = 'Electrical'
cg = 9.7
# printing the required information in given pattern using string formatting
info = """Hey {} Here!
My SID is, {}
I am from {} department and my CGPA is {}"""
print(info.format(na, sid, dep, cg))


# ANSWER 3
# Giving values to variables to a and b
a = 56
b = 10
# Using different bitwise operators
print(a & b)
print(a | b)
print(a ^ b)
# Left shifting both a and b with 2 bits
print(a << 2, b << 2)
# Right shifting a and b by 2 and 4 bits respectively
print(a >> 2, b >> 4)


# ANSWER 4
# Taking input of three numbers
x = input('Enter first number')
y = input('Enter second number')
z = input('Enter third number')
# Finding the greatest number among the inputs given by user
if x >= y:
    if x >= z:
        print(x, 'is the greatest number')
    else:
        print(z, 'is the greatest number')
elif y > x:
    if y >= z:
        print(y, 'is the greatest number')
    else:
        print(z, 'is the greatest number')


# ANSWER 5
nam = input('Enter a line:')
# Checking if name is present in string
if 'name' in nam:
    print('Yes')
else:
    print('No')


# ANSWER 6
# Taking input from user for
l1 = float(input('Enter first length'))
l2 = float(input('Enter second length'))
l3 = float(input('Enter third length'))
# Checking for the condition of possibility of triangle
if l1 >= l2 + l3:
    print('No, it is not possible to form a triangle')
elif l2 >= l1 + l3:
    print('No, it is not possible to form a triangle')
elif l3 >= l2 + l1:
    print('No, it is not possible to form a triangle')
else:
    print('Yes, it is possible to form a triangle')
