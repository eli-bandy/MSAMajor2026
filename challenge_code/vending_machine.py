# create a program for a vending machine that sells snacks for 50 cents
# Input: have user input values in coin denominations of 1, 5, 10, or 25
# display amount owed until the user inputs at least 50 cents
# Output: once at least 50 cents are inputted, display to the user how much change is owed

# create a function for amount_paid
def amount_paid():
        # create a while loop to continue prompting user to input coins until 50 cent threshold is achieved
    while(True):
        try:
            print(f"{amount_owed}")
            coin = int(input("Insert Coin: "))
            # if amount_owed <= 0 cents, break
              # validate that the coin denomination inputted is 1, 5, 10, or 25
            # if valid denomination used, subtract inputted value and continue loop
            if coin == 1 or 5 or 10 or 25:
                amount_owed = 50 - coin
            # if invalid coin used, reprompt with no error message
            if coin != 1 or 5 or 10 or 25:
                continue
            
            elif amount_owed > 0 and amount_owed < 50:
                continue
        except:



      
       
      

        
    # return value

# create a main function
    # make a variable for change_due = amount_paid - 50
    # print(f"Change Owed: {change_due}")

# call main function
        
        