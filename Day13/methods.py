class student:

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def display(self):
        print(f" Name: {self.name}")
        print(f" Age: {self.age}")


student1 = student("Diya",20)

student1.display()
