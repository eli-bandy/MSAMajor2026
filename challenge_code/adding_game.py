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
        question_number = input("Choose your number of questions (3 - 10): ")
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

        # "x + y" = question
        question = x + y

        # if answer != question, print error and reprompt up to 2 more times
        for attempts in range (3):
            #INPUT: prompt user to input answer to question
            answer = input(f"{x} + {y} = ")
            attempts_left = 3 - attempts
            try:
                int(answer)
                if int(answer) != question:
                    if attempts_left - 1 != 0:
                        print(f"Wrong! You have {attempts_left - 1} more attempt(s).")
                        continue
                    else:
                        print(f"Wrong! The correct answer is {question}.")
                        total_questions += 1
                        break
                else:
                    print("Correct!")
                    total_questions += 1
                    correct_answers += 1
                    break
            except:
                if attempts_left - 1 != 0:
                    print(f"Wrong! You have {attempts_left - 1} more attempt(s).")
                    continue
                else:
                    print(f"Wrong! The correct answer is {question}.")
                    total_questions += 1
                    break

    # once all questions have been answered, print correct/total and correct/total * 100 (percentage)
    percentage = (correct_answers / total_questions) * 100
    if percentage == 100:
        grade = "Congratulations! You got a perfect score!"
    elif percentage >= 89.5:
        grade = "A"
    elif percentage >= 79.5:
        grade = "B"
    elif percentage >= 69.5:
        grade = "C"
    elif percentage >= 59.5:
        grade = "D"
    else:
        grade = "F"
    print(f"\nResults: {grade}\n---------------\nYou got {correct_answers} out of {total_questions} questions correct.\n{percentage:.2f}%")

# call main function
main()