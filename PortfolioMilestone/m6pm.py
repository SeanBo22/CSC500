## Sean Bohuslavsky 
## CSC500 - Portfolio Milestone
## Python Program to create item and shopping cart class

#ItemToPurchase class
class ItemToPurchase:
    #Constructor
    def __init__(self):
        self.item_name = "none"
        self.item_description = "none"
        self.item_price = 0
        self.item_quantity = 0
    
    #Method
    def print_item_cost(self):
        print("{} {} @ {} = {}".format(self.item_name, self.item_quantity, self.item_price, (self.item_quantity * self.item_price)))

class ShoppingCart:
    #Constructor
    def __init__(self, customer_name="none", date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = date
        self.cart_items = []
    
    #Methods
    def add_item(self, item):
        self.cart_items.append(item)
    def remove_items(self, item_name):
        for i in self.cart_items:
            if i.item_name == item_name:
                self.cart_items.remove(i)
        else:
            print("Item not found in cart. Nothing removed")
    def modify_item(self, item):
        for i in self.cart_items:
            if i.item_name == item.item_name:
                if i.item_name == "none" and i.item_price == 0 and i.item_quantity == 0 and i.item_description == "none":
                    print("Item has default values. Item will not be modified")
                else:
                    i.item_name = item.item_name
                    i.item_price = input("\nEnter new price:")
                    i.item_quantity = input("\nEnter new quantity:")
                    i.item_description = input("\nEnter new description:")
            else:
                print("Item not found in cart. Nothing modified")
    def get_num_items_in_cart(self):
        total_quantity = 0
        for i in self.cart_items:
            total_quantity = i.item_quantity + total_quantity
        return total_quantity
    def get_cost_of_cart(self):
        total_cost = 0
        for i in self.cart_items:
            total_cost = i.item_price + total_cost
        return total_cost
    def print_total(self):
        if len(self.cart_items) > 0:
            total = 0
            print("{} - {}\nNumber of Items: {}".format(self.customer_name, self.current_date, len(self.cart_items)))
            for i in self.cart_items:
                print("{} {} @ ${} = ${}".format(i.item_name, i.item_quantity, i.item_price, (i.item_quantity * i.item_price)))
                total = total + (i.item_quantity * i.item_price)
            print("Total: ${}".format(total))
        else:
            print("SHOPPING CART IS EMPTY")
    def print_descriptions(self):
        if len(self.cart_items) > 0:
            print("{} - {}\nItem Descriptions".format(self.customer_name, self.current_date,))
            for i in self.cart_items:
                print("{}: {}".format(i.item_name, i.item_description))
        else:
            print("SHOPPING CART IS EMPTY")
        
#Print the option menu              
def print_menu():
    print("\tMENU")
    print("a - Add item to cart")
    print("r - remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - quit")
    print("\t  Choose an option:")

#Create 3 ItemToPurchase classes
item1 = ItemToPurchase()
item1.item_name = "Nike Romaleos"
item1.item_description = "Volt Color, Weightlifting shoes"
item1.item_price = 189
item1.item_quantity = 2

item2 = ItemToPurchase()
item2.item_name = "Chocolate Chips"
item2.item_description = "Semi-sweet"
item2.item_price = 3
item2.item_quantity = 5

item3 = ItemToPurchase()
item3.item_name = "Powerbeats 2 Headphones"
item3.item_description = "Bluetooth headphones"
item3.item_price = 128
item3.item_quantity = 1

#Create a ShoppingCart class
shopping_cart1 = ShoppingCart()
shopping_cart1.customer_name = "John Doe's Shopping Cart"
shopping_cart1.current_date = "February 1, 2020"
shopping_cart1.add_item(item1)
shopping_cart1.add_item(item2)
shopping_cart1.add_item(item3)

#Get user input
answer = ''
while answer != 'q':
    print_menu()
    answer = input(" ")
    if answer == 'o' or answer == 'O':
        print("\tOUTPUT SHOPPING CART")
        shopping_cart1.print_total()
    elif answer == 'i' or answer =='I':
        print("\tOUTPUTS ITEMS' DESCRIPTIONS")
        shopping_cart1.print_descriptions()
    elif answer == 'q' or answer =='Q':
        print("Quitting out.")
    else:
        print("Invalid choice or choice is not implemented yet. Please choose again")
        
        