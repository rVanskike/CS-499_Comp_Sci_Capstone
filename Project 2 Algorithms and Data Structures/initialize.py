########################################################################################################################
#                                         Grazioso Salvare Animal Rescue System                                        #
#                                                                                                                      #
# This script contains functions to initialize the lists of dogs and monkeys for the Grazioso Salvare Dog              #
# and Monkey database. These functions are designed to populate the animal lists with predefined data when             #
# the script is loaded into memory, serving as a starting point for testing and development.                           #
#                                                                                                                      #
# Author: Richard VanSkike                                                                                             #
# Revision: 2.0                                                                                                        #
# Course: CS-499 Computer Science Capstone                                                                             #
# Source: Milestone 2 - Enhancement One: Software Design and Engineering                                               #
# College: Southern New Hampshire University                                                                           #
#                                                                                                                      #
# Dependencies: dog (custom module), monkey (custom module)                                                            #
#                                                                                                                      #
# Functions:                                                                                                           #
#     initialize_dog_dict(dog_dict) - Populates the provided `dog_dict` with a predefined set of Dog objects,          #
#                                     simulating a database of dogs for initial testing and development.               #
#     initialize_monkey_dict(monkey_dict) - Populates the provided `monkey_dict` with a predefined set of Monkey       #
#                                           objects, simulating a database of monkeys for initial testing and          #
#                                           development.                                                               #
#                                                                                                                      #
# Usage:                                                                                                               #
#     Call `initialize_dog_dict(dog_dict)` to populate the `dog_dict` with initial Dog objects.                        #
#     Call `initialize_monkey_dict(monkey_dict)` to populate the `monkey_dict` with initial Monkey objects.            #
########################################################################################################################
from dog import Dog         # Import the Dog class from dog.py
from monkey import Monkey   # Import the Monkey class from monkey.py

# Method to initialize the dog dictionary
# on initialization of the script into
# memory space
def initialize_dog_dict(dog_dict):
    dog1 = Dog("Spot", "German Shepherd", "male", "1", "25.6", "05-12-2019", "United States", "intake", False, "United States")
    dog2 = Dog("Rex", "Great Dane", "male", "3", "35.2", "02-03-2020", "United States", "In service", False, "United States")
    dog3 = Dog("Bella", "Chihuahua", "female", "4", "25.6", "12-12-2019", "Canada", "in service", True, "Canada")

    dog_dict[dog1.name.lower()] = dog1
    dog_dict[dog2.name.lower()] = dog2
    dog_dict[dog3.name.lower()] = dog3

# Method to initialize the monkey dictionary
# on initialization of the script into
# memory space
def initialize_monkey_dict(monkey_dict):
    monkey1 = Monkey("Chunky", "Capuchin", "male", "2", "35.6", "12", "6", "6", "1", "2", "1", "12-12-2020", "India", "in service", False, "Canada")
    monkey2 = Monkey("Becky", "Macaque", "female", "5", "32.3", "10", "2", "3", "2", "3", "1", "01-11-2017", "China", "in service", True, "Mexico")
    
    monkey_dict[monkey1.name.lower()] = monkey1
    monkey_dict[monkey2.name.lower()] = monkey2
