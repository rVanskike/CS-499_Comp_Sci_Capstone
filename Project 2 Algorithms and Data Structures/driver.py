########################################################################################################################
#                                         Grazioso Salvare Animal Rescue System                                        #
#                                                                                                                      #
# This script serves as the main driver for the Grazioso Salvare Dog and Monkey database project. It initializes       #
# the application, handles user interaction through a menu-driven interface, and processes user commands to manage     #
# the intake, reservation, and display of animals in the database.                                                     #
#                                                                                                                      #
# Author: Richard VanSkike                                                                                             #
# Revision: 2.0                                                                                                        #
# Course: CS-499 Computer Science Capstone                                                                             #
# Source: Milestone 2 - Enhancement One: Software Design and Engineering                                               #
# College: Southern New Hampshire University                                                                           #
#                                                                                                                      #
# Dependencies: typing, dog (custom module), monkey (custom module), reserve_animal (custom module),                   #
#       intake (custom module), initialize (custom module), print_animals (custom module), search (custom module)      #
#                                                                                                                      #
# Class:                                                                                                               #
#     Driver - Contains the main logic for the program, including the initialization of animal dictionaries and the    #
#              user interface loop that allows users to intake new animals, reserve animals, and print lists of        #
#              animals based on different criteria.                                                                    #
#                                                                                                                      #
# Methods:                                                                                                             #
#     main() - The main entry point of the application that initializes data, displays the menu, and processes user    #
#             input to perform various operations on the dog and monkey dictionaries.                                  #
#     display_menu() - Displays the main menu to the user, offering options for various operations on the animals.     #
#                                                                                                                      #
# Usage:                                                                                                               #
#     Run this script as the main entry point to start the Grazioso Salvare Animal Rescue System.                      #
########################################################################################################################
from typing import Dict                     # Import Dictionary object from typing library
from dog import Dog                         # Import the Dog class from dog.py
from monkey import Monkey                   # Import the Monkey class from monkey.py
from reserve_animal import ReserveAnimal    # Import the reserve_animal method
import intake                               # Import the intake methods
import initialize                           # Import the initialize methods
import print_animals                        # Import the print_animals method
import search                               # Import the search_and_update_animal method

class Driver:
    # Revision change from List to Dictionary:
    # With the expected expansion of the database, transitioning from a list to a dictionary
    # improves search efficiency. A list has O(n) time complexity for searching, where "n" 
    # represents the size of the list. This means that as the number of animals increases, 
    # searching through the list would take longer, growing linearly with the number of entries.
    # 
    # By switching to a dictionary, which uses hash-based indexing, we achieve an O(1) average 
    # time complexity for search operations. This provides constant time lookups regardless of 
    # the number of animals in the dictionary, making it significantly faster for retrieving 
    # an animal by its name. This decision optimizes search operations, especially as the 
    # database grows, providing much more efficient performance compared to lists.
    #
    # Dictionary Time Complexity:
    # - Search: O(1) average, O(n) worst-case (in case of hash collisions)
    # - Insertion: O(1) average, O(n) worst-case (in case of hash collisions)
    # - Deletion: O(1) average, O(n) worst-case (in case of hash collisions)
    # Source: https://wiki.python.org/moin/TimeComplexity
    dog_dict: Dict[str, Dog] = {}           # Dictionary for Dog objects
    monkey_dict: Dict[str, Monkey] = {}     # Dictionary for Monkey objects

    @staticmethod
    def main():
        scnr = input                                            # Using input() for user input
        initialize.initialize_dog_dict(Driver.dog_dict)         # Initialize dictionary of dogs
        initialize.initialize_monkey_dict(Driver.monkey_dict)   # Initialize dictionary of monkeys
        usr_input = ""                                          # Instantiating usr_input

        while usr_input != "q":     # While loop that will keep menu displayed until user presses "q"
            Driver.display_menu()   # Display user menu with options.
            usr_input = scnr()      # Set usr_input to scanner to capture user keystrokes.

            if usr_input == "1":                            # If user inputs 1, it will invoke the intake_new_dog method.
                print("Beginning Dog Intake")
                intake.intake_new_dog(Driver.dog_dict)      # Use intake.intake_new_dog to add a new dog to the database.

            elif usr_input == "2":                              # If user inputs 2, it will invoke the intake_new_monkey method.
                print("Beginning Monkey Intake")
                intake.intake_new_monkey(Driver.monkey_dict)    # Use intake.intake_new_monkey to add a new monkey to the database.

            elif usr_input == "3":                                                  # If user inputs 3, it will invoke the reserve_animal method.
                print("Beginning Animal Reservation")
                ReserveAnimal.reserve_animal(Driver.dog_dict, Driver.monkey_dict)   # Use ReserveAnimal.reserve_animal to search for and reserve an animal.

            elif usr_input == "4":                                                  # If user inputs 4, 5, or 6 it will invoke the print_animals method.
                print("Displaying List of dogs")
                print_animals.print_animals(1, Driver.dog_dict, Driver.monkey_dict) # Use print_animals.print_animals to display all dogs.

            elif usr_input == "5":                                                  
                print("Displaying List of monkeys")
                print_animals.print_animals(2, Driver.dog_dict, Driver.monkey_dict) # Use print_animals.print_animals to display all monkeys.

            elif usr_input == "6":                                                  
                print("Displaying List of unreserved animals")
                print_animals.print_animals(3, Driver.dog_dict, Driver.monkey_dict) # Use print_animals.print_animals to display all unreserved dogs and monkeys.
            
            elif usr_input == "7":                                          # If user inputs 7, it will invoke the search_animal method.
                print("Searching Database")
                search.search_animal(Driver.dog_dict, Driver.monkey_dict)   # Use search_animal to find animal and edit it.

            elif usr_input == "q":  # If user inputs "q", it will quit the loop and exit the program.
                print("Quitting.")

            else:  # If user inputs any other character, it will respond with invalid command and request a new input.
                print("Invalid command.")

    # Method to build the initial menu when program starts
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
        print("[7] Search for animal, and update status")
        print("[q] Quit application")
        print()
        print("Enter a menu selection")

if __name__ == "__main__":
    Driver.main()
