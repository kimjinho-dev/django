class Person:
    now_year = 2022 + 1

    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def details(cls, name, year):
        return cls(name, Person.now_year - year)

    def check_age(self):
        return self.age < 19


p1 = Person('김진호1', 18)
p2 = Person('김진호2', 30)
p3 = Person.details('김진호3', 2010)
p4 = Person.details('김진호4', 1993)
print(p1.check_age())
print(p2.check_age())
print(p3.check_age())
print(p4.check_age())
