#student management system:

class old_student():
    def __init__(self,fname,lname,rollno,course):
        self.fname=fname
        self.lname=lname
        self.rollno=rollno
        self.course=course
    def display(self):
        print(f"name={self.fname + self.lname}")
        print(f"rollno={self.rollno}")
        print(f"course={self.course}")

class new_student():
    def __init__(self):
        self.students={}

    def add_student(self):
        fname=input("enter the firstname:")
        lname=input("enter the lastname:")
        rollno=input("enter the rollno:")
        course=input("enter the course:")

        student=old_student(fname,lname,rollno,course)
        self.students[0]=student

    def display_all(self):
        if not self.students:
            print("no students data")
            return
        for student in self.students.items():
            student.display()

    def run(self):
        while True:
            print("students:")
            print("1.add student")
            print("2.display student")
            print("3.exit")

            choice=input("enter the choice=")

            if choice == "1":
                self.add_student()
            elif choice=="2":
                self.display_all()
            elif choice == "3":
                print("exit")
                break
            else:
                print("invalid input")
if __name__ == "__main__":
    s=new_student()
    s.run()

