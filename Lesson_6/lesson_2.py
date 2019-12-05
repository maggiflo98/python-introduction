# 1.conditional statements
# 2.looping
# a.if checks if a condition is true
# b.if else executes the condition that is not true
# c.if elif else executes the conditions before it,if they are nt true
# if statements most of the time make use of the assingnment operators i.e >,<,<=,>=!=

x = 5
y = 3
# check for true condition
if x > y:
    print(str(x)+"is greater than" + str(y))
    print(" {} is greater {}".format(x,y))
elif x < 10:
    print("{} is not less than {}".format(x,10))
    # checks for false conditions
else:
    print(" {} is greater {}".format(x,y))
    # nested if
if x > y:
  if y > 2:
    print("y is greater than 2,but less than {}".format(x))
  else:
    print("y is not greater than{} and{}".format(2,x))
else:
    print("{} is not greater than {}".format(x,y))


# while loops
count=0
while count < 10:
    print("hello world")
    count = count +1

num=0
while num <= 10:
    print(num)
    num = num +1
# break
    num2= 0
    while num2 <= 10:
        if num2==5:
            print("at the middle")
            # break stops the loop if the condition is true
            break
        print(num2)
        num2 = num2 + 1

        # continue
        num3 = 0
        while num3 <= 10:
            num3 = num3 + 1
            if num3 == 5:
                print("at the middle")
                # if true skip thus instance
                continue
            print(num3)

            # for loop
            for letter in "john":
                print(letter)
                # range(starting point,ending point,increment value)
            for i in range(3, 10,2):
               print(i)


               # else in a statement with a for loop
               for i in range(10):
                   print(i)
               else:
                  pass
               # assingement:write a program that prints the smallest and the largest number i this list
               #  numbers=[210,34,65,0,33,54,54,54,3,65,]