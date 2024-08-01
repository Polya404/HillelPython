from exception import GroupFullError
from groups import Group
from people import Student

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
