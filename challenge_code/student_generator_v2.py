from Student import Student

def main():
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

     # create a for loop to print students   
    for student in student_info_list:
        student.print_student_data()

    # close file
    data_file.close

main()