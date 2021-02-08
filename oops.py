class Sample():
    pass
x= Sample()
print(type(x))

class Happy():
    pass
myhappy= Happy()
print(type(myhappy))

class Dog():
    def __init__(self):
        pass

mydog= Dog()
print(type(mydog))

class School():
    def __init__(self,name,age):
        self.name=name
        self.age=age

schoolname= School(name="RGPV", age=21)

print(schoolname.name)
print(schoolname.age)