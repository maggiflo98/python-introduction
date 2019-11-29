# Lists:collection of itrms that are ORDERED,CHANGEABLE
# DICTIONARY:collection of items that are UNORDERD,CHANGEABLE and INDEXED
# TUPLE: collection of items that are ORDERED,UNCHANGEABLE
# SET:collection of items that are Unordered,unchangeable list in Python
#variablename-['item 1,', 'item 2','item 3']
shoppingList = ['toothpaste','cake','item3']
item0 = shoppingList[0]
print(item0)
# item0=shoppinglist[-1]
item2 = shoppingList[2]
print(item2)
print(shoppingList)
print(shoppingList[1:2])
# list slicing
print(type(shoppingList))
print(type('hello'))
print(type(2))
print(type(2.1))
 # changing values in a list
 # variablename[index]=newitem
shoppingList[0] = 'book'
print(shoppingList)

# listlength
print(len(shoppingList))
# listmethods
# 1.append(): add an item as the last item to a list
# 2.insert(): you specify position to add item
# 3.pop(): removes the last item
# 4.delete deletes the whole list
# 5.clear leaves you with an empty list
# 6.extends :adds more than one item in a list
shoppingList.append("toothpaste")
print(shoppingList)
shoppingList.insert(1,'milk')
print(shoppingList)
shoppingList.pop()
print(shoppingList)
del shoppingList[3]
print(shoppingList)
del shoppingList
print(shoppingList)
# checking if an item exists in a list
# research on clear and extend methods
# checking if an item exists in list
if 'cake' in  shoppingList:
     print('cake is present in the list')
else:
    print('cake is not in the list')

if 'cakes'in shoppingList:print('cake is present in the list')