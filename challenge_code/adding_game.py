# create a program that prompts user the difficulty and number of questions of an addition game and outputs their results
# create a function to get difficulty level
 # import random for random number generator
import random
def get_difficulty_level():
    # while loop until difficulty input is valid
    while (True):
        # INPUT: prompt user to input difficulty level 1, 2, or 3
        difficulty_level = input("Choose your difficulty level (1, 2, or 3): ")
        # IF int(difficulty) doesn't equal 1, 2, or 3, error message and continue
        try:
            int(difficulty_level)
            if int(difficulty_level) == 1 or int(difficulty_level) == 2 or int(difficulty_level) == 3:
                break
        except:
            print("ERROR: Please enter a valid difficulty level.")
            continue
        #else return and break
    return difficulty_level

# create a function to get question number
def get_question_number():
    # while loop until question number is valid
    while (True):
        # INPUT: prompt user to input number of questions from 3 to 10
        question_number = input("Choose your number of question (3 - 10): ")
        # IF int(question_number) does not equal 3 - 10, error message and continue
        try:
            int(question_number)
            if int(question_number) >= 3 and int(question_number) <= 10:
                break
            else:
                print("ERROR: Please enter a valid number of questions.")
        except:
            print("ERROR: Please enter a valid number of questions.")
            continue
    return question_number

# create a main function
def main():
    # call difficulty level function
    difficulty_level = int(get_difficulty_level())
    # call question number function
    question_number = int(get_question_number())
    
   
    random_generator = random.Random()


    # initialize correct = 0 and total = 0
    correct_answers = 0
    total_questions = 0
    # create for loop and set range to question number
    for question in range (question_number):
        # create random number generator and set peremeters for number based on value of difficulty level using IF statements
        if difficulty_level == 1:
            x = random_number = random_generator.randint(0, 9)
            y = random_number = random_generator.randint(0, 9)
        elif difficulty_level == 2:
            x = random_number = random_generator.randint(10, 99)
            y = random_number = random_generator.randint(10, 99)
        else:
            x = random_number = random_generator.randint(100, 999)
            y = random_number = random_generator.randint(100, 999)

        # create for loop to generate 2 numbers
        for _ in range (2):
            # number_1 = first generated number
            number = random_number

        # "number_1 + number_2" = question
        question = number[1] + number[2]

        # print question
        answer = input(f"{number[1]} + {number[2]} = ")
        # print question
        #INPUT: prompt user to input answer to question
        # if answer == question, print Correct and += correct and total
        # if answer != question, print error and reprompt up to 2 more times
        # after 3 attempts, print answer and += total

    # once all questions have been answered, print correct/total and correct/total * 100 (percentage)

# call main function
main()