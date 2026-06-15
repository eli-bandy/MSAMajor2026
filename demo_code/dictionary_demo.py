def main():
    # the need for dictionaries
    scores = [55, 75, 87, 82, 91]
    students = ["Alice", "Bob", "Jerry", "Jane", "Bill"]

    # print the names of the students with their scores
    print("Students and scores using the lists\n--------------")
    for index in range (len(scores)):
        print(f"{students[index]}: {scores[index]}")

    # create a dictionary of names and scores
    student_scores = {
        "Alice" : 55,
        "Bob" : 75,
        "Jerry" : 87,
        "Jane" : 82,
        "Bill" : 91
    }    

    # print Bob and Janes' scores
    print("\nPrint Bob and Jane's Scores\n-------------------")
    print(student_scores["Bob"])
    print(student_scores["Jane"])

    # print all the data in the students scores dictionary
    print("\nPrint all Student Data\n-----------------")
    for student in student_scores:
        print(f"{student}: {student_scores[student]}")

main()