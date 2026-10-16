# Name: Sophia Chang
# AM

#imports module datetime
import datetime 

#Stores the products
products = ["Chips", "Soda", "Candy", "Cookies", "Water", "Sandwich"]

#Stores the prices of the products
prices = [2.00, 2.50, 1.50, 3.00, 1.00, 5.00]

#This stores the products the customers choose to purchase
shopping_cart = []

#Control variable to break out of the while loop
checkout = False

#subtotal variable
subtotal = 0

#While loop that loops until the customer selects checkout
while checkout == False:
    #Main menu
    print("========== SMART SHOPPING CART ==========")
    print()
    print("1. View Available Prodcuts")
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
        print("========== AVAILABLE PRODUCTS ==========")
        #prints out all of the products and their prices
        for num in range(len(products)):
            print(f"{num + 1}.", products[num], "     ", f"${prices[num]:.2f}")

    #Checks if the user chose option 2
    elif choice == 2:
        print("Which product would you like to add to your cart?")
        #prints out all of the available products that are sold
        for num in range(len(products)):
            print(f"{num+1}.",products[num])
        product = int(input("Enter product number:"))

        #While loops that checks if the product is unavilable
        while product > 6 or product < 1:
            print("Invalid product!")
            print("Please choose a number between 1 and 6.")
            product = int(input("Enter product number:"))

        #adds the available product to the shopping_cart list
        shopping_cart.append(products[product - 1])
        print(products[product - 1]," was added to your cart.")

    #Checks if the user chose option 3
    elif choice == 3:
        if len(shopping_cart) != 0:
            print("========== YOUR SHOPPING CART ==========")
            
            #prints all of the items in the shopping_cart list
            for product in range(len(shopping_cart)):
                print(f"{product+1}.", shopping_cart[product])

            print("Which item would you like to remove?")
            #Asks user what number to remove
            item = int(input("Enter item number: "))

            #Checks whether or not the item chosen by the user to remove is within the shopping_cart list
            if 1 <= item <= len(shopping_cart):
                print(shopping_cart[item - 1], "was removed from your cart.")
                shopping_cart.remove(shopping_cart[item - 1])
            #Displays when the user chooses an item number that's not within the range
            else:
                print("That item doesn't exist in your cart!")
                    #Checks whether or not the cart is empty
        elif len(shopping_cart) == 0:
            print("Your shopping cart is empty.")
            print("There is nothing to remove.")

    #Checks if the user chose option 4
    elif choice == 4:
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

    #Checks if the user chose option 5
    elif choice == 5:
        print("========== CURRENT TOTAL ==========")
        #calculates the total cost of everything in the cart
        for itm in range(len(shopping_cart)):
            subtotal += prices[products.index(shopping_cart[itm])]
        print("Subtotal:", f"${subtotal:.2f}")

    #checks if the user chose option 6
    elif choice == 6:
        if len(shopping_cart) != 0:
            print("========== RECEIPT ==========")

            #gets the current local date
            from datetime import datetime
            now = datetime.now()
            formatted_now = now.strftime("%m/%d/%Y").replace("/0", "/")
            print("Date:", formatted_now) 

            print("Subtotal:", f"${subtotal:.2f}")
            discount = 0
            #Checks whether or not the subtotal is greater than or equal to 40
            if subtotal >= 40:
                discount = 0.15
            #Checks whether or not the subtotal is greater than or equal to 20 and less than 40
            elif 20 <= subtotal < 40:
                discount = 0.10
            #checks whether or not the subtotal is greater than or equal to 10 and less than 20
            elif 10 <= subtotal < 20:
                discount = 0.05

            saved = subtotal - (discount * subtotal)
            final = saved + subtotal
            print("Discount: ", f"{discount:.0%}")
            print("Amount Saved: ", f"${saved:.2f}")
            print("Final Total:", f"${final:.2f}")
            print("Thank you for your time shopping here!")
            checkout = True
        else:
            print("You can't check out! You have nothing in your shopping cart")
    #This function runs when the user chooses a number that's out of the range of 1 and 6 inclusive
    else:
        print("Invalid option!")
 
    

