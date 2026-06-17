# create a program that prompts the user to input a valid menu item and outputs the total cost of the order

# function to load data from a file and return a dictionary
# INPUT: filename: string
# OUTPUT: dictionary

def load_menu_items(filename:str) -> dict:
    # open menu.txt: create a file handler to open file in read mode
    data_file = open(filename, "r")

    # create an empty dictionary
    menu_items = {}
    # use a loop to read the contents of the file line by line
    for line_of_data in data_file:
        # split the line at the comma
        item_name_and_price = line_of_data.split(",")

        # get the item and price from the list
        item_name = item_name_and_price[0]
        item_price = float(item_name_and_price[1])

        # create an entry in the dictionary for the item and price
        menu_items[item_name] = item_price

    # close the file
    data_file.close()

    # return the dictionary of menu items
    return menu_items

# create a main function
def main():
    #  create a dictionary of the menu items
    menu_items = load_menu_items("menu.txt")
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
        if item.title() not in menu_items.keys():
            # if item is invalid, continue loop
            continue
    
        # add item to total by using square brackets to get value paired with item and avoid accidentally trying to add the string to the total
        total += menu_items[item.title()]
        # print total and repeat loop
        print(f"Total: ${total:,.2f}\n---------------")

# call main function
main()