########################################################################################################################
#                                         Grazioso Salvare Animal Rescue System                                        #
#                                                                                                                      #
# This script contains functions to initialize the lists of dogs and monkeys for the Grazioso Salvare Dog              #
# and Monkey database. These functions are designed to populate the animal lists with predefined data when             #
# the script is loaded into memory, serving as a starting point for testing and development.                           #
#                                                                                                                      #
# Author: Richard VanSkike                                                                                             #
# Revision: 1.0                                                                                                        #
# Course: CS-499 Computer Science Capstone                                                                             #
# Source: IT-145 Foundation in Application Development                                                                 #
# College: Southern New Hampshire University                                                                           #
#                                                                                                                      #
# Dependencies: dog (custom module), monkey (custom module)                                                            #
#                                                                                                                      #
# Functions:                                                                                                           #
#     initialize_dog_list(dog_list) - Populates the provided `dog_list` with a predefined set of Dog objects,          #
#                                     simulating a database of dogs for initial testing and development.               #
#     initialize_monkey_list(monkey_list) - Populates the provided `monkey_list` with a predefined set of Monkey       #
#                                           objects, simulating a database of monkeys for initial testing and          #
#                                           development.                                                               #
#                                                                                                                      #
# Usage:                                                                                                               #
#     Call `initialize_dog_list(dog_list)` to populate the `dog_list` with initial Dog objects.                        #
#     Call `initialize_monkey_list(monkey_list)` to populate the `monkey_list` with initial Monkey objects.            #
########################################################################################################################
from dog import Dog         # Import the Dog class from dog.py
from monkey import Monkey   # Import the Monkey class from monkey.py

# Method to initialize the dog list
# on initialiation of the script into
# memory space.
def initialize_dog_list(dog_list):
    dog1 = Dog("Spot", "German Shepherd", "male", "1", "25.6", "05-12-2019", "United States", "Intake", False, "United States")
    dog2 = Dog("Rex", "Great Dane", "male", "3", "35.2", "02-03-2020", "United States", "In service", False, "United States")
    dog3 = Dog("Bella", "Chihuahua", "female", "4", "25.6", "12-12-2019", "Canada", "In service", True, "Canada")

    dog_list.extend([dog1, dog2, dog3])

# Method to initialize the monkey list
# on initialiation of the script into
# memory space.
def initialize_monkey_list(monkey_list):
    monkey1 = Monkey("Chunky", "Capuchin", "male", "2", "35.6", "12", "6", "6", "1", "2", "1", "12-12-2020", "India", "In Service", False, "Canada")
    monkey2 = Monkey("Becky", "Macaque", "female", "5", "32.3", "10", "2", "3", "2", "3", "1", "01-11-2017", "China", "In Service", True, "Mexico")
    monkey3 = Monkey("BillyBob", "Macaque", "female", "5", "32.3", "10", "2", "3", "2", "3", "1", "01-11-2017", "China", "In Service", False, "United States")
    
    monkey_list.extend([monkey1, monkey2, monkey3])
