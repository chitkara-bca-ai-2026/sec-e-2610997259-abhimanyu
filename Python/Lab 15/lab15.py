students = {
    "101": {
        "Name": "Aman",
        "Branch": "BCA AI",
        "Semester": "1",
        "Marks": [85, 90, 78]
    },
    "102": {
        "Name": "Riya",
        "Branch": "BCA AI",
        "Semester": "1",
        "Marks": [92, 88, 95]
    },
    "103": {
        "Name": "Karan",
        "Branch": "BCA AI",
        "Semester": "1",
        "Marks": [74, 80, 82]
    }
}

print("==================================================")
print("       STUDENT INFORMATION MANAGEMENT SYSTEM      ")
print("==================================================")

while True:
    print("\nSelect an operation:")
    print("1. View All Students")
    print("2. Search Student by Roll Number")
    print("3. Register New Student")
    print("4. Update Student Details")
    print("5. View Academic Performance")
    print("6. Delete Student Record")
    print("7. Exit")

    choice = input("\nEnter your choice (1-7): ")

    if choice == "1":
        print("\n--- Enrolled Student Records ---")
        for roll, info in students.items():
            print("Roll No:", roll, "| Name:", info["Name"], "| Branch:", info["Branch"], "| Sem:", info["Semester"], "| Marks:", info["Marks"])
        print("Total Enrolled Students:", len(students))

    elif choice == "2":
        roll = input("Enter Roll Number to search: ")
        student = students.get(roll)
        if student != None:
            print("\n[FOUND] Record for Roll No " + roll + ":")
            print("Name    :", student["Name"])
            print("Branch  :", student["Branch"])
            print("Semester:", student["Semester"])
            print("Marks   :", student["Marks"])
        else:
            print("\n[ERROR] No student found with Roll No " + roll + ".")

    elif choice == "3":
        print("\n--- Register New Student ---")
        roll = input("Enter Roll Number: ")
        if roll in students:
            print("[ERROR] Roll Number already exists!")
        else:
            name = input("Enter Student Name: ")
            branch = input("Enter Branch (e.g. BCA AI): ")
            sem = input("Enter Semester: ")
            print("Enter marks obtained in 3 subjects:")
            m1 = int(input("  Subject 1: "))
            m2 = int(input("  Subject 2: "))
            m3 = int(input("  Subject 3: "))

            students[roll] = {
                "Name": name,
                "Branch": branch,
                "Semester": sem,
                "Marks": [m1, m2, m3]
            }
            print("\n[SUCCESS] Student '" + name + "' (Roll No: " + roll + ") registered successfully.")

    elif choice == "4":
        roll = input("Enter Roll Number to update: ")
        if roll in students:
            print("Current details for " + students[roll]["Name"] + " (Roll " + roll + "):")
            print("1. Branch:", students[roll]["Branch"], "| 2. Semester:", students[roll]["Semester"])
            opt = input("Choose field to update (1 for Branch, 2 for Semester): ")
            if opt == "1":
                new_branch = input("Enter new branch: ")
                students[roll]["Branch"] = new_branch
                print("[SUCCESS] Branch updated to '" + new_branch + "'.")
            elif opt == "2":
                new_sem = input("Enter new semester: ")
                students[roll]["Semester"] = new_sem
                print("[SUCCESS] Semester updated to '" + new_sem + "'.")
            else:
                print("[ERROR] Invalid option.")
        else:
            print("[ERROR] Student not found.")

    elif choice == "5":
        roll = input("Enter Roll Number for Academic Performance: ")
        student = students.get(roll)
        if student != None:
            marks = student["Marks"]
            total = sum(marks)
            average = total / len(marks)
            if average >= 40:
                status = "PASS"
            else:
                status = "FAIL"

            print("\n================ ACADEMIC REPORT ================")
            print("Student Name :", student["Name"], "(Roll:", roll + ")")
            print("Subject Marks:", marks)
            print("Total Marks  :", total, "/ 300")
            print("Average Marks:", str(round(average, 2)) + "%")
            print("Final Result :", status)
            print("=================================================")
        else:
            print("[ERROR] Student not found.")

    elif choice == "6":
        roll = input("Enter Roll Number to delete: ")
        removed = students.pop(roll, None)
        if removed != None:
            print("\n[SUCCESS] Record for '" + removed["Name"] + "' (Roll No: " + roll + ") deleted successfully.")
        else:
            print("\n[ERROR] Student not found.")

    elif choice == "7":
        print("\nThank you for using Student Information System. Goodbye!")
        break

    else:
        print("\nInvalid choice! Please enter a number from 1 to 7.")