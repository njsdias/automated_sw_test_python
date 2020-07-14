# classmethod and staticmethod

## Student Class
class Student(object):
    """docstring for Student."""

    def __init__(self, name, school):
        super(Student, self).__init__()
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    @classmethod #this avoid the need to use self and we don't have errors
    def go_to_scholl(cls): # cls means we are pass the class itself and not the self
        # print("I'm going to {}".formart(self.scholl))
        print("I'm going to scholl!")
        print("I'm a {}".format(cls))

    @staticmethod #this avoid the need to pass the class and the self
    def go_to_scholl_v2():
        print("I'm going to scholl.")


anna = Student("Anna", "MIT")
ramon = Student("Ramon", "Oxford")


anna.marks.append(56)
anna.marks.append(71)
print(anna.marks)
print(anna.average())
anna.go_to_scholl()
anna.go_to_scholl_v2()
Student.go_to_scholl_v2() # we don't have self so we don't care who is calling
                          # the method go_to_scholl_v2
