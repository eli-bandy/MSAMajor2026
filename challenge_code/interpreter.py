def main():
# while loop
    while(True):
        # INPUT
        # prompt the user to enter an expression
        expression = input("Expression (X Y Z): ")

        # PROCESS
        # validate the expression format
            # use the split method to split the expression at the space " "
        expression_validation = expression.split(" ")
            # if the length of the resulting list is not 3, then invalid format
        if len(expression_validation) != 3:
            print("Error: Incorrect Format")
            continue
        # validate that X and Z are integers
        x = expression_validation[1]
        y = expression_validation[2]
        z = expression_validation[3]
        # convert X and Z to integers
        try:
            x = int(x)
            z = int(z)
            # if converting causes an exception, then invalid format
        except:
            print(f"Error: {x} and/or {z} is not an integer.")
            continue

        # validate that Y is an acceptable operator (+, -, *, /)
            # use an IF statement to determine if Y == + or - or * or /
            # invalid format if not
        if y != "+" or y != "-" or y != "*" or y != "/":
            print(f"Error: {y} is not a valid operator")
            continue


        # validate that when Y is /, Z is not 0
            # use IF: if Y == "/" and Z == 0: divide by 0 error

        # do the math
            # use IF statements to carry out each of 4 operations as X Y Z converted as floats

        # OUTPUT
        # print the output to the user and offer user the option to reprompt
        break

main()