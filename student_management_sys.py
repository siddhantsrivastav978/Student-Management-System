import json
def add_student():

    student_id = input("Enter student ID: ")
    for s in students:
        if s ['id'] == student_id:
            print("\nStudent ID already exists. Please try again.")
            return
    student_name = get_valid_name()
    student_age = get_valid_age()
    student_course = get_valid_course()

    new_student = {
        "id": student_id,
        "name": student_name,
        "age": student_age,
        "course": student_course
    }

    students.append(new_student)
    save_students()

    print("\nStudent added successfully!")

def display_students():
          
    if len(students) == 0:
        print("\nNo students found.")
        return
    print("\n===== Student List =====")
        
    for s in students:
        print("-------------------------")
        print(f"ID: {s['id']}")
        print(f"Name: {s['name']}")
        print(f"Age: {s['age']}")
        print(f"Course: {s['course']}")
        print("-------------------------")

def search_student():
    student_id = input("Enter student ID to search: ")

    for s in students:
        if s['id'] == student_id:
            print("\n===== Student Details =====")
            print(f"ID: {s['id']}")
            print(f"Name: {s['name']}")
            print(f"Age: {s['age']}")
            print(f"Course: {s['course']}")
            return

    print("\nStudent not found.")

def update_student():
    student_id = input("Enter student ID to update:")

    for s in students:
        if s['id'] ==student_id:
            print("\n===== update student Detials =====")
            s['name'] = get_valid_name()
            s['age'] = get_valid_age()
            s['course'] = get_valid_course()
            save_students()
            return

    print("\nStudent not found.")     

def delete_student():
    student_id = input("Enter student ID to delete: ")

    for s in students:
        if s['id'] == student_id:
            students.remove(s)
            print("\nStudent deleted successfully!")
            save_students()
            return

    print("\nStudent not found.")    

def save_students():
    with open("students.json","w")as file:
        json.dump(students,file,indent=4)

def load_students():
    try:
        with open("students.json","r")as file:
            return json.load(file)
        
    except FileNotFoundError:
        return []
    
students = load_students()

def get_valid_age():
    while True:
        age = input("Enter student age: ")
        if not age.isdigit() :
            print("Invalid age. Please enter a valid number.")
            continue
        age = int(age)
        if age < 1 or age > 120:
            print("Invalid age. Please enter a valid age between 1 and 120.")
            continue
        return age
    
def get_valid_name():
    while True:
        name = input("Enter student name: ")
        name = name.strip()
        if not name:
            print("Invalid name. Please enter a valid name.")
            continue
        return name

def get_valid_course():
    while True:
        course = input("Enter student course: ")
        course = course.strip()
        if not course:
            print("Invalid course. Please enter a valid course.")
            continue
        return course
    
def student_statistics():
    total_students = len(students)
    if total_students == 0:
        print("\nNo students found.")
        return

    max_age = int(students[0]['age'])
    min_age = int(students[0]['age'])
    total_age = 0

    for s in students:
        age = int(s['age'])
        total_age += age
        if age > max_age:
            max_age = age
        if age < min_age:
            min_age = age

    average_age = total_age / total_students

    print("\n===== Student Statistics =====")
    print(f"Total Students: {total_students}")
    print(f"oldest Student: {max_age}")
    print(f"youngest Student: {min_age}")
    print(f"Average Age: {average_age:.2f}")

def sort_students():
    print("\n===== Sort Students =====")
    print("1. Sort by Name") 
    print("2. Sort by Age")
    print("3. sort by id")    
    print("4. back to main menu")
    choice = input("Enter your choice (1/2/3/4):")
    if choice == '1':
        students.sort(key=lambda s: s['name'])
        print("\nStudents sorted successfully by name.")
        display_students()
    elif choice == '2':
        students.sort(key=lambda s: int(s['age']))
        print("\nStudents sorted successfully by age.")
        display_students()
    elif choice == '3':
        students.sort(key=lambda s: s['id'])
        print("\nStudents sorted successfully by ID.")
        display_students()
    elif choice == '4':
        return 
    else:
        print("Invalid choice. Please try again.")

while True:

    print("\n===== Student Management System =====")
    print("\n1. Add Student")
    print("2. Display Students")
    print("3. Search Student by ID")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Student Statistics")
    print("7. Sort Students")
    print("8. Exit")

    choice = input("Enter your choice (1/2/3/4/5/6/7/8): ")

    if choice == '1':
        add_student()

    elif choice == '2':
        display_students()

    elif choice == '3':
        search_student()

    elif choice == '4':
        update_student()
        print("\nStudent updated successfully!")
        display_students()

    elif choice == '5':
        delete_student()

    elif choice == '6':    
        student_statistics()

    elif choice == '7':
        sort_students()

    elif choice == '8':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")