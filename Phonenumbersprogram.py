#######################################################
# Name:   Kostas Spyropoulos
# Class:   CIS-1400-NET07
# Assignment: Homework 08  Spring 2021
# File:   Homework_08.py
# Purpose: Create An Address Book Of 10 People's Names, Phone Numbers,
# & Emails Which Contains A Search Feature For The Names
#######################################################

print('\n**  Kostas Spyropoulos  **\n')  # Display author's name

# Named Constants
SIZE = 10  # Size declarator is 10 for 10 people in the address book


def main():
    # Declare names, phones, and emails arrays
    names = [0] * SIZE
    phones = [''] * SIZE
    emails = [''] * SIZE

    # For Loop for labeling each person's name, phone number, and email
    for counter in range(0, SIZE):
        # Get each person's name.
        names[counter] = str(input('Enter name #' + str(counter + 1) + ': '))

        # Get each person's number
        phones[counter] = str(input('Enter the number #' + str(counter + 1) + ': '))

        # Get each person's email
        emails[counter] = str(input('Enter the email address #' + str(counter + 1) + ': '))
        print()

    # Enter search value to search for names that match the search value
    search_value = input('Enter search value or press Enter to exit: ')
    # While loop that continues to run as long as a search value is entered
    while search_value != '':
        print('Name'.ljust(30,' '),'Phone'.ljust(30,' '), 'Email'.ljust(30,' '))
        print('----'.ljust(30,' '), '----'.ljust(30,' '), '----'.ljust(30,' '))
        counter = 0
        # While loop that searches for names of 10 people entered that
        # match the search value
        # While loop displays name, phone, and email of each person
        while counter < len(names):
            if search_value in names[counter]:
                print(names[counter].ljust(30,' '), phones[counter].ljust(30,' '), emails[counter].ljust(30,' '))
            counter = counter + 1
        # Enter search value for names after each attempted search
        print()
        search_value = input('Enter search value or press Enter to exit: ')

# Call Main procedure
main()