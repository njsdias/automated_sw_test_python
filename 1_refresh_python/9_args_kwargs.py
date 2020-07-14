import os

os.system("clear")


def my_method(arg1, arg2):
    return arg1 + arg2

def my_long_method(arg1, arg2, arg3, arg4, arg5, arg6):
    return arg1 + arg2 + arg3 + arg4 + arg5 + arg6

def my_list_addition(list_arg):
    return sum(list_arg)

my_long_method(3, 4, 15, 26, 35, 49)

my_list_addition([3, 4, 15, 26, 35, 49])

# We can use *args to pass a list of arguments
def addition_simplified(*args):
    return sum(args)

addition_simplified(3, 4, 15, 26, 35, 49)

## kwargs

def what_are_kwargs(*args, **kwargs):
    print(args)   #tuple
    print(kwargs) #set

# what_are_kwargs(2, 4, 5, name='Jose', location='UK')

def what_are_kwargs_v2(*args, name, location):
    print(args)   #tuple
    print(name, location)

# what_are_kwargs_v2(2, 4, 5, name='Jose', location='UK')

def what_are_kwargs_v3(arg1, name, location):
    print(arg1)   #tuple
    print(name, location)

what_are_kwargs_v2(2, location='UK', name='Jose') # the parameter order does't matter


## Improving Student Class
class Student():
    """docstring fs Student."""

    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks)/len(self.marks)

    @classmethod # to allow me use friend with Working Student
    # def friend(cls, origin, friend_name, *args):
    # def friend(cls, origin, friend_name, **kwargs):
    def friend(cls, origin, friend_name, *args, **kwargs):
        # but in this case we need origin method
        # return a new Student called "friend_name" in the same school as self.

        # return cls(friend_name, origin.school, *args)
        return cls(friend_name, origin.school, *args, **kwargs)

## Inheritance
class WorkingStudent(Student):
    def __init__(self, name, school, salary, job_title):
        # we are now call the call init methof from class Student
        # for this we use the super method
        super().__init__(name, school)
        self.salary = salary
        self.job_title = job_title

    def salary_average(self):
        return sum(self.salary)/len(self.salary)

# anna = WorkingStudent("Anna", "Oxford", 20.0, "Team Leader")
# anna = WorkingStudent("Anna", "Oxford", salary= 20.0, job_title="Software Developer")
# anna = WorkingStudent("Anna", "Oxford", salary= 20.0, job_title="Software Developer")
anna = WorkingStudent("Anna", "Oxford", [20.0], "Software Developer")
print('Name: {} \n'.format(anna.name),
    'School: {} \n'.format(anna.school),
    'Salary: {} \n'.format(anna.salary),
    'Salary Average: {}:'.format(anna.salary_average()))

# friend = WorkingStudent.friend(anna, "Greg", 15.50, "Software Developer")
# friend = WorkingStudent.friend(anna, "Greg", salary=15.50, job_title="Software Developer")
friend = WorkingStudent.friend(anna, "Greg", [15.50, 20.0], "Software Developer")
print('Name: {} \n'.format(friend.name),
    'School: {} \n'.format(friend.school),
    'Salary: {} \n'.format(friend.salary),
    'Salary Average: {}:'.format(friend.salary_average()))
