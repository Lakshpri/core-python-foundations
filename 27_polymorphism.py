# ============================================================
# POLYMORPHISM IN PYTHON
# ============================================================

# Polymorphism means:
#
# "Many forms"
#
# The same method name can perform
# different actions for different objects.


# ============================================================
# 1. METHOD OVERRIDING
# ============================================================

class Dog:

    def sound(self):

        print("Dog barks.")


class Cat:

    def sound(self):

        print("Cat meows.")


dog = Dog()

cat = Cat()

dog.sound()

cat.sound()


# Same method:
#
# sound()
#
# Different behavior.


# ============================================================
# 2. SAME FUNCTION WITH DIFFERENT OBJECTS
# ============================================================

def make_sound(animal):

    animal.sound()


dog = Dog()

cat = Cat()

make_sound(dog)

make_sound(cat)


# The same function works with different objects.


# ============================================================
# 3. POLYMORPHISM WITH INHERITANCE
# ============================================================

class Animal:

    def sound(self):

        print("Animal sound")


class Dog(Animal):

    def sound(self):

        print("Dog barks")


class Cat(Animal):

    def sound(self):

        print("Cat meows")


animals = [
    Dog(),
    Cat()
]


for animal in animals:

    animal.sound()


# ============================================================
# 4. REAL-WORLD PAYMENT EXAMPLE
# ============================================================

class CreditCard:

    def pay(self, amount):

        print(
            "Paid",
            amount,
            "using Credit Card"
        )


class UPI:

    def pay(self, amount):

        print(
            "Paid",
            amount,
            "using UPI"
        )


class Cash:

    def pay(self, amount):

        print(
            "Paid",
            amount,
            "using Cash"
        )


def make_payment(payment_method, amount):

    payment_method.pay(amount)


make_payment(
    CreditCard(),
    1000
)

make_payment(
    UPI(),
    500
)

make_payment(
    Cash(),
    300
)


# ============================================================
# 5. OPERATOR POLYMORPHISM
# ============================================================

# The + operator behaves differently
# depending on the data type.


print(10 + 20)

print("Hello " + "Python")

print([1, 2] + [3, 4])


# Same operator:
#
# + 
#
# Different behavior.


# ============================================================
# 6. BUILT-IN POLYMORPHISM
# ============================================================

print(len("Python"))

print(len([10, 20, 30]))

print(len((10, 20, 30)))


# len() works with different objects.


# ============================================================
# REAL-WORLD EXAMPLE
# ============================================================

class EmailNotification:

    def send(self, message):

        print("Email:", message)


class SMSNotification:

    def send(self, message):

        print("SMS:", message)


class WhatsAppNotification:

    def send(self, message):

        print("WhatsApp:", message)


def send_notification(service, message):

    service.send(message)


send_notification(
    EmailNotification(),
    "Your order has been shipped."
)

send_notification(
    SMSNotification(),
    "Your order has been shipped."
)

send_notification(
    WhatsAppNotification(),
    "Your order has been shipped."
)


# ============================================================
# IMPORTANT
# ============================================================

# Polymorphism allows us to write flexible code.
#
# Instead of writing:
#
# if payment == "UPI":
#     ...
#
# if payment == "Card":
#     ...
#
# We can make different classes
# implement the same method.