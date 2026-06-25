from Student import Student

"""
Function top return a list of student objects
INPUT: none
OUTPUT: list of student objects
"""
def load_students() -> list[Student]:
    # open data file
    data_file = open("students.csv", "r")

    student_info_list = []
    line_number = 0
    
    # create a for loop to split data at commas
    for line_of_data in data_file:
        # skip first line
        line_number += 1
        if line_number == 1:
            continue
        
        # student_data = split data at commas
        student_info = line_of_data.split(",")

        # handle errors in data format. line_of_data should have 6 items
        # if error in format then write to a log file
        try:
            if len(student_info) != 6:
                raise Exception(f"Error on line {line_number} of the file. Data has {len(student_info)} items, but should have 6 items.\n")
        except Exception as error:
            #raise Exception(f"Error on line {line_number} of the file. Data has {len(student_info)} items, but should have 6 items.\n")
            continue
        # first_name = student_data[0], last_name = student_data[1], etc.
        first_name = student_info[0]
        last_name = student_info[1]
        major = student_info[2]
        try:
            credit_hours = int(student_info[3])
            gpa = float(student_info[4])
        except:
            print(f"Error on line {line_number}.")
            continue
        student_id = student_info[5].strip()
        
        # create a student object
        student = Student(first_name, last_name, major, credit_hours, gpa, student_id)
        # append the student to the student info list
        student_info_list.append(student)

    # close file
    data_file.close
    return student_info_list
"""
Function to convert student objects into student dictionaries
INPUT: list of student objects
OUTPUT: list of student dictionaries
"""
def student_to_dictionary(list_of_students: list[Student]) -> list[dict]:
    # create an empty list to store the dictionaries
    student_dictionary_list = []

    # loop through the list and write each student's data to a dictionary
    for student in list_of_students:
        # create an empty dictionary
        student_dictionary = {}

        # make entries into the dictionary using the student properties
        # first name, last name, major, gpa, class, id
        student_dictionary['first_name'] = student.get_first_name()
        student_dictionary['last_name'] = student.get_last_name()
        student_dictionary['major'] = student.get_major()
        student_dictionary['gpa'] = student.get_gpa()
        student_dictionary['class'] = student.get_class_level()
        student_dictionary['id'] = student.get_id_number()

        # append the dictionary to the list of dictionaries
        student_dictionary_list.append(student_dictionary)
    # return the list of dictionaries
    return student_dictionary_list

"""
Function to get student dictionaries
INPUT: none
OUTPUT: a list of student dictionaries
"""
def get_student_dictionaries():
    # get a list of students
    student_list = load_students()

    # get a list of student dictionaries
    student_dictionaries = student_to_dictionary(student_list)

    return student_dictionaries
