### Create python class with attributes of name,age and section with inheritance.
#Create a Python class Person with attributes: name and age of type string.
#Create a display() method that displays the name and age of an object created via the Person class.
#Create a child class Student  which inherits from the Person class and which also has a section attribute.
#Create a method displayStudent() that displays the name, age and section of an object created via the Student class.
#Create a student object via an instantiation on the Student class and then test the displayStudent method.

"""
class Person:
    def __init__(self,age,name):
        self.name=name
        self.age=age

    def display(self):
        print("Person name is :",self.name)
        print("Person age is :",self.age)

class Student(Person):
    def studentdisplay(self,sec):
        print("Person section is :",sec)

        super().display()
s = Student(24,"**Rishi**")
s.studentdisplay("Data Science")
-------------------------------------------------------------------------------
OUTPUT==
#Person section is : Data Science
#Person name is : **Rishi**
#Person age is : 24
"""
###IN THS INHERITANCE SUPER METHOD ALSO CALLED
