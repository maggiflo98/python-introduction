# # operators:used to perform operations to variables and values
# 1.arithmetic
# 2.assignment
# 3.comparison
# 4.logical
# 1.arithmetic
# 1.addition
x=23
y=32
print("addition of {} {} is {} ".format(x,y,x+y))
print("subtraction of {} {} is {} ".format(x,y,x-y))
print("division of {}  and {} is {} ".format(x,y,x/y))
print("multiplication of {}  and {} is {} ".format(x,y,x*y))
print("modulus of {}  and {} is {} ".format(3,2,3%2))
# area of a circle radius 7
x=22
y = 7

print(x/y*y*y)
# 2.Assingment:used assign  a value to a variable
# 1,=
name="john"
# 2.+=
x = 5
x = x +6
x+= 6
# comparison operator
# 1.==equals
# 1.!=not equal
#  2.>,<,>=,<=
# compariosn operator return boolean datatype
# logical operators:used to combine conditional operations
# 1. and
# 2.or
# 3.not
# result is boolean
x = 3
y = 2
# and:returns true if both conditions are true
print(x > y and x < 10 )
# or  returns if one condition is true
print(x >y or x< 10)
    # not  returns false if a result is true
print(not( x > y and  x < 10))
# datatype lists,dictionary,set,tuple