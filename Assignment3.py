# ANSWER 1
# Taking an input string from user
line = input('Enter a String :')
# Creating blank dictionaries
alpha = {}
beta = {}
# Checking if string has single or multiple words
if ' ' in line:
    # Splitting multiple words and adding them to dictionary using for loop
    lin = line.split()
    for word in lin:
        if word in beta:
            beta[word] += 1
        else:
            beta[word] = 1
    # Printing occurrences of all words
    print('Occurrence of all word in given string is : \n' + str(beta))
else:
    # Using for loop to add alphabets in empty dictionary
    for i in line:
        if i in alpha:
            alpha[i] += 1
        else:
            alpha[i] = 1
    # Printing occurrences of all characters
    print('Occurrence of all characters in given string is : \n' + str(alpha))




# ANSWER 2
# Taking input from user for date
year = int(input('Enter a year :'))
month = int(input('Enter a month :'))
day = int(input('Enter a date :'))
# Checking if date entered by user is valid
if 1 <= month <= 12 and 1 <= day <= 31:
    # Checking for a leap year
    if year % 4 == 0:
        leap_year = True
    else:
        leap_year = False
    # Assigning length to various months
    if month in (1, 3, 5, 7, 9, 11):
        month_length = 31
    elif month == 2:
        if leap_year:
            month_length = 29
        else:
            month_length = 28
    else:
        month_length = 30
    # Checking if date entered by user is valid
    if day <= month_length:
        # Checking if new month is starting
        if day < month_length:
            day += 1
        else:
            day = 1
            # Checking for a new year
            if month == 12:
                month = 1
                year += 1
            else:
                month += 1
                # Printing the required result
        print('The next date is(in dd-mm-yyyy) :', (day, month, year))
    else:
        print('Enter a valid date')
else:
    print('Enter a valid date')





# Answer 3
# Creating empty list
lst = []
# Taking input for number of elements in list
num_elements = int(input('Enter number of elements in list :'))
# Using for loop for taking input of elements of list
for i in range(0, num_elements):
    num = int(input('Enter a number :'))
    y = num, num*num
    # Adding the element and its square to the list
    lst.append(y)
# Printing the final list
print(lst)




# ANSWER 4
# Taking input of grade from user
grade = int(input('Enter your grade(4-10) :'))
# Assigning specific statements to each valid grade
if grade == 10:
    print('Your grade is A+ and Outstanding Performance')
elif grade == 9:
    print('Your grade is A and Excellent Performance')
elif grade == 8:
    print('Your grade is B+ and Very Good Performance')
elif grade == 7:
    print('Your grade is B and Good Performance')
elif grade == 6:
    print('Your grade is C+ and Average Performance')
elif grade == 5:
    print('Your grade is C and Below Average Performance')
elif grade == 4:
    print('Your grade is D and Poor Performance')
else:
    print('Enter a valid grade')




# ANSWER 5
# Assigning the given string to a variable
line = 'ABCDEFGHIJK'
# Taking two variables for loop
i = 11
x = 0
# Using loop to get the desired pattern
while i > 0:
    print(' '*x, line[0: i])
    i -= 2
    x += 1




# ANSWER 6
# Creating an empty dictionary
d = {}
# Using while loop to add values in dictionary and using True condition to continue it
while True:
    nam = str(input('Enter student\'s name :'))
    sid = int(input('Enter student\'s SID :'))
    v = str(input('Do you want to add another value(Y/N) :'))
    # Putting sid as key and student name as value
    d[sid] = nam
    # Using while loop to get a valid input
    while v not in ('Y', 'N'):
        v = str(input('Do you want to add another value(Y/N) :'))
    if v == 'N':
        break
        # Printing the dictionary
print(d)
# Sorting dictionary using student name
d1 = sorted(d.items(), key=lambda item: item[1])
print(d1)
# Sorting dictionary using sid
d2 = sorted(d.items(), key=lambda item: item[0])
print(d2)
# Taking input from user for a student's sid and then printing his/her name
info = int(input('Enter SID of required Student :'))
print('Name of Student :', d.get(info))




# ANSWER 7
# Defining a function for fibonacci series
def fib(n):
    a = 0
    b = 1
    # Checking condition for a valid input
    if n <= 0:
        print('Incorrect Input')
    elif n == 1:
        print(a)
    else:
        print(a)
        print(b)
        add = 1
        # Using for loop to get fibonacci series
        for i in range(2, n):
            c = a + b
            a = b
            b = c
            print(c)
            # Adding all terms of the series
            add += c
        # Finding average of the given series and printing it
        avg = add/num
        print('Average of series till given terms is :', avg)
# Taking input from user for number of terms in fibonacci series
num = int(input('Enter number of terms of fibonacci series :'))
# Putting the value in function and executing it
fib(num)




# ANSWER 8
# Making three given sets
set1 = {1, 2, 3, 4, 5}
set2 = {2, 4, 6, 8}
set3 = {1, 5, 9, 13, 17}
# Creating a new set of all elements that are in set1 and set2 but not both
s1 = set1.symmetric_difference(set2)
print(s1)
# Creating a new set of all elements that are in only one of the three sets set1, set2 and set3
s2 = set1.symmetric_difference(set2).symmetric_difference(set3)
print(s2)
# Creating a new set of elements that are in exactly two of the sets set1, set2 and set3
s3 = set1.intersection(set2).union(set2.intersection(set3)).union(set3.intersection(set1))
print(s3)
# Creating a new set of all integers in the range 1 to 10 that are not in set1
set4 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
s4 = set4.difference(set1)
print(s4)
# Creating a new set of all integers in the range 1 to 10 that are not in set1, set2 and set3
s5 = set4.difference(set1.union(set2.union(set3)))
print(s5)
