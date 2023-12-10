shop = 'Paws n Cart'
shopping_cart = []
# display the user menu and cart until checkout
done = False
while not done:
    print("\n", "-" * 80, "\n This is your shopping cart.\n", "-" * 80)
    print(" Would you like to: \n"
          "\t1: Add an item to your cart.\n"
          "\t2: Remove an item from your cart.\n"
          "\t3: View the items in your cart.\n"
          "\t4: Change the quantity of an item.\n"
          "\t5: View the total cost of your cart.\n"
          "\t6: Checkout.\n", "-" * 80)
    while True:
        try:
            choice = int(input("Enter the number of the item you would like to choose:\n"))
            break
        except ValueError:
            print("Please enter a number.")
    if choice == 1:
        # find out item and price and add them to the cart
        item = input("What item would you like to add to your cart? ")
        price = float(input("How much does the item cost? £"))
        amt = int(input("How many would you like to add? "))
        new_item = {'item': item, 'price': price, 'amt': amt}
        shopping_cart.append(new_item)
    elif choice == 2:
        # find item that must be removed and check if it is in the cart
        remove = input("Which item would you like to remove? ")
        removed = 0
        for i in range(len(shopping_cart)):
            if shopping_cart[i]['item'] == remove:
                del shopping_cart[i]
                removed += 1
                break
        if removed > 0:
            print(f"{remove} has been removed from the shopping cart.")
        else:
            print(f"{remove} is not in your cart.")
    elif choice == 3:
        # display all the items in the cart, and the total cost
        total = 0
        print(" #\tItem\t\t\t\t\t\tQuantity\t\t\tCost")
        print("-"*80)
        for _ in range(len(shopping_cart)):
            print(f" {_+1}\t{shopping_cart[_]['item']}\t\t\t\t\t"
                  f"{shopping_cart[_]['amt']}\t\t\t\t\t£{shopping_cart[_]['price']:.2f}")
        print('-'*80)
        for _ in range(len(shopping_cart)):
            total += shopping_cart[_]['price'] * shopping_cart[_]['amt']
        print(f"\t\t\t\t\t\t\t\t\t\t\t\t\t£{total:.2f}")
    elif choice == 4:
        # edit the quantity of one of the items
        print("These are the items in your cart:\n")
        for _ in range(len(shopping_cart)):
            print(f" {_+1}\t{shopping_cart[_]['item']}")
        print('-' * 80)
        while True:
            try:
                edit = int(input("Please select the item you would like to edit. "))
                print(f"You have selected {shopping_cart[edit-1]['item']}, "
                      f"the current quantity is {shopping_cart[edit-1]['amt']}.")
                break
            except ValueError:
                print("Please enter a number")
        while True:
            try:
                new_amt = int(input("Please enter the new quantity: "))
                break
            except ValueError:
                print("Please enter a number")
        shopping_cart[edit-1]['amt'] = new_amt
        print(f"You have successfully updated the quantity of {shopping_cart[edit-1]['item']} "
              f"to {shopping_cart[edit-1]['amt']}.")
    elif choice == 5:
        total = 0
        # calculate the cost of all items in the cart
        for _ in range(len(shopping_cart)):
            total += shopping_cart[_]['price'] * shopping_cart[_]['amt']
        print(f"The total cost of your cart is £{total:.2f}")
    elif choice == 6:
        # exit from the program
        print(f"Thank you for shopping with {shop}!")
        done = True
    else:
        print("That is not a valid option.")
