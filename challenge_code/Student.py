# create a class that determines the class of the students
class Student:
    # define a constructor that is the function that is called to generate student info
    def __init__(self, first_name:str, last_name:str, major:str, credit_hours:int, gpa:float, id_number:str):
        # define class properties with parameter values
        self.__first_name = first_name
        self.__last_name = last_name
        self.__major = major
        self.__credit_hours = credit_hours
        self.__gpa = gpa
        self.__id_number = id_number

    # create a getter and setter method for class properties
    def get_first_name(self):
        return self.__first_name
    def set_first_name(self, new_first_name:str):
        self.__first_name = new_first_name
        return
    
    def get_last_name(self):
        return self.__last_name
    def set_last_name(self, new_last_name:str):
        self.__last_name = new_last_name
        return
    
    def get_major(self):
        return self.__major
    def set_major(self, new_major:str):
        self.__major = new_major
        return
    
    def get_credit_hours(self):
        return self.__credit_hours
    def set_credit_hours(self, new_credit_hours:int):
        self.__credit_hours = new_credit_hours
        return
    
    def get_gpa(self):
        return self.__gpa
    def set_gpa(self, new_gpa:float):
        self.__gpa = new_gpa
        return
    
    def get_id_number(self):
        return self.__id_number
    
    # create a method to determine class of student
    def get_class_level(self):
        credit_hours = self.__credit_hours
        if credit_hours > 90:
            return "Senior"
        elif credit_hours > 60:
            return "Junior"
        elif credit_hours > 30:
            return "Sophomore"
        else:
            return "Freshman"

    # create a method to update credit hours
    def update_credit_hours(self, additional_hours:int):
        self.__credit_hours += additional_hours
        return

    # create a method to print student data
    def print_student_data(self):
        student_class = self.get_class_level()
        print(f"\nTranscript:\n-------------------------------\n{self.__first_name} {self.__last_name}\nClass Level: {student_class}, Major: {self.__major}")
        print(f"GPA: {self.__gpa}, ID: {self.__id_number}")