# ============================================================
# CONSTRUCTORS IN PYTHON
# ============================================================

# A constructor is a special method that runs
# automatically when an object is created.
#
# Python's constructor method is:
#
# __init__()
#
# It is used to initialize object data.


# ============================================================
# 1. SIMPLE CONSTRUCTOR
# ============================================================

class Student:

    def __init__(self):

        print("Student object created.")


student1 = Student()

student2 = Student()


# __init__ automatically runs when:
#
# Student()
#
# is executed.


# ============================================================
# 2. CONSTRUCTOR WITH PARAMETERS
# ============================================================

class Student:

    def __init__(self, name, age):

        self.name = name

        self.age = age


student1 = Student("Priya", 22)

student2 = Student("Rahul", 23)


print(student1.name)
print(student1.age)

print(student2.name)
print(student2.age)


# ============================================================
# 3. CONSTRUCTOR WITH MULTIPLE VALUES
# ============================================================

class Employee:

    def __init__(self, employee_id, name, role, salary):

        self.employee_id = employee_id

        self.name = name

        self.role = role

        self.salary = salary


employee = Employee(
    101,
    "Priya",
    "Developer",
    40000
)


print("ID:", employee.employee_id)

print("Name:", employee.name)

print("Role:", employee.role)

print("Salary:", employee.salary)


# ============================================================
# 4. CONSTRUCTOR + METHOD
# ============================================================

class Student:

    def __init__(self, name, marks):

        self.name = name

        self.marks = marks


    def display(self):

        print("Name:", self.name)

        print("Marks:", self.marks)


student = Student("Priya", 90)

student.display()


# ============================================================
# 5. REAL-WORLD BANK ACCOUNT
# ============================================================

class BankAccount:

    def __init__(self, account_number, name, balance):

        self.account_number = account_number

        self.name = name

        self.balance = balance


    def display(self):

        print("Account Number:", self.account_number)

        print("Name:", self.name)

        print("Balance:", self.balance)


account = BankAccount(
    1001,
    "Priya",
    50000
)

account.display()


# ============================================================
# 6. CONSTRUCTOR WITH DEFAULT VALUE
# ============================================================

class Employee:

    def __init__(
        self,
        name,
        role="Developer"
    ):

        self.name = name

        self.role = role


employee1 = Employee("Priya")

employee2 = Employee(
    "Rahul",
    "Tester"
)


print(employee1.name)
print(employee1.role)

print(employee2.name)
print(employee2.role)


# ============================================================
# IMPORTANT
# ============================================================

# __init__() is automatically called
# when an object is created.
#
# self.name = name
#
# means:
#
# Store the parameter "name"
# inside the current object's "name" attribute.