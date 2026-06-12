import json
try:
    with open ("stu.json","r") as f:
        data = json.load(f)
except (FileNotFoundError, json.JSONDecodeError):
    data = []
def save_data():
    with open("stu.json", "w") as f:
        json.dump(students, f, indent=2)

students = data
while True:
    try:
        menu = int(input(
        "1. Add Student\n"
        "2. View Student\n"
        "3. Search Student\n"
        "4. Delete Student\n"
        "5. Update Student\n"
        "6. Exit\n"
        "Enter your choice: "
        ))
    except ValueError:
        print("Invalid Input")
        print("-" * 20)
        continue
    if menu == 1:
        name = input("Enter your name:")
        found = False
        try:
            roll_no = int(input("Enter your roll number:")) 
            found = False
            for student in students:
                if student["roll_no"] == roll_no:
                    print("Roll number already exists")
                    found = True
                    break
            if found == True:
                continue
        except ValueError:
            print("Invalid Input")
            print("-" * 20)
            continue
        branch = input("Enter your Branch:")
        try:
            marks = int(input("Enter your marks:"))
        except ValueError:
            print("Invalid Input")
            print("-" * 20)
            continue
        print("-" * 20)
        stu={"name" : name,
             "roll_no" : roll_no,
             "branch" : branch,
             "marks" : marks}
        students.append(stu)
        print("Student added successfully!")
        print("-" * 20)
        save_data()
    elif menu == 2:
        if len(students) == 0:
            print("No students found!")
        else:
            for student in students:
                print("-" * 20)
                print("Name:", student["name"])
                print("Roll No:", student["roll_no"])
                print("Branch:", student["branch"])
                print("Marks:", student["marks"])
                print("-" * 20)
            print("Total students:", len(students))

    elif menu == 3:
        try:
            roll = int(input("Enter roll number of student to search: "))    
        except ValueError:
            print("Invalid Input")
            print("-" * 20)
            continue
        found = False
        for student in students:
            if(student["roll_no"] == roll):
                print(student)
                print("-" * 20)
                found = True
                break
        if found == False:
            print("Student not found")
    elif menu == 4:
        try:
            roll = int(input("Enter roll number of student to delete: "))
        except ValueError:
            print("Invalid Input")
            print("-" * 20)
            continue
        found = False
        for student in students:
            if(student["roll_no"] == roll):
                students.remove(student)
                save_data()
                print("Student deleted successfully!")
                print("-" * 20)
                found = True
                break    
        if found == False:
            print("Not a valid roll number for any student")
    elif menu == 5:
        try:
            roll = int(input("Enter roll number of student to Update: "))    
        except ValueError:
            print("Invalid Input")
            print("-" * 20)
            continue
        found = False
        for student in students:
            if (student["roll_no"] == roll):
                name = input("Enter your name:")
                try:
                    roll_no = int(input("Enter your roll number:"))    
                except ValueError:
                    print("Invalid Input")
                    print("-" * 20)
                    continue
                branch = input("Enter your Branch:")
                try:
                    marks = int(input("Enter your marks:"))
                except ValueError:
                    print("Invalid Input")
                    print("-" * 20)
                    continue
                print("-" * 20)
                student["name"] = name
                student["roll_no"] = roll_no
                student["branch"] = branch
                student["marks"] = marks
                print("Student Updated successfully!")
                print("-" * 20)
                save_data()
                found = True
                break
        if found == False:
            print("Student not exist")  
    elif menu == 6:
        print("Thankyou")
        break
    else:
        print("Invalid choice")