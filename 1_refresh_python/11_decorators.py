# Decorators: it is a function that's just call before another function
import functools
import os

os.system("clear")

def my_decorator(func):
    @functools.wraps(func)
    def function_that_runs_func():
        print("In the decorator!")
        func()
        print("After decorator!")
    return function_that_runs_func

# Apply my_decorator to my_function
@my_decorator
# Pass my_function to th decorator as func
def my_function():
    print("I'm the function!")

# Now my_function was transformed in function_that_runs_func
# because this function is inside of decorator.
# At the end we are extending the func()

my_function()


## More Complex Decorators: It's accept arguments itself

def decorator_with_arguments(number):
    def my_decorator(func):
        # Wraps tell us the below function will be subsitute by new one
        @functools.wraps(func)
        def function_that_runs_func(*args, **kwargs):
            print("In the decorator_2!")
            if number == 56:
                print("Not running the function!")
            else:
                func(*args, **kwargs)
            print("After decorator_2!")
        return function_that_runs_func
    return my_decorator

@decorator_with_arguments(57)
def my_function_two(x, y):
    #print("Hello")
    print(x + y)
my_function_two(57, 67)

# It can be usefull when we ar developing a website when we need to pass
# the users permissions as arguments. If the user is not an admin it doesn't
# shows the admin page

# Insert elements in the database if they matches of criteria
