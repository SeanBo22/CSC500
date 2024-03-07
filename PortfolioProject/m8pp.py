## Sean Bohuslavsky 
## CSC500 - Portfolio Project
## Python Program to create item class, create a shopping cart class, and let user interface with them.

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
        item_exists = False
        for i in self.cart_items:
            if i.item_name == item_name:
                self.cart_items.remove(i)
                item_exists = True
                print("Item was successfully removed")
                break
        if item_exists == False:
            print("Item not found in cart. Nothing removed")
    def modify_item(self, item_name, new_quantity):
        item_exists = False
        for i in self.cart_items:
            if i.item_name == item_name:
                if i.item_name == "none" and i.item_price == 0 and i.item_quantity == 0:
                    print("Item has defualt values. Item will not be modified")
                else:
                    i.item_quantity = new_quantity
                    item_exists = True
                    print("Item was successfully modified")
                    break
        if item_exists == False:
            print("Item not found in cart. Nothing modified")
    def get_num_items_in_cart(self):
        print(len(self.cart_items))
    def get_cost_of_cart(self):
        for i in self.cart_items:
            total = i.item_price + total
        return total
    def print_total(self):
        if len(self.cart_items) > 0:
            total = 0
            print("{} - {}\nNumber of Items: {}".format(self.customer_name, self.current_date, len(self.cart_items)))
            for i in self.cart_items:
                print("{} {} @ ${} = ${}".format(i.item_name, i.item_quantity, i.item_price, (i.item_quantity * i.item_price)))
                total = total + (i.item_quantity * i.item_price)
            print("Total: ${}".format(total))
        else:
            print("There are no items in the cart.")
    def print_descriptions(self):
        if len(self.cart_items) > 0:
            print("{} - {}\nItem Descriptions".format(self.customer_name, self.current_date,))
            for i in self.cart_items:
                print("{}: {}".format(i.item_name, i.item_description))
        else:
            print("There are no items in the cart.")

#Function to print menu options                
def print_menu():
    print("\tMENU")
    print("a - Add item to cart")
    print("r - remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
    print("o - Output shopping cart")
    print("q - quit")
    print("\t  Choose an option:")

#Create shopping cart. Get user input
shopping_cart = ShoppingCart()
shopping_cart.customer_name = input("Enter customer's name:\n")
shopping_cart.current_date = input("Enter today's date: (Month DD, YYYY)\n")

print("Customer name: {}".format(shopping_cart.customer_name))
print("Today's date: {}".format(shopping_cart.current_date))

#Get user input for menu selection
answer = ''
while answer != 'q':
    print_menu()
    answer = input(" ")
    if answer == 'o' or answer == 'O':
        print("\tOUTPUT SHOPPING CART")
        shopping_cart.print_total()
    elif answer == 'i' or answer =='I':
        print("\tOUTPUTS ITEMS' DESCRIPTIONS")
        shopping_cart.print_descriptions()
    elif answer == 'a' or answer =='A':
        print("\tADD ITEM TO CART")
        new_item = ItemToPurchase()
        new_item.item_name = input("Enter the item name:\n")
        new_item.item_description = input("Enter the item description:\n")
        new_item.item_price = float(input("Enter the item price:\n"))
        new_item.item_quantity = int(input("Enter the item quantity:\n"))
        shopping_cart.add_item(new_item)
    elif answer == 'r' or answer =='R':
        print("\tREMOVE ITEM FROM CART")
        item_name = input("Enter name of item to remove:\n")
        shopping_cart.remove_items(item_name)
    elif answer == 'c' or answer =='C':
        print("\tCHANGE ITEM QUANTITY")
        item_name = input("Enter the item name:\n")
        item_new_quantity = int(input("Enter the new quantity:\n"))
        shopping_cart.modify_item(item_name,item_new_quantity)