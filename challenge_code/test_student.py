from Student import Student
def main():
    # create a student
    test_student = Student("Truman", "Tiger", "Mizzou Staff", 1839, 4.5, "12345678")

    test_student.print_student_data()

    # test the set credit hours method
    test_student.set_credit_hours(55)
    test_student.print_student_data()

    # test update credit hours
    test_student.update_credit_hours(20)
    test_student.print_student_data()

main()