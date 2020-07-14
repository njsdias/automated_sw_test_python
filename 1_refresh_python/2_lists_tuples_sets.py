my_variable = "hello"

grade_one = 77
grade_two = 80
grade_three= 90

# print((grade_one + grade_two + grade_three)/3)

# It is not sustentable because we can have thousands of grades examples

# we can store our grades in a list
grades = [77, 80, 95, 100, 105, 107]
grades.append(108)  #adding new element in a list
print(sum(grades)/ len(grades))

# A tuple is inmutable (different than a list)
# We dont ave ways to increase the size of a tuple
tuple_grades = (77, 80, 95, 100, 105, 107)
# to add alues we need to modify all tupple
tuple_grades = tuple_grades + (100,)
# print(tuple_grades)

# Set: it is a collection of unique & unorder values
set_grades = {77, 80, 90, 100, 100}
# print(set_grades) #to confirm the unique & unorder output

##
# Slicing in lists. We are not able to do this in tuples
print(grades[0])
grades[0] = 60
print(grades)

# Slicing is not appropriated for:
# tuples: We cannnot modify mvalues in tupples because they are inmutable
# sets: they are unorder, so they don't have positions
set_grades.add(60)

## Set operations
your_lottery_numbers = {1, 2, 3, 4, 5}
winning_number = {1, 3, 5, 7, 9, 11}

print(your_lottery_numbers.intersection(winning_number))
print(your_lottery_numbers.union(winning_number))
print(your_lottery_numbers.difference(winning_number))
