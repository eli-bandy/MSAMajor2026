# create a program for a vending machine that sells snacks for 50 cents
# Input: have user input values in coin denominations of 1, 5, 10, or 25
# display amount owed until the user inputs at least 50 cents
# Output: once at least 50 cents are inputted, display to the user how much change is owed

# create a function for amount_paid

# create a main function
def main():
         # create a while loop to continue prompting user to input coins until 50 cent threshold is achieved
    amount_owed = 50
    print("Vending Machine\n ---------")
    while(True):
        print(f"Amount Due: {amount_owed}")
        coin = (input(f"Insert Coin: "))


        # if amount_owed <= 0 cents, break
            # validate that the coin denomination inputted is 1, 5, 10, or 25
        # if valid denomination used, subtract inputted value and continue loop
        if coin == "1" or coin == "5" or coin == "10" or coin == "25":
            amount_owed = amount_owed - int(coin)
            
            if amount_owed <= 0:
                print(f"Change Owed: {amount_owed * -1}")
                break
        # if invalid coin used, reprompt with no error message
        else:
            continue



        # make a variable for change_due = amount_paid - 50
        # print(f"Change Owed: {change_due}")
# call main function
print("Amount Due: 50")
main()