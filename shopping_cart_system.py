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
        #prints out all of the products and their prices
        for num in range(len(products)):
            print("Available Products:")
            print(products[num], "     $", prices[num])

    #Checks if the user chose option 2
    elif choice == 2:
        print("Which product would you like to purchase?")
        #prints out all of the available products that are sold
        for num in range(len(products)):
            print(num, ". ",products[num])
        product = int(input("Enter product number:"))

        #While loops that checks if the product is unavilable
        while product > 6 or product < 0:
            print("Invalid product!")
            print("Please choose a number between 1 and 6.")
            product = int(input("Enter product number:"))

        #adds the available product to the shopping_cart list
        shopping_cart.append(products[product - 1])
        print(products[product - 1]," was added to your cart.")

    #Checks if the user chose option 3
    elif choice == 3:
        
        #prints all of the items in the shopping_cart list
        for product in range(len(shopping_cart)):
            print(product, ". ", shopping_cart[product])

        print("Which item would you like to remove?")
        #Asks user what number to remove
        item = int(input("Enter item number: "))

        #Checks whether or not the cart is empty
        if len(shopping_cart) == 0:
            print("Your shopping cart is empty.")
            print("There is nothing to remove.")

        #If the cart isn't empty, then the item chosen to be removed will be removed
        else:
            print(shopping_cart[item - 1], "was removed from your cart.")
            shopping_cart.remove(item - 1)

    #Checks if the user chose option 4
    elif choice == 4:
        #checks whether the shopping_cart list is empty. in other words, it checks if the cart is empty
        if len(shopping_cart) == 0:
            print("Your shopping cart is empty.")

        #functions when the shopping_cart list isn't empty. in other words, it works when the cart is not empty
        else:
            #displays everything currently in the shopping cart
            for itm in range(len(shopping_cart)):
                print(itm, ". ", shopping_cart[itm], "     $", prices[shopping_cart.index[shopping_cart(itm)]])

        #prints the amount of items there are
        print("Total Items:", len(shopping_cart))

    #Checks if the user chose option 5
    elif choice == 5:
        subtotal = 0
        #calculates the total cost of everything in the cart
        for itm in range(len(shopping_cart)):
            subtotaltotal += prices[shopping_cart.index[shopping_cart(itm)]]

    #checks if the user chose option 6
    elif choice == 6:
        print("Subtotal: ", subtotal)
        if subtotal >= 40:
            print("Subtotal: ", subtotal)
            print("Discount: 15%")
            print("Amount Saved: ", subtotal * 0.15)
        elif 20 <= subtotal < 40:
            discount = 10
        print("Discount: ", discount)
        print("Amount Saved: ", )



        
    

