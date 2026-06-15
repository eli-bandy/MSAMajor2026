def main():
# while loop
    while(True):
        # INPUT
        # prompt the user to enter an expression
        expression = input("Expression (X Y Z Format): ")

        # PROCESS
        # validate the expression format
            # use the split method to split the expression at the space " "
        expression_validation = expression.split(" ")
            # if the length of the resulting list is not 3, then invalid format
        if len(expression_validation) != 3:
            print("Error: Incorrect Format")
            continue
        # validate that X and Z are integers
        x = expression_validation[0]
        y = expression_validation[1]
        z = expression_validation[2]
        # convert X and Z to integers
        try:
            x = int(x)
            z = int(z)
            # if converting causes an exception, then invalid format
        except:
            print(f"Error: {x} and/or {z} is not an integer.")
            continue

        # validate that when Y is /, Z is not 0
            # use IF: if Y == "/" and Z == 0: divide by 0 error
        if y == "/" and z == 0:
            print("Error: Unable to Divive by Zero")
            continue

        # do the math
            # use IF statements to carry out each of 4 operations as X Y Z converted as floats
            # create outputs for each operation
        valid_operators = ["+", "-", "*", "/"]
        if y not in valid_operators:
            print(f"Error: {y} is not a valid operator.")
            continue

        if y == "+":
            print(f"{(float(x) + float(z)):,}")
            break
        elif y == "-":
            print(f"{(float(x) - float(z)):,}")
            break
        elif y == "*":
            print(f"{(float(x) * float(z)):,}")
            break
        elif y == "/":
            print(f"{(float(x) / float(z)):,.2f}")
            break

    
    # offer to reprompt user
    while(True):
        reprompt_option = input("Would you like to create another expression? Press y for yes or n for no: ")
        if reprompt_option.lower() == "y":
            main()
        elif reprompt_option.lower() == "n":
            break
        
# OUTPUT
# print the output to the user
main()