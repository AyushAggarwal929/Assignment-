# ANSWER 1
# Defining a recursive function for tower of hanoi
def tower_of_hanoi(n, source, destination, auxiliary):
    if n == 1:
        # Moving disc 1 from one rod to another
        print('Move disc 1 from source', source, 'to destination', destination)
        return
    # Using the defined function inside itself
    tower_of_hanoi(n - 1, source, auxiliary, destination)
    print('Move disc', n, 'from source', source, 'to destination', destination)
    tower_of_hanoi(n - 1, auxiliary, destination, source)
# Executing the function with 3 discs and rods named A, B and C
tower_of_hanoi(3, 'A', 'B', 'C')




# ANSWER 2
# A) Printing pascal's triangle using recursive method
# Defining a fumction for pascal's triangle
def pascals_triangle(n):
    # Checking if input entered by user is valid
    if n <= 0:
        print('Enter a valid input')
    elif n == 1:
        return [1]
    else:
        new_line = [1]
        last_line = pascals_triangle(n - 1)
        # Using for loop to get the sequence
        for i in range(len(last_line) - 1):
            new_line.append(last_line[i] + last_line[i + 1])
        # Printing the sequence
        print(' ' * (rows - len(last_line)), last_line)
        new_line += [1]
        return new_line
    # Taking input from user for length of series
rows = int(input('Enter the length of series :'))
# Executing the function
print(pascals_triangle(rows))


# B) Printing pascal's triangle using iterative method
# Taking input from user for number of rows in tower of hanoi
n = int(input('Enter the length of series :'))
# Checking if number entered by user is valid
if n <= 0:
    print('Enter a valid number')
else:
    for i in range(1, n + 1):
        # Using for loop for initial space before the preceding lines
        for j in range(0, n - i + 1):
            print(' ', end='')
        # First value in a line is always 1
        a = 1
        # Using for loop to create the sequence
        for j in range(1, i + 1):
            print(' ', a, sep='', end='')
            a = a * (i - j) // j
        # Using a empty print to shift the pattern to next line
        print()




# ANSWER 3
# Taking input from the user
n1 = int(input("\nEnter first number :"))
n2 = int(input("Enter second number :"))
# Defining quotient and remainder function
def q_and_r_finder(x, y):
    quotient = (x // y)
    remainder = (x % y)
    return quotient, remainder
# Making a list of return values
list1 = list(q_and_r_finder(n1, n2))
# a1 = Quotient
quo = list1[0]
# a2 = Remainder
rem = list1[1]
# Printing the quotient and remainder
print(f"\nThe quotient when {n1} is divided by {n2} is {quo}")
print(f"The remainder when {n1} is divided by {n2} is {rem}")

# Ques 3a
print("\nQues 3a")
c1 = callable(q_and_r_finder)
c2 = callable(n1)
c3 = callable(n2)
if c1 is True:
    print(f"Function is callable")
if c1 is False:
    print(f"Function is Not-callable")
if c2 is True:
    print(f"{n1} is callable")
if c2 is False:
    print(f"{n1} is Not-callable")
if c3 is True:
    print(f"{n2} is callable")
if c3 is False:
    print(f"{n2} is Not-callable")

# Ques 3b
print("\nQues 3b")
# List of values
list_val = [quo, rem]
zero = False
if zero in list_val:
    zero = True
else:
    zero = False
if zero is True:
    print("All result values are NOT 'non-zero'")
elif zero is False:
    print("All result values are 'non-zero'")

# Ques 3c
print("\nQues 3c")
# New values of list
list_r = [quo, rem]
for i in range(4, 7):
    list_r.append(i)
list_val2 = []
# Adding number > 4 from list_r to list_val2
for i in list_r:
    if i > 4:
        list_val2.append(i)
# A new list list_val3 with same elements as list_val2 but in string form
list_val3 = list(map(str, list_val2))
# Using join
v = ",".join(list_val3)
print(f"Values greater than 4 are {v}")

# Ques 3d
print("\nQues 3d")
set1 = {1, 2}
set1.clear()
# Changing above result in set datatype
for el in list_val2:
    set1.add(el)
print("Above result in set form is shown below:")
print(set1)

# Ques 3e
print("\nQues 3e")
# Making set1 immutable
frozenset(set1)
print("The above set has been converted to immutable.")

# Ques 3f
print("\nQues 3f")
print(f"Max value from set is {max(set1)}")
# Using hash function
hash_value = hash(max(set1))
print(f"Hash value of {max(set1)} is {hash_value}")




# ANSWER 4
# Forming a class named student
class Student:
    # Using constructor to create class objects
    def __init__(self, name, roll_no):
        self.name = name
        self.roll_no = roll_no
    # Defining print function
    def stu(self):
        print(f'My name is {self.name} and my roll no. is {self.roll_no}')
    # Calling destructor
    def __del__(self):
        print('Calling destructor')
# Making in object in student class
name = Student('Ayush', 21104044)
name.stu()
del name




# ANSWER 5
# Creating a class named Employee
class Employee:
    # Assigning initial number of objects in class
    count = 0
    # Assigning a constructor to create class objects
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1
    # Defining a function to print details of employees
    def display_details(self):
        print('Name :', self.name, ',', 'Salary :', self.salary)
# Adding objects in the class
emp1 = Employee('Mehak', 40000)
emp2 = Employee('Ashok', 50000)
emp3 = Employee('Viren', 60000)
# Printing details of all employees
print('Details of all employees ->')
emp1.display_details()
emp2.display_details()
emp3.display_details()


# a) Update the salary of Mehak to 70000
class Employee:
    count = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1
    def display_details(self):
        print('Name :', self.name,',', 'Salary :', self.salary)
emp1 = Employee('Mehak', 40000)
emp2 = Employee('Ashok', 50000)
emp3 = Employee('Viren', 60000)
# Changing salary of Mehak from 40000 to 70000
emp1.salary = 70000
print('Details of all employees ->')
emp1.display_details()
emp2.display_details()
emp3.display_details()


# b) Delete the record of employee Viren
class Employee:
    count = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.count += 1
    def display_details(self):
        print('Name :', self.name,',', 'Salary :', self.salary)
emp1 = Employee('Mehak', 40000)
emp2 = Employee('Ashok', 50000)
emp3 = Employee('Viren', 60000)
print('Details of all employees ->')
emp1.display_details()
emp2.display_details()
print('Employee', emp3.name, 'data has been removed')
# Deleting the record of employee Viren
del emp3




# ANSWER 6
gap = ' '*10
print(f'\n{gap}WELCOME TO THE FRIENDSHIP GAME')
# Defining principle of game i.e. anagram
def anagram(word1, word2):
    # Converting all letters to lowercase
    word1 = word1.lower()
    word2 = word2.lower()
    # Form empty list to store letters of words
    l1 = []
    l2 = []
    for x in word1:
        l1.append(x)
    for y in word2:
        l2.append(y)
    # Sorting the list alphabetically
    l1.sort()
    l2.sort()
    if l1 == l2:
        return True
    else:
        return False
# Taking player name input
player1 = str(input("Enter name of player 1 :"))
player2 = str(input("Enter name of player 2 :"))
# Taking words spoken by written
word_p1 = str(input(f"\nEnter Word by {player1} :"))
word_p2 = str(input(f"Enter Word by {player2} :"))
# Using anagram function
result = anagram(word_p1, word_p2)
# Printing the final result
if result is True:
    print(f"\nFriendship of {player1} and {player2} is REAL")
elif result is False:
    print(f"\nFriendship of {player1} and {player2} is FAKE")
