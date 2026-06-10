# Calculate the net income of a person using their hours worked, wages, and taxes
# INPUT: Have the user input their hours worked daily

# Loop to determine hours worked in a day
while(True):
    try:
        # prompt user to input hours daily as a float data type
        hours_worked_daily = float(input("Enter the number of hours you work daily: "))
        # if hours worked is less than 0, reprompt
        if hours_worked_daily < 0:
            print("Error: Enter a number no less than 0.\n")
            continue
        # if input is greater than 24, reprompt
        elif hours_worked_daily > 24:
            print("Error: Enter a number no greater than 24.\n")
            continue
        elif hours_worked_daily == float("nan"):
            print("Error: Enter a number.\n")
            continue
        break
    # if user inputs a value that can't be converted to a float, reprompt
    except:
        print("Error: Enter a number.\n")
        continue

# Loop to determine hourly wages
while(True):
    try:
         # prompt user to input hourly wages
         hourly_wages = float(input("Enter your hourly wages: $"))
         # if wages are less than 0, reprompt
         if hourly_wages <= 0:
             print("Error: Enter a value greater than 0.\n")
             continue
         elif hourly_wages == float("inf"):
             print("Error: Enter a finite value.")
             continue
         elif hourly_wages == float("nan"):
             print("Error: enter a number.\n")
             continue
         break
     # if user doesn't input a number, reprompt
    except:
         print("Error: Enter a number.\n")
         continue
# PROCESSING: calculate annual wages before taxes
annual_wages_before_taxes = hours_worked_daily * hourly_wages * 350.0
# deduct taxes
annual_wage_after_taxes = annual_wages_before_taxes * 0.88
tax_amount = annual_wages_before_taxes * 0.12
# print Pay Advice with hours worked per daily, wages, annual wages before and after taxes, and tax amount
print(f"Pay Advice\n-------------------\n")
print(f"Hours Worked Daily: {hours_worked_daily}\nHourly Wage: ${hourly_wages:.2f}")
print(f"Wages Before Taxes: ${annual_wages_before_taxes:.2f}\nTax Amount: ${tax_amount:.2f}")
print(f"Annual Wage After Taxes: ${annual_wage_after_taxes:.2f}")