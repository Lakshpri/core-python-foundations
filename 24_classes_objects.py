# ============================================================
# CLASSES AND OBJECTS
# ============================================================

# A class is a blueprint.
#
# An object is an actual instance of that class.


# ============================================================
# 1. SIMPLE CLASS
# ============================================================

class Student:

    pass


# Creating objects

student1 = Student()

student2 = Student()

print(student1)

print(student2)


# ============================================================
# 2. OBJECT ATTRIBUTES
# ============================================================

class Student:

    pass


student1 = Student()

student1.name = "Priya"
student1.age = 22
student1.course = "Python"


print(student1.name)
print(student1.age)
print(student1.course)


# ============================================================
# 3. DIFFERENT OBJECTS CAN HAVE DIFFERENT DATA
# ============================================================

student1 = Student()

student1.name = "Priya"
student1.age = 22


student2 = Student()

student2.name = "Rahul"
student2.age = 23


print(student1.name)
print(student1.age)

print(student2.name)
print(student2.age)


# ============================================================
# 4. CLASS METHOD
# ============================================================

class Student:

    def study(self):

        print("Student is studying.")


student1 = Student()

student1.study()


# ============================================================
# 5. METHOD USING OBJECT DATA
# ============================================================

class Student:

    def display(self):

        print("Name:", self.name)

        print("Age:", self.age)


student1 = Student()

student1.name = "Priya"

student1.age = 22

student1.display()


# ============================================================
# 6. MULTIPLE METHODS
# ============================================================

class Student:

    def study(self):

        print("Student is studying.")

    def attend_class(self):

        print("Student is attending class.")

    def write_exam(self):

        print("Student is writing exam.")


student = Student()

student.study()

student.attend_class()

student.write_exam()


# ============================================================
# 7. REAL-WORLD EMPLOYEE
# ============================================================

class Employee:

    def work(self):

        print(self.name, "is working.")

    def display(self):

        print("Employee ID:", self.employee_id)

        print("Name:", self.name)

        print("Role:", self.role)


employee = Employee()

employee.employee_id = 101

employee.name = "Priya"

employee.role = "Developer"

employee.display()

employee.work()


# ============================================================
# 8. REAL-WORLD BANK ACCOUNT
# ============================================================

class BankAccount:

    def deposit(self):

        print("Deposit successful.")

    def withdraw(self):

        print("Withdrawal successful.")

    def check_balance(self):

        print("Balance:", self.balance)


account = BankAccount()

account.balance = 10000

account.check_balance()

account.deposit()

account.withdraw()


# ============================================================
# CLASS VS OBJECT
# ============================================================

# Class:
# Student
#
# Object:
# student1
#
# Class:
# Car
#
# Objects:
# car1
# car2
# car3
#
# Class:
# Employee
#
# Objects:
# employee1
# employee2
# employee3