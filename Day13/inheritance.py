class animal:

    def sound(self):
        print("Animals makes a sound!")

class dog(animal):

    def bark(self):
        print("Dog barks")

dog1 = dog()

dog1.sound()
dog1.bark()