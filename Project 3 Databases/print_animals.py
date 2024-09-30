#######################################################################################################################
#                                         Grazioso Salvare Animal Rescue System                                       #
#                                                                                                                     #
# This script defines the `print_animals` function, which is responsible for displaying information                   #
# about the available rescue animals within the Grazioso Salvare Dog and Monkey database. The function                #
# allows users to print lists of dogs, monkeys, or both, focusing on animals that are not reserved                    #
# and are in service. It provides a simple interface for users to view the current status of these                    #
# animals, including their names, acquisition countries, and training statuses.                                       #
#                                                                                                                     #
# Author: Richard VanSkike                                                                                            #
# Revision: 3.0                                                                                                       #
# Course: CS-499 Computer Science Capstone                                                                            #
# Source: Milestone 3 - Enhancement Two: Algorithms and Data Structure                                                #
# College: Southern New Hampshire University                                                                          #
#                                                                                                                     #
# Dependencies: initialize (custom module)                                                                            #
#                                                                                                                     #
# Functions:                                                                                                          #
#     print_animals(choice) - Prints information about animals based on the user's choice.                            #
#                                                                                                                     #
# Usage:                                                                                                              #
#    This script is intended to be used as part of the Rescue Animal Database application.                            #
#######################################################################################################################
from initialize import Initialize       # Import Initialize from initialize.py

def print_animals(choice):
    if choice == 1: 
        print("Listing all Dogs:\n")
        dogs = Initialize.fetch_all_dogs()  # Fetch all dogs from the database

        if not dogs:
            print("No dogs available in the system.")
        else:
            for dog in dogs:
                print(f"Name: {dog[1]}")  # Assuming dog[1] is the name column
                print(f"Breed: {dog[2]}")  # Assuming dog[2] is the breed column
                print(f"Gender: {dog[3]}")  # Assuming dog[3] is the gender column
                print(f"Age: {dog[4]}")  # Assuming dog[4] is the age column
                print(f"Weight: {dog[5]}")  # Assuming dog[5] is the weight column
                print(f"Acquisition Date: {dog[6]}")  # Assuming dog[6] is the acquisition date column
                print(f"Acquisition Country: {dog[7]}")  # Assuming dog[7] is the acquisition country column
                print(f"Training Status: {dog[8]}")  # Assuming dog[8] is the training status column
                print(f"Reserved: {'Yes' if dog[9] else 'No'}")  # Assuming dog[9] is the reserved column
                print(f"In Service Country: {dog[10]}")  # Assuming dog[10] is the in-service country column
                print("-" * 40)  # Separator line for readability

    elif choice == 2:
        print("Listing all Monkeys:\n")
        monkeys = Initialize.fetch_all_monkeys()  # Fetch all monkeys from the database

        if not monkeys:
            print("No monkeys available in the system.")
        else:
            for monkey in monkeys:
                print(f"Name: {monkey[1]}")  # Assuming monkey[1] is the name column
                print(f"Species: {monkey[2]}")  # Assuming monkey[2] is the species column
                print(f"Gender: {monkey[3]}")  # Assuming monkey[3] is the gender column
                print(f"Age: {monkey[4]}")  # Assuming monkey[4] is the age column
                print(f"Weight: {monkey[5]}")  # Assuming monkey[5] is the weight column
                print(f"Tail Length: {monkey[6]}")  # Assuming monkey[6] is the tail length column
                print(f"Height: {monkey[7]}")  # Assuming monkey[7] is the height column
                print(f"Body Length: {monkey[8]}")  # Assuming monkey[8] is the body length column
                print(f"Torso Length: {monkey[9]}")  # Assuming monkey[9] is the torso length column
                print(f"Skull Length: {monkey[10]}")  # Assuming monkey[10] is the skull length column
                print(f"Neck Length: {monkey[11]}")  # Assuming monkey[11] is the neck length column
                print(f"Acquisition Date: {monkey[12]}")  # Assuming monkey[12] is the acquisition date column
                print(f"Acquisition Country: {monkey[13]}")  # Assuming monkey[13] is the acquisition country column
                print(f"Training Status: {monkey[14]}")  # Assuming monkey[14] is the training status column
                print(f"Reserved: {'Yes' if monkey[15] else 'No'}")  # Assuming monkey[15] is the reserved column
                print(f"In Service Country: {monkey[16]}")  # Assuming monkey[16] is the in-service country column
                print("-" * 40)  # Separator line for readability

    elif choice == 3:
        print("Listing all unreserved animals:\n")
        dogs = Initialize.fetch_all_dogs()  # Fetch all dogs from the database
        monkeys = Initialize.fetch_all_monkeys()  # Fetch all monkeys from the database

        unreserved_dogs = [dog for dog in dogs if not dog[9]]  # Filter unreserved dogs (assuming dog[9] is the reserved column)
        unreserved_monkeys = [monkey for monkey in monkeys if not monkey[15]]  # Filter unreserved monkeys (assuming monkey[15] is the reserved column)

        if not unreserved_dogs and not unreserved_monkeys:
            print("No unreserved animals available in the system.")
        else:
            if unreserved_dogs:
                print("Unreserved Dogs:\n")
                for dog in unreserved_dogs:
                    print(f"Name: {dog[1]}")
                    print(f"Breed: {dog[2]}")
                    print(f"Gender: {dog[3]}")
                    print(f"Age: {dog[4]}")
                    print(f"Weight: {dog[5]}")
                    print(f"Acquisition Date: {dog[6]}")
                    print(f"Acquisition Country: {dog[7]}")
                    print(f"Training Status: {dog[8]}")
                    print(f"In Service Country: {dog[10]}")
                    print("-" * 40)  # Separator line for readability

            if unreserved_monkeys:
                print("Unreserved Monkeys:\n")
                for monkey in unreserved_monkeys:
                    print(f"Name: {monkey[1]}")
                    print(f"Species: {monkey[2]}")
                    print(f"Gender: {monkey[3]}")
                    print(f"Age: {monkey[4]}")
                    print(f"Weight: {monkey[5]}")
                    print(f"Tail Length: {monkey[6]}")
                    print(f"Height: {monkey[7]}")
                    print(f"Body Length: {monkey[8]}")
                    print(f"Torso Length: {monkey[9]}")
                    print(f"Skull Length: {monkey[10]}")
                    print(f"Neck Length: {monkey[11]}")
                    print(f"Acquisition Date: {monkey[12]}")
                    print(f"Acquisition Country: {monkey[13]}")
                    print(f"Training Status: {monkey[14]}")
                    print(f"In Service Country: {monkey[16]}")
                    print("-" * 40)  # Separator line for readability