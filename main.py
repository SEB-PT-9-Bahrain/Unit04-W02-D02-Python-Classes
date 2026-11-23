my_name = 'Omar'

print(type([1,2,3]))

# Creating a new class
class BankAccount():
    # 1. ALL classes have __init__(self) method
    # 2. ALL methods in python take self as first argument
    def __init__(self, owner_param, balance_param = 100):
        print('NEW ACCOUNT CREATED')
        self.owner = owner_param
        self.balance = balance_param
    def print_balance_nicely(self):
        print(f'you {self.owner} have ${self.balance}')

    def withdraw(self, amount_to_withdraw):
        self.balance -= amount_to_withdraw


# Creates a new instance of the class
abdullah_account = BankAccount('Abdullah',200)

abdullah_account.balance = 500

print(abdullah_account.balance)

ahmed_account = BankAccount('Ahmed',250)

abdullah_account.print_balance_nicely()
ahmed_account.print_balance_nicely()


ahmed_account.withdraw(100)
ahmed_account.print_balance_nicely()


ammar_account = BankAccount('Ammar')




# exercise 1: create a class called Student
# this class should have the following attributes: name and country
# if the country is not provided default to 'Bahrain'
# this class should have 1 method introduce_self(self): which should print
# my name is {name} and I am from {country}


class Student():
    teacher = 'Omar'
    def __init__(self, name, country = 'Bahrain'):
        self.name = name
        self.country = country
    def introduce_self(self):
        print(f'my name is {self.name} and I am from {self.country}')
    def __str__(self):
        return f'Name: {self.name}, country:{self.country}'

    @classmethod
    def change_teacher(cls, new_teacher):
        print(cls)
        cls.teacher = new_teacher
    

mahdi_student = Student('Mahdi')
abdullah_student = Student('Abdullah')

mahdi_student.introduce_self()


print(mahdi_student)

Student.teacher = 'Sayed Hamed'

print(mahdi_student.teacher)
print(abdullah_student.teacher)


Student.change_teacher('Jameela')

print(Student.teacher)


class GAEmployee():
    def __init__(self, name, fridge_code):
        self.name = name
        self.fridge_code = fridge_code

    def introduce_self(self):
        print(f'Hello my name is {self.name} and I Work at GA')


class Teacher(GAEmployee):
    def __init__(self, name, fridge_code, courses_taught):
        super().__init__(name, fridge_code)
        self.courses_taught = courses_taught


omar_teacher = Teacher('Omar',112,['Java','JavaScript','Python'])

print(omar_teacher)