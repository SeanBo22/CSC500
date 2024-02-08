## Sean Bohuslavsky 
## CSC500 - Portfolio Milestone
## Python Program to create item class

#ItemToPurchase Class
class ItemToPurchase:
    def __init__(self):
        #Attributes
        self.item_name = "none"
        self.item_price = 0
        self.item_quantity = 0
        
    #Method to print item cost
    def print_item_cost(self):
        print("{} {} @ ${} = ${}".format(self.item_name, self.item_quantity, self.item_price, (self.item_quantity * self.item_price)))

#Create item1
item1 = ItemToPurchase()
item1.item_name = input("Enter the name of item 1: ")
item1.item_price = float(input("Enter the price of item 1: "))
item1.item_quantity = int(input("Enter the quantity of item 1: "))

#Create item2
item2 = ItemToPurchase()
item2.item_name = input("Enter the name of item 2: ")
item2.item_price = float(input("Enter the price of item 2: "))
item2.item_quantity = int(input("Enter the quantity of item 2: "))

#Calculate total cost
total_cost = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)

#Print total cost
print("        TOTAL COST      ")
item1.print_item_cost()
item2.print_item_cost()
print("        Total: ${}".format(total_cost))