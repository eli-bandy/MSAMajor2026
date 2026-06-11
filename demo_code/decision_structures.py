def main():
    a = 5
    b = 5

    if (a > b):
        print(f"a = {a} is greater than b = {b}.")
    elif (b > a):
        print(f"b = {b} is greater than a = {a}.")
    else:
        print(f"a = {a} is equal to b = {b}.")
    # print the appropriate letter grade based on a test score
    # A is 90 - 100, B: 80 - 89, C: 70 - 79, D: 60 - 69, F: < 60
    # test_score = 83: 
    # Output: 83 is a B
    print("\nGrade Decision: 1\n---------------")
    test_score = 82

    if (test_score >= 90):
        print(f"{test_score} --> A")
    elif (test_score < 90) and (test_score >= 80):
        print(f"{test_score} --> B")
    elif (test_score < 80) and (test_score >= 70):
        print(f"{test_score} --> C")
    elif (test_score < 70) and (test_score >= 60):
        print(f"{test_score} --> D")
    else:
        print(f"{test_score} --> F")

    print(f"\n{test_score <= 100} and {test_score >= 90}")

    print("\nGrade Decision: 2\n---------------")
    if (test_score >= 90):
        print(f"{test_score} --> A")
    elif (test_score >= 80):
        print(f"{test_score} --> B")
    elif (test_score >= 70):
        print(f"{test_score} --> C")
    elif (test_score >= 60):
        print(f"{test_score} --> D")
    else:
        print(f"[test_score --> F]")

    c = 4
    d = 10

    if (a == 4) or (b == 15) or (c == 5) or (d == 9):
        print("The OR condition is True.")
    else:
        print("The OR condition is false.")

main()