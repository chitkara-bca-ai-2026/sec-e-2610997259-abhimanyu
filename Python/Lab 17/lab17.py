def calculate_results(marks):
    total = sum(marks)
    average = total / len(marks)
    return total, average

def display_student(roll, students):
    info = students[roll]
    total, avg = calculate_results(info["Marks"])
    print("Roll No:", roll, "| Name:", info["Name"], "| Marks:", info["Marks"], "| Total:", total, "| Average:", str(round(avg, 2)) + "%")

def add_student(records, roll, name, marks):
    if roll in records:
        print("[ERROR] Roll Number already exists!")
    else:
        records[roll] = {
            "Name": name,
            "Marks": marks
        }
        print("[SUCCESS] Student '" + name + "' (Roll No: " + roll + ") added successfully.")

students = {
    "101": {
        "Name": "Aman",
        "Marks": [85, 90, 78]
    },
    "102": {
        "Name": "Riya",
        "Marks": [92, 88, 95]
    },
    "103": {
        "Name": "Karan",
        "Marks": [74, 80, 82]
    }
}

print("==================================================")
print("         STUDENT RECORDS MANAGEMENT SYSTEM        ")
print("==================================================")

while True:
    print("\nSelect an operation:")
    print("1. Display All Students")
    print("2. Add New Student")
    print("3. Search Student")
    print("4. Exit")

    choice = input("\nEnter choice (1-4): ")

    if choice == "1":
        print("\n--- All Student Records ---")
        for roll, data in students.items():
            display_student(roll, students)
        print("Total Students:", len(students))

    elif choice == "2":
        print("\n--- Add New Student ---")
        roll = input("Enter Roll Number: ")
        name = input("Enter Student Name: ")
        print("Enter marks for 3 subjects:")
        m1 = int(input("  Subject 1: "))
        m2 = int(input("  Subject 2: "))
        m3 = int(input("  Subject 3: "))
        add_student(students, roll, name, [m1, m2, m3])

    elif choice == "3":
        roll = input("Enter Roll Number to search: ")
        if students.get(roll) != None:
            print("[RECORD FOUND]")
            display_student(roll, students)
        else:
            print('[ERROR] No student found with Roll Number "' + roll + '".')

    elif choice == "4":
        print("Thank you for using the Student Records System. Goodbye!")
        break

    else:
        print("Invalid choice! Please select between 1 and 4.")