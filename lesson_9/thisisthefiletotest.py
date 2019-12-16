shopping_list=['rice','beef','cooking oil',]
myDict = {
    "name":"john",
     "amount":"1200",
     " shop":"naivas"

}
class Town:
    def __init__(self,name):
        self.name=name

    def getName(self):
          print("{}supermarket".format(self.name))

    def getDetails(shoppingList,customer):
        print("{}shopping list bout by {}".format(shoppingList))
