"""
By Kamran Bigdely Nov. 2020
Replace temp variable with query
Use 'extract method' refactoring technique to improve this code. If required, use
'replace temp variable with query' technique to make it easier to extract methods.
"""

class Employer:
    """Creates a new Emplyer objects with the given name"""
    def __init__(self, name):
        self.name = name

    def send(self, students):
        """Prints out that students contact info was send to the employer."""
        print(f"{', '.join(students)}' contact info were sent to", self.name + '.')

class Student:
    """Creates a new Student object from the given gpa and name"""
    def __init__(self, gpa, name):
        self.gpa = gpa
        self.name = name

    def get_gpa(self):
        """Returns the students current gpa"""
        return self.gpa

    def send_congrat_email(self):
        """Prints a congrats message using the students name"""
        print("Congrats", self.name + ". You graduated successfully!")

class School:
    """Creates a new School object from the given students"""
    def __init__(self, students) -> None:
        self.students = students
        self.top_employers = [
            Employer('Microsoft'),
            Employer('Free Software Foundation'),
            Employer('Google')
        ]

    def get_passed_students(self):
        """Finds the students in the school that have a gpa greater than 2.5."""
        min_gpa = 2.5 # minimum acceptable GPA
        passed_students = []
        for student in self.students:
            if student.get_gpa() > min_gpa:
                passed_students.append(student)
        return passed_students

    def get_students_in_top_n_precent(self, percentile):
        """Gets the top 10% of students based on their gpa"""
        students = self.get_passed_students()
        students.sort(key=lambda s: s.get_gpa())
        index = int(percentile * len(students))
        return students[index:]

    def process_graduation(self):
        """
        Prints out passing students and also the top employer where studetns in the to 10
        percent's contact infromation were send to
        """
        passed_students = self.get_passed_students()

        # print student's name who graduated.
        print('*** Student who graduated *** ')
        for student in passed_students:
            print(student.name)
        print('****************************')

        # Send congrats emails to them.
        for student in passed_students:
            student.send_congrat_email()

        top_10_percent = self.get_students_in_top_n_precent(0.9)
        for employer in self.top_employers:
            employer.send(top_10_percent)


school_students = [Student(2.1, 'donald'), Student(2.3, 'william'), Student(2.7, 'toro'),
            Student(3.9, 'lili'), Student(3.2,'kami'), Student(3,'sarah')]
school  = School(school_students)
school.process_graduation()
