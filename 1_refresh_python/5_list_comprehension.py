my_list = [0, 1, 2, 3, 4]

an_equal_list = [x for x in range(5)] # [0, 1 ,2, 3, 4]

multiply_list = [x * 3 for x in range(5)]

print(8 % 3)

print(9 % 2)

# List of a even numbers
even_numbers = [n for n in range(10) if n % 2 == 0]
print(even_numbers)

people_you_know = ["Rolf", "John", "Ana", "Greg"]
normalised_people =  [person.strip().lower() for person in people_you_know]
print(normalised_people)


## Improving the last Exercise
def who_do_you_know():
    # Ask the user for a list of people they know: John, Anna, Mary, Greg
    people = input("Enter the names of people you know, separated by commas: ")
    # Split the string into a list: ["John", "Anna", "Mary", "Greg"]
    people_list = people.split(",")
    people_without_spaces = [person.strip() for person in people_list]

    return people_without_spaces

def ask_user():
    # Ask user for a name
    person = input("Enter a name, please: ")
    # See if their name is in the list of people they know
    if person in who_do_you_know():
        print("You know {}!".format(person))
    else:
        print("You don't know {}!".format(person))
    # Print out that they know the person
    return
