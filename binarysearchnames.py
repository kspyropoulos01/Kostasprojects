#######################################################
# Name:   Kostas Spyropoulos
# Class:   CIS-1400-NET07
# Assignment: Homework 09  Spring 2021
# File:   Homework_09.py
# Purpose: Enters 20 names and assorts them into ascending alphabetical order
# and has a binary search feature
#######################################################

print('\n**  Kostas Spyropoulos  **\n')  # Display author's name

# Named Constants
SIZE = 20  # Size declarator is 20 for 20 names to be entered


def main():
    # names array has a size declarator of 20
    names = [0] * SIZE

    # Enter the twenty names of the array
    print('Please enter twenty names')
    for i in range(0, SIZE):
        names[i] = str(input(str(i + 1) + ':'))

    # Displays 'The sorted names are:'
    print()
    print('The sorted names are:')
    print()

    # Set max_element to length of names array - 1
    max_element = len(names) - 1

    # While loop that arranges names into ascending alphabetical order
    while max_element >= 0:
        # Set i to 0
        i = 0
        # While loop compares every element with its neighboring element
        while i <= max_element - 1:
            # Switch the two elements
            if names[i] > names[i + 1]:
                temp = names[i]
                names[i] = names[i + 1]
                names[i + 1] = temp
            # Increase i by 1 incrementally
            i = i + 1
        # Decrease max_element by 1 decrementally
        max_element = max_element - 1

    # Displays all 20 names in ascending alphabetical order
    for i in range(0, SIZE):
        print(names[i])

    # Binary search for the 20 names
    # Ask user for search_value for binary search
    print()
    search_value = input('Enter name to search for <or Enter to exit>:')
    # While loop executes as long as search_value is not blank
    while search_value != '':
        first = 0
        last = len(names) - 1
        found = False
        searches = 1
        # Search for the search_value
        while not found and first <= last:
            # Calculate mid point
            middle = int((first + last) / 2)
            # If search_value is found at mid point display Name, Position, and
            # array lookups
            if names[middle] == search_value:
                found = True
                # Display Name, Position, array lookups if value is found
                print()
                print('Name Found:', names[middle])
                print('Position:', middle)
                print('array lookups:', searches)
            # Else if search_value is in lower half decrease last
            # decrementally
            elif names[middle] > search_value:
                last = middle - 1
            # Else if search_value is in upper half increase first
            # incrementally
            else:
                first = middle + 1
            # Count number of array lookups
            searches = searches + 1
        # If search_value is not found display 'Name not found',
        # 'array lookups: -1'
        if not found:
            print()
            print('Name not found')
            print('array lookups: -1')
        # Ask user for another search_value and user has the option to stop
        # searching
        print()
        search_value = input('Enter name to search for <or Enter to exit>:')

# Call main procedure
main()
