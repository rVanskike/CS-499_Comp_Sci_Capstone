#########################################################################################################################
#                                         Grazioso Salvare Animal Rescue System                                         #
#                                                                                                                       #
# This script defines the `print_animals` function, which is responsible for displaying information                     #
# about the available rescue animals within the Grazioso Salvare Dog and Monkey database. The function                  #
# allows users to print lists of dogs, monkeys, or both, focusing on animals that are not reserved                      #
# and are in service. It provides a simple interface for users to view the current status of these                      #
# animals, including their names, acquisition countries, and training statuses.                                         #
#                                                                                                                       #
# Author: Richard VanSkike                                                                                              #
# Revision: 1.0                                                                                                         #
# Course: CS-499 Computer Science Capstone                                                                              #
# Source: IT-145 Foundation in Application Development                                                                  #
# College: Southern New Hampshire University                                                                            #
#                                                                                                                       #
# Methods:                                                                                                              #
#     print_animals(choice, dog_list, monkey_list) - Prints details of available dogs and monkeys                       #
#                                                   based on the user's selection.                                      #
#                                                                                                                       #
# Usage:                                                                                                                #
#    Call the print_animals function with the appropriate choice (1 for dogs, 2 for monkeys, 3 for both)                #
#    and provide the lists of dogs and monkeys to view their availability and status.                                   #
#########################################################################################################################
# Method to print all animals based off user selection
def print_animals(choice, dog_list, monkey_list):
    if choice == 1:
        print("Listing all Dogs:\n")
        if not dog_list:
            print("No dogs available in the system.") # If no dogs are found in the database, say so.
        else:
            for dog in dog_list: # If dogs are found, iterate through the database and print the items with their corresponding information.
                print(f"Name: {dog.name}")
                print(f"Breed: {dog.breed}")
                print(f"Gender: {dog.gender}")
                print(f"Age: {dog.age}")
                print(f"Weight: {dog.weight}")
                print(f"Acquisition Date: {dog.acquisition_date}")
                print(f"Acquisition Country: {dog.acquisition_country}")
                print(f"Training Status: {dog.training_status}")
                print(f"Reserved: {'Yes' if dog.reserved else 'No'}")
                print(f"In Service Country: {dog.in_service_country}")
                print("-" * 40)  # Separator line for readability.

    elif choice == 2:
        print("Listing all Monkeys:\n")
        if not monkey_list:
            print("No monkeys available in the system.") # If no monkeys are found in the databse, say so.
        else:
            for monkey in monkey_list: # If monkeys are found, iterate through the database and print the items with their corresponding information.
                print(f"Name: {monkey.name}")
                print(f"Species: {monkey.species}")
                print(f"Gender: {monkey.gender}")
                print(f"Age: {monkey.age}")
                print(f"Weight: {monkey.weight}")
                print(f"Tail Length: {monkey.tail_length}")
                print(f"Height: {monkey.height}")
                print(f"Body Length: {monkey.body_length}")
                print(f"Torso Length: {monkey.torso_length}")
                print(f"Skull Length: {monkey.skull_length}")
                print(f"Neck Length: {monkey.neck_length}")
                print(f"Acquisition Date: {monkey.acquisition_date}")
                print(f"Acquisition Country: {monkey.acquisition_country}")
                print(f"Training Status: {monkey.training_status}")
                print(f"Reserved: {'Yes' if monkey.reserved else 'No'}")
                print(f"In Service Country: {monkey.in_service_country}")
                print("-" * 40)  # Separator line for readability.

    elif choice == 3:
        print("Getting Available Dogs:\n")
        for dog in dog_list: # Iterate through the dog_list.
            if not dog.reserved and dog.training_status and dog.training_status.lower() == "in service": # Dog must not be reserved and must be in service, if found print information.
                print(f"The dog: {dog.name} is available.")
                print(f"{dog.name} is from: {dog.acquisition_country}")
                print(f"{dog.name}'s current status is: {dog.training_status}")
                print("-" * 40)  # Separator line for readability.

        print("Getting Available Monkeys:\n")
        for monkey in monkey_list: # Iterate through the monkey_list.
            if not monkey.reserved and monkey.training_status and monkey.training_status.lower() == "in service": # Dog must not be reserved and must be in service, if found print information.
                print(f"The Monkey: {monkey.name} is available.")
                print(f"{monkey.name} is from: {monkey.acquisition_country}")
                print(f"{monkey.name}'s current status is: {monkey.training_status}")
                print("-" * 40)  # Separator line for readability.
