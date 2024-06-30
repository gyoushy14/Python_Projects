class Student:
    # Class variable to keep track of all student objects
    all_students = []

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        # Adding the newly created student object to the list of all students
        Student.all_students.append(self)

    def update_grade(self, new_grade):
        self.grade = new_grade

    def display_student_info(self):
        try:
            print(f"Student Name: {self.name}, Grade: {self.grade}")
        except AttributeError:
            print(f"Student Name: {self.name} has no recorded grade.")

    @classmethod
    def display_all_students(cls):
        if cls.all_students:
            print("All Students:")
            for student in cls.all_students:
                student.display_student_info()
        else:
            print("No students available.")

    @classmethod
    def delete_student(cls, student):
        # Attempt to remove the student from the list, if they exist
        try:
            cls.all_students.remove(student)
            del student
        except ValueError:
            print(f"Student not found in the list.")
        except NameError:
            print(f"Student object does not exist.")

# Creating several Student objects
student1 = Student("Alice", "A")
student2 = Student("Bob", "B")
student3 = Student("Charlie", "C")

# Update the grade of a student
student1.update_grade("A+")

# Display all students
Student.display_all_students()

# Delete the grade attribute of a student object and attempt to display it
del student2.grade
student2.display_student_info()

# Delete a Student object and try accessing it afterward
Student.delete_student(student3)
try:
    student3.display_student_info()
except NameError as e:
    print("This student has been deleted.", e)

# Display all students after deletion
Student.display_all_students()

