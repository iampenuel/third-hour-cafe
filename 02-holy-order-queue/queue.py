## PROJECT 2 - Holy Order Queue

# define the function take_order
def take_order():
    # print welcome message
    print("Welcome to The Third Hour: Order Queue™")
    
    # ask how many orders to be taken
    try:
        order_num = int(input("How many orders are we taking today? "))
    except ValueError:
        print("Please enter a valid number. Come back when your soul is ready for digits.")
        return
    
    # edge case check
    if order_num <= 0:
        print("No orders today? Sabbath rest is holy. Shutting down queue.")
        return

    # create new empty list
    order_list = []

    # establish counter
    i = 0

    # use while counter less than order numbers
    while i < order_num:
        # print order number i+1
        print(f"\nOrder #{i+1}")
        # get name
        name = input("Name: ").strip()
        # get drink
        drink = input("Drink: ").strip().title()
        # get full order
        full_order = f"{name}: {drink}"
        order_list.append(full_order)
        # get counter to loop through again till i=i
        i += 1

    # print queue summary
    print("\nHere's the queue:")
    # use for loop to get list content
    for content in order_list:
        # print list content
        print(f"- {content}")

    print("\nBless the baristas, and may your orders be anointed.")

# call the function
take_order()
