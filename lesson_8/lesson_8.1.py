class Animal:
    def __init__(self,name,country,color):
        self.name = name
        self.country = country
        self.color = color

    def printDetails(self):
        print("name is :{}" "and country is : {}".format(self.name,self.country))
    def printColor(self):
        print( "name is {}" " and country is {}" " my color is  {}".format(self.name,self.country,self.color))

    # child class
class Goat(Animal):
     # pass     # used when you dont want to add any code

    def __init__(self,name,country,owner):    # the child class will nolonger inherit from the parent
        self.name = name
        self.country = country
        self.owner = owner
    def printDetails(self):
        print("name is {}" " and country is {}" " my owner is  {}".format(self.name, self.country, self.owner))

g1 = Goat('gush','kenya','black')
g1.printDetails()


class Dog():
    pass


class Dog(Animal):
    def __init__(self, name, country,color):
        # Animal.__init__ (self, name, country,)
        # inherit from parent
        super().__init__(name,country,color)
        self.color = color

    def getDetails(self):
       print("name {} and country {} and color {}".format(self.name,self.country,self.color))


d1 = Dog("smooth","somalia","red")
d1.getDetails()
  # oop goals,principles,patters