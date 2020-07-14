class Student():
    """docstring fs Student."""

    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks)/len(self.marks)

    def friend(self, friend_name):
        # return a new Student called "friend_name" in the same school as self.
        return Student(friend_name, self.school)

    @classmethod # to allow me use friend with Working Student
    def friend_v2(cls, origin, friend_name, salary):
        # but in this case we need origin method
        # return a new Student called "friend_name" in the same school as self.
        return cls(friend_name, origin.school, salary)


anna = Student("Anna", "Oxford")

friend = anna.friend("Greg")
print(friend.name)
print(friend.school)
print(friend.school == anna.school)

## Inheritance
class WorkingStudent(Student):
    def __init__(self, name, school, salary):
        # we are now call the call init methof from class Student
        # for this we use the super method
        super().__init__(name, school)
        self.salary = salary

anna = WorkingStudent("Anna", "Oxford", 20.00)
print(anna.salary)

friend_v2 = WorkingStudent.friend_v2(anna, "Greg", 15.60)
print(friend_v2.name)
print(friend_v2.school)
