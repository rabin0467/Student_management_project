class Student:
    def __init__(self, id, name, department):
        self.__id = id
        self.__name = name
        self._department = department
        self.is_enrolled = False
        
    def get_id(self):
        return self.__id
        
    def get_name(self):
        return  self.__name

    def get_depart(self):
        return self._department
        
class StudentDataBase:
    student_list = []

    def __init__(self, name):
        self.name = name
    
    @classmethod
    def add_student(cls, id, name, department):
        student = Student(id, name, department)
        cls.student_list.append(student)
        student.is_enrolled = True
        
    @classmethod
    def enroll_student( cls, id, name, department):
        for student in cls.student_list:
            if student.get_id() == id:
                print(f'Student {student.get_id()} is already enrolled')
                return
        cls.add_student( id, name, department)
        print(f'Student {id} enrolled succesfully')
        student.is_enrolled = True
    @classmethod
    def drop_student(cls, id):
        for student in cls.student_list:
            if student.get_id() == id:
                print(f'This Student {id}, dropped succesfully')
                student.is_enrolled = False
                return     
        print(f'Student with this id: {id} has not enrolled yet')

    def view_student_info():
        for student in StudentDataBase.student_list:
            print(f'ID: {student.get_id()}, Name: {student.get_name()}, Department: {student.get_depart()}, Enrolled: {student.is_enrolled}')


first = StudentDataBase('Alice Smith')
first.add_student('S101', 'Alice Smith', 'computer science')
second = StudentDataBase('Bob Johnson')
second.add_student('S102', 'Bob Johnson', 'Mathematics')
third = StudentDataBase('Charlie Lee')
third.add_student('S103', 'Charlie Lee', 'Physics')

# replica system:
start = True
while start != False:
    print('---Student Management Menu---')
    print('1. View All Student')
    print('2. Enroll Student')
    print('3. Drop Student')
    print('4. Exit')
    option = int(input('Enter your choice(1-4):'))
    if option == 1:
        StudentDataBase.view_student_info()
    elif option == 2:
        id = input('Enter your ID:')
        name = input('Enter your name:')
        depart = input('Enter your department:')
        StudentDataBase.enroll_student( id, name, depart)
    
    elif option == 3:
        id = input('Enter students id: ')
        StudentDataBase.drop_student(id)
    elif option == 4:
        start = False
    else:
        print('Enter a valid number.')
