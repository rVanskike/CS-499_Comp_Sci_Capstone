#########################################################################################################################
#                                         Grazioso Salvare Animal Rescue System                                         #
#                                                                                                                       #
# This script serves as the main driver for the Grazioso Salvare Dog and Monkey database project. It initializes        #
# the application, handles user interaction through a menu-driven interface, and processes user commands to manage      #
# the intake, reservation, and display of animals in the database.                                                      #
#                                                                                                                       #
# Author: Richard VanSkike                                                                                              #
# Revision: 1.0                                                                                                         #
# Course: CS-499 Computer Science Capstone                                                                              #
# Source: IT-145 Foundation in Application Development                                                                  #
# College: Southern New Hampshire University                                                                            #
#                                                                                                                       #
# Dependencies: typing, dog (custom module), monkey (custom module), intake (custom module), initialize (custom module),#
#       print_animals (custom module), reserve_animal (custom module)                                                   #
#                                                                                                                       #
# Class:                                                                                                                #
#     Driver - Contains the main logic for the program, including the initialization of animal lists and the            #
#              user interface loop that allows users to intake new animals, reserve animals, and print lists of         #
#              animals based on different criteria.                                                                     #
#                                                                                                                       #
# Methods:                                                                                                              #
#     main() - The main entry point of the application that initializes data, displays the menu, and processes user     #
#             input to perform various operations on the dog and monkey lists.                                          #
#     display_menu() - Displays the main menu to the user, offering options for various operations on the animals.      #
#                                                                                                                       #
# Usage:                                                                                                                #
#     Run this script as the main entry point to start the Grazioso Salvare Animal Rescue System.                       #
#########################################################################################################################
from typing import List         # Import List object from typing library
from dog import Dog             # Import the Dog class from dog.py
from monkey import Monkey       # Import the Monkey class from monkey.py
import intake                   # Import the intake methods
import initialize               # Import the initialize methods
import print_animals            # Import the print_animals method
import reserve_animal           # Import the reserve_animal method

class Driver:
    dog_list: List['Dog'] = []          # Creating list for Dog
    monkey_list: List['Monkey'] = []    # Creating list for Monkey

    @staticmethod
    def main():
        scnr = input                                            # Using input() for user input
        initialize.initialize_dog_list(Driver.dog_list)         # Initialize and load dog_list
        initialize.initialize_monkey_list(Driver.monkey_list)   # Initialize and load monkey_list
        usr_input = ""                                          # Instantiating usrInput

        while usr_input != "q":     # While loop that will keep menu displayed until user presses "q"
            Driver.display_menu()   # Display user menu with options.
            usr_input = scnr()      # Set usr_input to scanner to capture user keystrokes.

            if usr_input == "1":                            # If user inputs 1, it will invoke the intake_new_dog method.
                print("Beginning Dog Intake")
                intake.intake_new_dog(Driver.dog_list)      # Use intake.intake_new_dog to add a new dog to the database.

            elif usr_input == "2":                              # If user inputs 2, it will invoke the intake_new_monkey method.
                print("Beginning Monkey Intake")
                intake.intake_new_monkey(Driver.monkey_list)    # Use intake.intake_new_monkey to add a new monkey to the database.

            elif usr_input == "3":                                                  # If user inputs 3, it will invoke the reserve_animal method.
                print("Beginning Animal Reservation")
                reserve_animal.reserve_animal(Driver.dog_list, Driver.monkey_list)  # Use reserve_animal.reserve_animal to search for and reserve an animal.

            elif usr_input == "4":                                                  # If user inputs 4, 5, or 6 it will invoke the print_animals method.
                print("Displaying List of dogs")
                print_animals.print_animals(1, Driver.dog_list, Driver.monkey_list) # Use print_animals.print_animals to display all dogs.

            elif usr_input == "5":
                print("Displaying List of monkeys")
                print_animals.print_animals(2, Driver.dog_list, Driver.monkey_list) # Use print_animals.print_animals to display all monkeys.

            elif usr_input == "6":
                print("Displaying List of unreserved animals")
                print_animals.print_animals(3, Driver.dog_list, Driver.monkey_list) # Use print_animals.print_animals to display all unreserved dogs and monkeys.

            elif usr_input == "q":      # If user inputs "q" it will quit the loop and exit the program.
                print("Quitting.")

            else:                       # If user inputs any other char it will respond invalid command and request a new input.
                print("Invalid command.")

    # Method to build the initial menu when program starts.
    @staticmethod
    def display_menu():
        print("\n\n")
        print("\t\t\t\tRescue Animal System Menu")
        print("[1] Intake a new dog")
        print("[2] Intake a new monkey")
        print("[3] Reserve an animal")
        print("[4] Print a list of all dogs")
        print("[5] Print a list of all monkeys")
        print("[6] Print a list of all animals that are not reserved")
        print("[q] Quit application")
        print()
        print("Enter a menu selection")

if __name__ == "__main__":
    Driver.main()
