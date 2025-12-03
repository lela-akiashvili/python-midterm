import os

# Base Class: Person (Identity + Inheritance)

class Person:
    def __init__(self, name):
        self._name = name        # Encapsulation via protected attribute

    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name


# Derived Class: Student (Inheritance + Polymorphism)

class Student(Person):
    def __init__(self, name, roll_number, grade):
        super().__init__(name)   # Inherit from Person
        self._roll_number = roll_number
        self._grade = grade

    # Encapsulated Getters/Setters
    def get_roll_number(self):
        return self._roll_number

    def get_grade(self):
        return self._grade

    def set_grade(self, grade):
        self._grade = grade

    # Polymorphism Example: Display method overridden
    def display_info(self):
        print(f"Name: {self._name}, Roll Number: {self._roll_number}, Grade: {self._grade}")


# Student Management System Class (Encapsulation)

class StudentManager:
    def __init__(self):
        self.students = []   # Array/List of student objects

    
    # Add New Student
    
    def add_student(self, name, roll_number, grade):
        student = Student(name, roll_number, grade)
        self.students.append(student)
        print("Student added successfully.")

    
    # View All Students
    
    def view_all_students(self):
        if not self.students:
            print("No students found.")
            return
        for student in self.students:
            student.display_info()

    
    # Search by Roll Number
    
    def search_by_roll(self, roll_number):
        for student in self.students:
            if student.get_roll_number() == roll_number:
                student.display_info()
                return student
        print("Student not found.")
        return None

    
    # Update Student Grade
    
    def update_grade(self, roll_number, new_grade):
        student = self.search_by_roll(roll_number)
        if student:
            student.set_grade(new_grade)
            print("Grade updated successfully.")

    
    # File Operations
    
    def save_to_file(self, filename="students.txt"):
        with open(filename, "w") as file:
            for student in self.students:
                file.write(f"{student.get_name()},{student.get_roll_number()},{student.get_grade()}\n")
        print("Students saved to file.")

    def load_from_file(self, filename="students.txt"):
        if not os.path.exists(filename):
            print("No existing student file found.")
            return

        with open(filename, "r") as file:
            for line in file:
                name, roll, grade = line.strip().split(",")
                self.add_student(name, int(roll), grade)

        print("Students loaded from file.")

    def delete_file(self, filename="students.txt"):
        if os.path.exists(filename):
            os.remove(filename)
            print("File deleted.")
        else:
            print("File does not exist.")


# Input Validation Helpers

def input_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Enter a valid number.")

def input_grade(prompt):
    while True:
        grade = input(prompt).upper()
        if len(grade) == 1 and grade.isalpha():
            return grade
        print("Invalid grade. Enter a single letter (A-Z).")


# Console Menu System

def main():
    manager = StudentManager()

    # Attempt to load existing data
    manager.load_from_file()

    while True:
        print("\n===== Student Management System =====")
        print("1. Add New Student")
        print("2. View All Students")
        print("3. Search Student by Roll Number")
        print("4. Update Student Grade")
        print("5. Save to File")
        print("6. Delete File")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            name = input("Enter Name: ")
            roll = input_int("Enter Roll Number: ")
            grade = input_grade("Enter Grade: ")
            manager.add_student(name, roll, grade)

        elif choice == "2":
            manager.view_all_students()

        elif choice == "3":
            roll = input_int("Enter Roll Number: ")
            manager.search_by_roll(roll)

        elif choice == "4":
            roll = input_int("Enter Roll Number: ")
            grade = input_grade("Enter New Grade: ")
            manager.update_grade(roll, grade)

        elif choice == "5":
            manager.save_to_file()

        elif choice == "6":
            manager.delete_file()

        elif choice == "7":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Try again.")


# Start program

if __name__ == "__main__":
    main()
