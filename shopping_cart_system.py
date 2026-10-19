# Name: Sophia Chang
# AM

#Stores the products
products = ["Chips", "Soda", "Candy", "Cookies", "Water", "Sandwich"]

#Stores the prices of the products
prices = [2.00, 2.50, 1.50, 3.00, 1.00, 5.00]

#This stores the products the customers choose to purchase
shopping_cart = []

#Control variable to break out of the while loop
checkout = False

#Option 1
def display_products():
    print("========== AVAILABLE PRODUCTS ==========")
    #prints out all of the products and their prices
    for num in range(len(products)):
        print(f"{num + 1}.", products[num], "     ", f"${prices[num]:.2f}")

#Option 2
def add_product(shopping_cart, products):
    print("Which product would you like to add to your cart?")
    #prints out all of the available products that are sold
    for num in range(len(products)):
        print(f"{num+1}.",products[num])
    product = int(input("Enter product number:"))

    #While loops that checks if the product is unavilable
    while product > len(products) or product < 1:
        print("Invalid product!")
        print("Please choose a number between 1 and ", f"{len(products)}", ".")
        product = int(input("Enter product number:"))

    #adds the available product to the shopping_cart list
    shopping_cart.append(products[product - 1])
    print(products[product - 1]," was added to your cart.")

#Option 3
def remove_product(shopping_cart):
    #controls whether or not the number picked to remove is valid:
    valid = False            
    if len(shopping_cart) != 0:
        print("========== YOUR SHOPPING CART ==========")
        
        #prints all of the items in the shopping_cart list
        for product in range(len(shopping_cart)):
            print(f"{product+1}.", shopping_cart[product])

        print("Which item would you like to remove?")
        #Asks user what number to remove
        item = int(input("Enter item number: "))

        #checks whether or not the number the user picked is within the range of shopping_cart list
        while valid == False:
            if item < 1 or item > len(shopping_cart):
                print("That item doesn't exist in your cart!")

            #Checks whether or not the item chosen by the user to remove is within the shopping_cart list
            elif 1 <= item <= len(shopping_cart):
                print(shopping_cart[item - 1], "was removed from your cart.")
                shopping_cart.pop(item - 1)
                valid = True
                return valid
            #Asks user what number to remove
            item = int(input("Enter item number: "))

    #Checks whether or not the cart is empty
    elif len(shopping_cart) == 0:
        print("Your shopping cart is empty.")
        print("There is nothing to remove.")

#Option 4
def display_cart(shopping_cart):
    print("========== YOUR SHOPPING CART ==========")

    #checks whether the shopping_cart list is empty. in other words, it checks if the cart is empty
    if len(shopping_cart) == 0:
        print("Your shopping cart is empty.")

    #functions when the shopping_cart list isn't empty. in other words, it works when the cart is not empty
    else:
        #displays everything currently in the shopping cart
        for itm in range(len(shopping_cart)):
            print(f"{itm+1}.", shopping_cart[itm], "     ", f"${prices[products.index(shopping_cart[itm])]:.2f}")

    #prints the amount of items there are
    print("Total Items:", len(shopping_cart))

#Option 5
def calculate_total(cart):
    sub = 0
    for itm in range(len(cart)):
        sub += prices[products.index(cart[itm])]
    return sub

def get_discount(sub):
    #Checks whether or not the subtotal is greater than or equal to 40
    if sub >= 40:
        return  0.15
    #Checks whether or not the subtotal is greater than or equal to 20 and less than 40
    elif 20 <= sub < 40:
        return 0.10
    #checks whether or not the subtotal is greater than or equal to 10 and less than 20
    elif 10 <= sub < 20:
        return 0.05
    else:
        return 0


#Option 6
def receipt(subtotal, cart):
    if len(cart) != 0:
        print("========== RECEIPT ==========")

        #gets the current local date
        from datetime import datetime
        now = datetime.now()
        formatted_now = now.strftime("%m/%d/%Y").replace("/0", "/")
        print("Date:", formatted_now) 

        for itm in range(len(cart)):
            print(f"{itm+1}.", cart[itm], "     ", f"${prices[products.index(cart[itm])]:.2f}")

        print("Subtotal:", f"${subtotal:.2f}")

        #calls the discount function
        discount = get_discount(subtotal)

        saved = discount * subtotal
        final = subtotal - saved
        print("Discount: ", f"{discount:.0%}")
        print("Amount Saved: ", f"${saved:.2f}")
        print("Final Total:", f"${final:.2f}")
        print("Thank you for your time shopping here!")
        return True
    else:
        print("You can't check out! You have nothing in your shopping cart")
        return False

#While loop that loops until the customer selects checkout
while checkout == False:
    #Main menu
    print("========== SMART SHOPPING CART ==========")
    print()
    print("1. View Available Products")
    print()
    print("2. Add Product to Cart")
    print()
    print("3. Remove Product from Cart")
    print()
    print("4. View Shopping Cart")
    print()
    print("5. View Current Total")
    print()
    print("6. Checkout")
    print()
    #Asks the user to input their choice based off the menu
    choice = int(input("Enter your choice: "))

    #Checks if the user chose option 1
    if choice == 1:
        display_products()

    #Checks if the user chose option 2
    elif choice == 2:
        add_product(shopping_cart,products)

    #Checks if the user chose option 3
    elif choice == 3:
        remove_product(shopping_cart)

    #Checks if the user chose option 4
    elif choice == 4:
        display_cart(shopping_cart)

    #Checks if the user chose option 5
    elif choice == 5:
        print("========== CURRENT TOTAL ==========")
        subtotal = calculate_total(shopping_cart)
        print("Subtotal:", f"${subtotal:.2f}")

    #checks if the user chose option 6
    elif choice == 6:
        subtotal = calculate_total(shopping_cart)
        checkout = receipt(subtotal, shopping_cart)
        

    #This function runs when the user chooses a number that's out of the range of 1 and 6 inclusive
    else:
        print("Invalid option!")
 
    

