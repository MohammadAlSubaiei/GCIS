'''
GROUP 5
Members: Naqiya hathiari, Mohammad AlSubaiei

Contribution:
Mohammad- 50%
Naqiya- 50%

Github Links:

- Mohammad Ali: https://github.com/MohammadAlSubaiei/GCIS
- Naqiya: https://github.com/naqiyahathiari/group.git

Program description:
This program is a simple virtual shopping cart program. It allows users to choose from a menu which has 
list available items, add them to a virtual shopping cart, remove items, and finally, check out. The 
available items i.e. the inventory is taken and read from a csv file name named catalogue.csv 
and shown to the users.

Each item in the inventory has a name, price, and quantity. Users can add multiple quantities of 
items to their cart, with discounts applied for bulk purchases of three or more items. The checkout 
process calculates the total amount to pay, including a 7% tax.

'''

import csv

INVENTORY = {}

"""The read_data function we pass a the filename into the parameter, after that we open the csv file 
and read the content, the csv file will automatically close because we used (with open(filename, 'r') 
as csv_file:), furthermore we place the information into a variable called csv_reader
which we placed it into a for loop so it can take each row individually. And we added 
three variables which are name, price and quantity which will be used later on."""

def read_data(filename):
    with open(filename, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for line in csv_reader:
            name = line['name']
            price = float(line['price'])
            quantity = int(line['inventory'])
            INVENTORY[name] = {'price': price, 'quantity': quantity} #Giving variable name to each paramter

"""
This class is used to define an article with 3 attributes i.e. name,quantity and price 
and give each of them attributes to further implement them in the shopping cart.
"""
class Article:
    def __init__(self, name, quantity, price):   #Constructor method: Used to initialize the object/Article and give it attributes
        self.__name = name
        self.__quantity = quantity
        self.__price = price

    def get_name(self):    #Getter methods retrieve the value of a private attribute
        return self.__name

    def get_quantity(self):
        return self.__quantity

    def get_price(self):
        return self.__price

    def set_quantity(self, quantity):     #Setter methods modify the value of a private attribute
        self.__quantity = quantity

    def __str__(self):     #used to get a string representation of the object.
        return "Article: ", str(self.__name), "Quantity: ", str(self.__quantity), "Price: ", str(self.__price)

'''
For the menu function, it is used to display options to the user which they can choose from 
by taking their input and enhacing their shopping experience.
'''
def menu():
    print("              ( MENU )\n===============================")  #Given in activity brief
    print("[1] List all items, inventory, and price")
    print("[2] List cart shopping items")
    print("[3] Add an item to the shopping cart")
    print("[4] Remove an item from the shopping cart")
    print("[5] Checkout")
    print("[6] Exit")

'''
For class cart there are 5 functions within it, the first one is called the constructor function (__init__)
which initializes a new instance with an empty list called (list_of_purchased), which we use 
for storing items added to the cart.
'''
class Cart:
    def __init__(self):             #Constructor method
        self.__list_of_purchased = []   #Makes an empty list used to store the objects

    def addProduct(self, name, quantity): # It takes two arguments: name and quantity. 
        global INVENTORY
        if name in INVENTORY: #Input from user should match the items in catalogue 
            available_quantity = INVENTORY[name]['quantity']
            if available_quantity >= quantity:     #If quantity is more than whats there in inventory it wont add the item.
                for item in self.__list_of_purchased:
                    if item['name'] == name:
                        item['quantity'] += quantity
                        return
                self.__list_of_purchased.append({'name': name, 'quantity': quantity, 'price': INVENTORY[name]['price']})

    def removeProduct(self, name, quantity):    #It removes an item along with its quantity.
        for item in self.__list_of_purchased:
            if item['name'] == name:
                if item['quantity'] <= quantity:        #Remove item quantity should be less than whats already added to shopping cart
                    self.__list_of_purchased.remove(item)
                else:
                    item['quantity'] -= quantity
                return

    def displayCart(self):
        if not self.__list_of_purchased:     #If theres nothing in shopping cart then give this message.
            print("No items in shopping cart.")
        else:
            print("Shopping Cart:")
            for item in self.__list_of_purchased:       #If user asks to view shopping cart, show the item along with quantity
                print("Product: ", str(item['name']), "Quantity: ", str(item['quantity']))

    def checkout(self):
        total = 0
        for item in self.__list_of_purchased:
            price = item['price']
            quantity = item['quantity']
            if quantity >= 3:
                price *= 0.9  # 10% discount is given only if quantity is 3 or more for an item
            total += price * quantity
        total *= 1.07  # 7% TAX, suppose price is x and 7% tax would be 0.07x. 
        return total   #Hence the total would become x + 0.07x---> x(1+0.07) --> 1.07 *total

'''
Main function reads item data from a CSV file, displays a menu for users to interact with, 
allows them to view inventory, add or remove items from the cart, calculate the total amount 
at checkout, and exit the program. Basically it integrates the whole menu 
and all the functions of the Class Cart.
'''

def main():
    read_data('products.csv')
    cart = Cart()
    while True:
        menu()
        option = input("Enter your option: ")

        if option == '1':
            print("Inventory:")
            for item, details in INVENTORY.items():
                print("Item: ", str(item), "Price: ", str(details['price']), "Quantity: ", str(details['quantity']))

        elif option == '2':
            cart.displayCart()

        elif option == '3':
            name = input("Enter the name of the item: ")
            quantity = int(input("Enter the quantity: "))
            cart.addProduct(name, quantity)

        elif option == '4':
            name = input("Enter the name of the item: ")
            quantity = int(input("Enter the quantity: "))
            cart.removeProduct(name, quantity)

        elif option == '5':
            total = cart.checkout()
            print("Total amount to pay after 7% tax and discount(if applicable): ", str(total))

        elif option == '6':
            print("Thank you for shopping!")
            break

        else:
            print("Invalid option. Please choose a valid option.")

if __name__ == "__main__":
    main()


