#######################################################################################################################
#                                         Grazioso Salvare Animal Rescue System                                       #
#                                                                                                                     #
# This script serves as the main driver for the Grazioso Salvare Dog and Monkey database project. It initializes      #
# the application, handles user interaction through a menu-driven interface, and processes user commands to manage    #
# the intake, reservation, and display of animals in the database.                                                    #
#                                                                                                                     #
# Author: Richard VanSkike                                                                                            #
# Revision: 3.0                                                                                                       #
# Course: CS-499 Computer Science Capstone                                                                            #
# Source: Milestone 3 - Enhancement Two: Algorithms and Data Structure                                                #
# College: Southern New Hampshire University                                                                          #
#                                                                                                                     #
# Dependencies: initialize (custom module), reserve_animal (custom module), intake (custom module),                   #
#               security (custom module), validation (custom module), tkinter, print_animals (custom module),         #
#               search (custom module), dashboard (custom module)                                                     #
#                                                                                                                     #
# Classes:                                                                                                            #
#   Driver - Main class for handling user interaction and routing.                                                    #
#                                                                                                                     #
# Methods:                                                                                                            #
#     login() - Prompts the user to log in and verifies credentials.                                                  #
#     main() - Main method that displays the menu and routes user inputs.                                             #
#     display_menu() - Displays the main menu options.                                                                #
#                                                                                                                     #
# Usage:                                                                                                              #
#    Run this script to launch the Rescue Animal Database application.                                                #
#######################################################################################################################
from initialize import Initialize               # Import Initialize class from initialize.py
from intake import Intake                       # Import Intake class from intake.py
from reserve_animal import ReserveAnimal        # Import ReserveAnimal class from reserve_animal.py
from security import Security                   # Import Security class from security.py
import tkinter as tk                            # Import tkinter as tk to provide UI capabilties
from validation import Validation               # Import Validation class from validation.py
import dashboard                                # Import dashboard.py
import print_animals                            # Import print_animals.py
import search                                   # Import the search.py

# Revision change from Dictionary to PostgreSQL Database:
# With the need for more scalable and persistent data management, transitioning from an
# in-memory dictionary to a PostgreSQL database enhances both performance and data integrity.
# While dictionaries offer O(1) average time complexity for search operations, they are
# limited by memory constraints and lack persistence across sessions.
#
# A PostgreSQL database allows for efficient storage and retrieval of larger datasets without
# being limited by memory. Using SQL queries, we can search the database with high efficiency
# using indexed columns, such as animal names, ensuring that lookups remain fast even as the 
# database grows in size. In particular, database indexing provides an O(log n) time complexity 
# for search operations in most cases, which remains scalable for large datasets.
#
# The integration of a GUI provides a user-friendly interface for selecting and editing records
# directly from the database. Instead of searching through the command line or raw SQL queries, 
# users can visually interact with the data, select an animal record, and perform edits, making
# the application more accessible and intuitive.
#
# PostgreSQL Database Search Time Complexity:
# - Search (with indexes): O(log n)
# - Search (without indexes): O(n)
# - Insertion: O(log n) with indexing
# 
# The combination of PostgreSQL and a GUI offers both performance and usability advantages, 
# making it suitable for large-scale applications where data integrity, persistence, and user 
# experience are priorities.
class Driver:
    @staticmethod
    def login():
        print("Welcome to the Rescue Animal System. Please log in.")
        attempts = 3
        while attempts > 0:
            username = input("Username: ")
            username = Validation.null_validation(username, "username")
            password = input("Password: ")
            password = Validation.null_validation(password, "password")
            
            user = Initialize.get_user_from_db(username)
            
            if user and Security.verify_password(password, user[2]):
                print("Login successful!")
                return True
            
            print("Invalid username or password.")
            attempts -= 1
        
        print("Too many failed attempts. Exiting.")
        return False
    
    @staticmethod
    def main():
        # User will be presented with login before they can access
        # Will not move to main menu until successful login
        if not Driver.login():
            return
            
        while True:    
            Initialize.connect_db()                     # Connect to Database
            dashboard.Dashboard(tk.Tk())                # Invoke dashboard once logged in
            scnr = input                                # Using input() for user input
            # Initialize the lists (if needed)
            # Initialize.initialize_dog_list()
            # Initialize.initialize_monkey_list()
            usr_input = ""                              # Instantiate usr_input

            while usr_input != "q":                     # While loop that will keep menu displayed until user presses "q"
                Driver.display_menu()                   # Display user menu with options.
                usr_input = scnr()                      # Set usr_input to scanner to capture user keystrokes.

                if usr_input == "1":                    # If user inputs 1, it will invoke the intake_new_dog method.
                    print("Beginning Dog Intake")
                    Intake.intake_new_dog(scnr)         # Use intake.intake_new_dog to add a new dog to the database.

                elif usr_input == "2":                  # If user inputs 2, it will invoke the intake_new_monkey method.
                    print("Beginning Monkey Intake")
                    Intake.intake_new_monkey(scnr)      # Use intake.intake_new_monkey to add a new monkey to the database.

                elif usr_input == "3":                  # If user inputs 3, it will invoke the reserve_animal method.
                    print("Beginning Animal Reservation")
                    ReserveAnimal.reserve_animal(scnr)  # Use ReserveAnimal.reserve_animal to search and reserve an animal.

                elif usr_input == "4":                  # If user inputs 4, 5, or 6 it will invoke the print_animals method.
                    print("Displaying List of dogs")
                    print_animals.print_animals(1)      # Use print_animals.print_animals to display all dogs.

                elif usr_input == "5":
                    print("Displaying List of monkeys")
                    print_animals.print_animals(2)      # Use print_animals.print_animals to display all monkeys.

                elif usr_input == "6":
                    print("Displaying List of unreserved animals")
                    print_animals.print_animals(3)      # Use print_animals.print_animals to display all unreserved dogs and monkeys.
                
                elif usr_input == "7":                  # If user inputs 7, will invoke the search_animal function.
                    print("Searching Database")
                    search.search_animal()              # Use search_animal to find animal and edit it.

                elif usr_input == "8":                  # If user inputs 8, will invoke the add_user function.
                    print("Adding New User")
                    Security.add_user(scnr)             # Use add_user to add a new user to the database.

                elif usr_input == "9":                  # If user inputs 9, will display dashboard.
                    print("Displaying Dashboard")
                    dashboard.Dashboard(tk.Tk())        # Use Dashboard to bring up graphical user interface.

                elif usr_input == "q":                  # If user inputs "q" it will quit the loop and exit the program.
                    print("Quitting.")
                    Initialize.close_db()               # Close connection to database
                    return 'q'

                else:                                   # If user inputs any other char it will respond invalid command and request a new input.
                    print("Invalid command.")

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
        print("[8] Add a new user")
        print("[9] Display Dashboard")
        print("[q] Quit application")
        print()
        print("Enter a menu selection")

if __name__ == "__main__":
    Driver.main()