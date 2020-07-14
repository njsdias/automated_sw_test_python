my_variable = "hello"

print("Print first character: ", my_variable[0])

# Print each character of a string using an iteration
# strings, lists, sets, tuples, and more
for character in my_variable:
    print(character)


my_num_list = [1, 3, 5, 7, 9]

for number in my_num_list:
    print(number ** 2)

user_wants_number = True
while user_wants_number == True:
    print(10)
    # user_wants_number = False
    user_input = input("Should we print again? (y/n)")
    if user_input == 'n':
        user_wants_number = False
