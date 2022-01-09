# ANSWER 1
# taking input from user of three numbers
a = int(input('Enter first number :'))
b = int(input('Enter second number :'))
c = int(input('Enter third number :'))
# finding average of three numbers
x = (a + b + c) / 3
# printing the average
print('Average of given three numbers is :', x)


# ANSWER 2
# taking input from user for gross income and number of dependents
gi = int(input('Enter Gross Income :'))
nd = int(input('Enter number of dependents :'))
# finding total income(ti) of user
ti = gi - 10000 - (nd * 3000)
# finding tax payable by user
tx = (ti * 20) / 100
# printing the tax payable by user
print('Your payable tax is :', tx)


# ANSWER 3
# making an empty list
student = []
# taking input from user for various fields
sid = int(input('Enter your SID :'))
na = str(input('Enter your Name :'))
# using while loop to get a valid answer form user
i = 1
while i >= 1:
    ge = str(input('Enter your Gender F/M/U :'))
    if ge == 'F' or ge == 'M' or ge == 'U':
        break
    else:
        print('Enter a valid gender :')
    i = i + 1
cn = input('Enter name of course :')
cg = float(input('Enter CGPA :'))
# adding various inputs of user to the empty list
student.append(sid)
student.append(na)
student.append(ge)
student.append(cn)
student.append(cg)
# printing the final list
print(student)


# ANSWER 4
# making an empty list
stu = []
# using a for loop to fill the marks in the list
for i in range(0, 5):
    # taking input of marks from the user
    mark = float(input('Enter marks of student :'))
    # adding the input values to the list
    stu.append(mark)
# sort the value given by the user
stu.sort()
# printing the final list of marks
print('Marks of students', stu)


# ANSWER 5(a)
# making the list of given colours
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# removing colour black from the list
del color[3]
# printing the updated list
print(color)

# ANSWER 5(b)
# replacing colours black and pink of the list with purple
color[3: 5] = {'Purple'}
# printing the updated list
print(color)
