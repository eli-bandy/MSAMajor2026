# create a decision structure to determine the season
# seasons are winter, spring, summer, fall
# ask the user to enter the number of the month. Month must be 1 - 12
# winter: 12, 1, 2 | spring: 3, 4, 5 | summer: 6, 7, 8 | fall: 9, 10, 11
# Output the season
# Prompt: enter month number: 11
# Output: it is fall
# create a function to have user input the month number
def main():
    while (True):
        try:
            month_number = int(input(f"Enter the number of the current month: "))
            # Ensure input is a number 1 - 12
            if month_number <= 0 or month_number > 12:
                print("Error: Enter a valid month number.")
                continue
            elif (month_number == 12) or (month_number <= 2):
                print("It is Winter.")
                break
            elif (month_number <= 5):
                print("It is Spring.")
                break
            elif (month_number <= 8):
                print("It is Summer.")
                break
            elif (month_number <= 11):
                print ("It is Fall.")
                break
        # Ensure input is an integer
        except:
            print("Error: Enter an integer.")
            continue

main()