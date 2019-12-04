# python function
# 1.a block of code with a name
# 2.only works when called
# 3. helps us to write repeated code
def nameofFunction():
    print('hello world')

 # calling a function in python
nameofFunction()
# naming a function
# 1.it should start with small case
# 2.it should start with a  letter or an underscore
def greeting_1(name):
    print(" hello world " + name)
greeting_1("flo")
 # 2.function with more than one argument
def greetings_2(name,country,gender):
    print(" my name is "+ name +" i come from "+ country +  " i am  "+ gender)
greetings_2("john","kenya","male")

# 3.default parameter
def greetings_3(name =" developer "):
     print("hello world " + name)
greetings_3()
greetings_3('mary')

# using_
def sum_of_two_num(number_1,number_2):
    print(number_1+number_2)
sum_of_two_num(3,5)

# using camelcase
def sumOfTwoNum(number_1,number_2):
    theSum = number_1+number_2
    return theSum
ans=sumOfTwoNum(3,10)
print(ans)

# function that computes area of a circle given radius
def areaOfCircle(radius):
    area = 22/7 * radius * radius
    return area
ans=areaOfCircle(10)
print(ans)

# default area of a circle
def areaOfCircle(radius=7):
    print(22/7 *radius**2)
areaOfCircle()


shoppingList = ['soap','sugar','bread','cooking oil',['kijiko','kikombe'],{"name":"john"}]
print(shoppingList[4][0])
print(shoppingList[5]["name"])
def loopList(theList):
    for item in theList:
        print(item)
loopList(shoppingList)