# Program to convert lbs to kilograms
# INPUT (getting the data that will be processed)

# loop
while(True):
    #   Validate input: ensure the data is a number type
    try:
        # Prompt user to enter weight in lbs
        user_weight = float(input("Enter weight in lbs: "))
        # if weight is less than or equal to 0, output error message and reprompt the user
        if user_weight <= 0:
            print("Error: Enter a number greater than 0.\n")
            continue
        break
    except:
        print("ERROR: Please enter a number.\n")
        continue
#   if the input is invalid then reprompt the user until the input is valid

# PROCESSING
# Use a conversion factor to convert lbs to kgs (2.205 lbs = 1 kg)
lbs_to_kg = 2.205
user_weight_in_kg = user_weight / lbs_to_kg

# OUTPUT
# Print the output to the user
print(f"You weigh {user_weight_in_kg:.2f} kgs.")