# create a program that prompts the user to input a valid menu item and outputs the total cost of the order
# create a main function
def main():
    #  create a dictionary of the menu items
    menu = {"Baja Taco": 4.00, "Burrito": 7.50, "Bowl": 8.50, "Nachos": 11.00, "Quesadilla": 8.50, "Super Burrito": 8.50, "Super Quesadilla": 9.50, "Taco": 3.00, "Tortilla Salad": 8.00}
    # initialize the total of $0.00
    total = 0.00

    # create a while loop to allow user to continue to input menu items
    while (True):
        # INPUT: prompt user to input their menu item of choice
        item = input("Item: ")
        # determine if "End" is typed in any case; if so, end program
        if item.title() == "End":
            # OUTPUT: print final total and end program
            print(f"Enjoy your meal! Your total is ${total:,.2f}.")
            break
        # PROCESS: use an IF statement to determine whether or not the item is valid
        if item.title() not in menu.keys():
            # if item is invalid, continue loop
            continue
    
        # add item to total by using square brackets to get value paired with item and avoid accidentally trying to add the string to the total
        total += menu[item.title()]
        # print total and repeat loop
        print(f"Total: ${total:,.2f}\n---------------")

# call main function
main()