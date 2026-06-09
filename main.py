student =[]
class student:
    def __init__(self, name, roll_no, branch, marks):
        self.name = name
        self.roll_no = roll_no
        self.branch = branch
        self.marks = marks

    def view_stu(self):
        print("Student name =",self.name )
        print("Student roll no. =",self.roll_no )
        print("Student branch =",self.branch )
        print("Student marks =",self.marks )

stu1 = student("Aman",12,"CSE(AI)",90)
stu1.view_stu()