#Inheritance
class Animal():
    def __init__(self):
        print("Animal created")

    def whoAmI(self):
        print("Animal")
    def eat(self):
        print("eating")


class Dog(Animal):

    def __init__(self):
        #Animal.__init__(self)
        print("dog created")
    def favfood(self):
        print("bones")



mydog= Dog()
mydog.whoAmI()
mydog.eat()
mydog.favfood()

#SpecialMethods

class Book():
    def __init__(self,title,author,pages):
        self.title=title
        self.author=author
        self.pages=pages

b= Book("Python","richa",200)
print(b)

    
mylist= [1,2,3]
print(mylist)
