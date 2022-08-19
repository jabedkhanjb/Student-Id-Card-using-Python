class Student_information:
    def __init__(self, name, id, department, mobile):
        self.student_name = name
        self.student_id = id
        self.student_department = department
        self.student_mobile = mobile

    def details(self):
        print("\n")
        print("*********************************************************")
        print("*             The Millennium University                 *")
        print("*                   Student ID Card                     *")
        print("*********************************************************")
        print("*     Student name : " + self.student_name,)
        print("*     Id : " + self.student_id)
        print("*     Department : " + self.student_department)
        print("*     Cell : " + self.student_mobile)
        print("*********************************************************")
        print("\n")


student1 = Student_information(name=input("Enter your name : "), id=input("Enter your ID : "),
                               department=input("Enter your department name : "),
                               mobile=input("Enter your mobile number : +88"))
student1.details()
