class Course:
    def __init__(self, code, name, credit, semester, instructor):
        self.code = code
        self.name = name
        self.credit = credit
        self.semester = semester
        self.instructor = instructor

    def __str__(self):
        return f"{self.code} - {self.name} ({self.credit} credits, Semester {self.semester}, Instructor: {self.instructor})"


class Student:
    def __init__(self, first_name, last_name, number):
        self.first_name = first_name
        self.last_name = last_name
        self.number = number
        self.courses = {}

    def __str__(self):
        return f"{self.number} - {self.first_name} {self.last_name}"

    def set_course_mark(self, course, grade):
        self.courses[course] = grade

    def get_gpa(self):
        if not self.courses:
            return 0.0
        total = sum(self.courses.values())
        count = len(self.courses)
        return total / count


class University:
    def __init__(self, name):
        self.name = name
        self.students = []

    def __str__(self):
        return f"University: {self.name} (Students: {len(self.students)})"

    def register_student(self, student):
        self.students.append(student)

    def grade_students(self):
        print(f"--- {self.name} Student GPAs ---")
        for s in self.students:
            print(f"{s}: GPA = {s.get_gpa():.2f}")


university = University("Gisma")
print(university)
print()

course1 = Course("CS101", "Introduction to Programming", 4, 1, "Dr. Smith")
course2 = Course("MATH201", "Calculus I", 3, 1, "Prof. Johnson")
course3 = Course("ENG101", "English Literature", 3, 1, "Dr. Brown")

print("Available Courses:")
print(course1)
print(course2)
print(course3)
print()

student1 = Student("John", "Doe", "S001")
student2 = Student("Jane", "Smith", "S002")
student3 = Student("Alice", "Johnson", "S003")

print("Registering Students:")
university.register_student(student1)
print(f"Registered: {student1}")
university.register_student(student2)
print(f"Registered: {student2}")
university.register_student(student3)
print(f"Registered: {student3}")
print()

print("Setting Course Marks:")
student1.set_course_mark(course1, 85)
student1.set_course_mark(course2, 90)
student1.set_course_mark(course3, 88)
print(f"{student1.first_name} enrolled in {len(student1.courses)} courses")

student2.set_course_mark(course1, 92)
student2.set_course_mark(course2, 87)
print(f"{student2.first_name} enrolled in {len(student2.courses)} courses")

student3.set_course_mark(course1, 78)
student3.set_course_mark(course2, 82)
student3.set_course_mark(course3, 91)
print(f"{student3.first_name} enrolled in {len(student3.courses)} courses")
print()

university.grade_students()
print()

print("Individual Student Information:")
print(f"{student1.first_name} {student1.last_name}'s GPA: {student1.get_gpa():.2f}")
print(f"{student2.first_name} {student2.last_name}'s GPA: {student2.get_gpa():.2f}")
print(f"{student3.first_name} {student3.last_name}'s GPA: {student3.get_gpa():.2f}")
print()

print(f"Total students at {university.name}: {len(university.students)}")
