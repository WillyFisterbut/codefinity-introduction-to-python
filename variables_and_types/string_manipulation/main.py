grocery_items = "milk cheese bread apples oranges chicken"

#Create variables and use string slicing to separate the items from the variable "grocery_items" into new variables
dairy1 = grocery_items[0:4]
dairy2 = grocery_items[5:11]
bakery1 = grocery_items[12:17]

#Use string concatenation to build an output that mentions these items and their aisle number
print("We have dairy and bakery items: ", dairy1 + ", " + dairy2 + ", and " + bakery1 + " in aisle 5")