class  Myclass:
    # an attribute which is same as a variable
   x = "john"
   y = 12
   theList=[12,34,45,6,3]

    # object creation
c1=Myclass()
# c1=obj of myclass blueprint
print(c1.x)
print(c1.y)
print(c1.theList)

c2=Myclass()
print(c1.x)
print(c1.y)
print(c1.theList)

class Person:
   def __init__(self,name,age,country):
       self.thename = name      #assign the class "thename" attr
       self.theage = age        #assign the class "the age" attr
       self.thecountry = country

   def getter(self, ):
     # data = "{},{}".format(self.thename,self.theage)
     # print("hello world")
     print(self.thename)
     print(self.theage)


   def shout(self):
      print(p1.thename)
      print(p2.thename)
   # create objects
p1 = Person("John",34,"uganda")
p2 = Person("Mary",14, "ethiopia")
print(p1.thename +p1.thecountry + str(p1.theage))
print(p2.thename)
p1.getter()
p2.getter()
p1.shout()
p2.shout()
p1.getter()

class Animal:
    def __init__(self,nature,prey,name,gender,feeding):
     self.nature = nature
     self.prey = prey
     self.gender = gender
     self.name = name
     self.feeding = feeding

    def getDetails(self):
        print(self.nature)
        print(self.prey)
        print(self.name)
        print(self.gender)
        print(self.feeding)

a1=Animal("wild","chicken","mongoose","female","carnivorous")
a1.getDetails()
a2=Animal("domestic","goats","lion","male","carnivorous")
a2.getDetails()

# create a class that has the following
# name continent:
# attributes:size,number of countries,location,population,