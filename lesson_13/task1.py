class GroupFullError(Exception):
    def __init__(self, message="Cannot add more than 10 students to the group."):
        self.message = message
        super().__init__(self.message)


class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.gender}, {self.age} years old"


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"{super().__str__()}, Record Book: {self.record_book}"


class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            raise GroupFullError()
        self.group.add(student)

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            self.group.remove(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
        return None

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group)
        return f'Number: {self.number}\nStudents:\n{all_students}'


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Male', 22, 'John', 'Doe', 'AN146')
st4 = Student('Female', 23, 'Jane', 'Smith', 'AN147')
st5 = Student('Male', 21, 'Peter', 'Parker', 'AN148')
st6 = Student('Female', 22, 'Mary', 'Jane', 'AN149')
st7 = Student('Male', 24, 'Bruce', 'Wayne', 'AN150')
st8 = Student('Female', 26, 'Diana', 'Prince', 'AN151')
st9 = Student('Male', 25, 'Clark', 'Kent', 'AN152')
st10 = Student('Female', 28, 'Lois', 'Lane', 'AN153')
st11 = Student('Male', 27, 'Tony', 'Stark', 'AN154')

gr = Group('PD1')
students = [st1, st2, st3, st4, st5, st6, st7, st8, st9, st10, st11]

for stdt in students:
    try:
        gr.add_student(stdt)
    except GroupFullError as e:
        print(f"Error: {e}")

print(gr)
