students = []

class Student:
    school_name = "Springfield Elementary"

    def __init__(self, first_name, last_name, student_id=332):
        self.first_name = first_name
        self.last_name = last_name
        self.name = first_name + " " + last_name
        self.student_id = student_id
        students.append(self)

    def __str__(self):
        return "Student " + self.name

    def get_name_capitalize(self):
        return self.name.capitalize()

    def get_school_name(self):
        return self.school_name
