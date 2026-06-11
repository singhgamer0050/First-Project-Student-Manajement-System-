class Student:
    def __init__(self, name, roll_no, branch, marks):
        self.name = name
        self.roll_no = roll_no
        self.branch = branch
        self.marks = marks

    def view_stu(self):
        print("Student details:")
        print("Student name =",self.name )
        print("Student roll no. =",self.roll_no )
        print("Student branch =",self.branch )
        print("Student marks =",self.marks )

students =[]
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
        stu1 = Student(name, roll_no, branch, marks)
        students.append(stu1)
        print("Student added successfully!")
        print("-" * 20)
    elif menu == 2:
        if len(students) == 0:
            print("No students found!")
        else:
            for student in students:
                print("-" * 20)
                student.view_stu()
                print("-" * 20)
            print("Total student",len(students))
            print("-" * 20)

    elif menu == 3:
        try:
            roll = int(input("Enter roll number of student to search: "))    
        except ValueError:
            print("Invalid Input")
            print("-" * 20)
            continue
        found = False
        for stu in students:
            if(stu.roll_no == roll):
                stu.view_stu()
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
        for stu in students:
            if(stu.roll_no == roll):
                students.remove(stu)
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
        for stu in students:
            if (stu.roll_no == roll):
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
                stu.name = name
                stu.roll_no = roll_no
                stu.branch = branch
                stu.marks = marks
                print("Student Updated successfully!")
                print("-" * 20)
                found = True
                break
        if found == False:
            print("Student not exist")  
    elif menu == 6:
        print("Thankyou")
        break
    else:
        print("Invalid choice")