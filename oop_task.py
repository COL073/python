class Person:
    nationality = "Kenyan"

    def __init__(self, name, age, gender): #instance attributes
        self.name = name
        self.age = age
        self.gender = gender

    def introduction(self):
        print(f'Praise God, my name is {self.name}. I am {self.age} years old and I am {self.gender}.')

person1 = Person("Chris Bale", 20 , "Male" )
person1.introduction()            