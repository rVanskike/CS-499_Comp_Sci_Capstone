########################################################################################################################
#                                         Grazioso Salvare Animal Rescue System                                        #
#                                                                                                                      #
# This module defines the `search_animal` function, which allows users to search for a dog or monkey in the system     #
# and make changes to the animal's name, in-service country, or training status. The function uses dictionaries to     #
# store and retrieve animal information, leveraging validation methods to ensure accurate input.                       #
#                                                                                                                      #
# Author: Richard VanSkike                                                                                             #
# Revision: 2.0                                                                                                        #
# Course: CS-499 Computer Science Capstone                                                                             #
# Source: Milestone 2 - Enhancement One: Software Design and Engineering                                               #
# College: Southern New Hampshire University                                                                           #
#                                                                                                                      #
# Dependencies: typing, dog (custom module), monkey (custom module), validation (custom module)                        #
#                                                                                                                      #
# Functions:                                                                                                           #
#     search_animal(dog_dict, monkey_dict) - Searches for a dog or monkey by name and allows updating of the animal's  #
#                                            name, in-service country, or training status based on user input.         #
#                                                                                                                      #
# Usage:                                                                                                               #
#     This module is used to manage and update animal records in the Grazioso Salvare Dog and Monkey database project. #
########################################################################################################################
from typing import Dict                     # Import Dictionary object from typing library
from dog import Dog                         # Import the Dog class from dog.py
from monkey import Monkey                   # Import the Monkey class from monkey.py
from validation import Validation           # Import the Validation class from validation.py

# Method to search for an animal, and make changes to it
# Locate the animal using the name and type. Change
# the name or the country of the animal depending on user input.
def search_animal(dog_dict: Dict[str, Dog], monkey_dict: Dict[str, Monkey]):
    # Search for a specific dog or monkey in the respective dictionary and update details.
    #
    # Time Complexity: O(1) on average for dictionary lookup and updates (assuming the hash table is well-balanced).
    #                  O(n) in the worst case for dictionary operations if there are hash collisions.
    #                  The input/output operations (such as validation and input handling) are constant with respect to time.
    #
    # Space Complexity: O(1) - No additional space grows with the size of the input, except for minor input/output variables.
    animal_type = input("Please enter the animal type you would like to search for. (Dog or Monkey): ").strip().lower()
    animal_type = Validation.animal_type_validation(animal_type)
    
    # Intake for name with validation (should not be null)
    name = input("Please enter the animal name: ").strip().lower()
    name = Validation.null_validation(name, "name")

    # Handle search for animal type Dog
    if animal_type == "dog":
        if name not in dog_dict:
            print(f"The dog named {name.capitalize()} was not found in the system.")
            return
        else:
            animal = dog_dict[name]
            print(f"The dog named {name.capitalize()} has been found in the system.")
            print(f"The current name for this dog is: {animal.name}.")
            print(f"The current country for this dog is: {animal.in_service_country}.")
            print(f"The current training status for this dog is: {animal.training_status}.\n")
            
            # Intake for option to change name or country with validation (should match "name" or "country")
            option = input("What would you like to update for this dog? (Enter: Name, Country, or Training): ").strip().lower()
            option = Validation.name_country_training_validation(option)
            
            # If name is selected, validate new name, process the changes to the name
            if option == "name":
                new_name = input(f"Please enter the new name for {name.capitalize()}: ").strip().lower()
                new_name = Validation.null_validation(new_name, "name").capitalize()
                dog_dict[new_name] = dog_dict.pop(name)
                animal.name = new_name
                print(f"Dog's name has been changed to: {new_name.capitalize()}")
            
            # If country is selected, validate new country, process the changes to the country
            elif option == "country":
                new_country = input(f"Please enter the new country for {name.capitalize()}: ").strip().lower()
                new_country = Validation.null_validation(new_country, "country").capitalize()
                animal.in_service_country = new_country
                print(f"{name.capitalize()} is now assigned to the country: {new_country.capitalize()}.")
            
            # If training is selected, validate new training status, process the changes to the training status
            elif option == "training":
                new_training_status = input(f"Please enter the new training status for {name.capitalize()}: ").strip().lower()
                new_training_status = Validation.status_validation(new_training_status)
                animal.training_status = new_training_status
                print(f"{name.capitalize()} is now assigned to the status: {new_training_status.capitalize()}.")

    # Handle search for animal type Monkey
    elif animal_type == "monkey":
        if name not in monkey_dict:
            print(f"The monkey named {name.capitalize()} was not found in the system.")
            return
        else:
            animal = monkey_dict[name]
            print(f"The monkey named {name.capitalize()} has been found in the system.")
            print(f"The current name for this monkey is: {animal.name}.")
            print(f"The current country for this monkey is: {animal.in_service_country}.\n")
            print(f"The current training status for this monkey is: {animal.training_status}.\n")
            
            # Intake for option to change name or country with validation (should match "name" or "country")
            option = input("What would you like to update for this monkey? (Enter: Name, Country, or Training): ").strip().lower()
            option = Validation.name_country_training_validation(option)
            
            # If name is selected, validate new name, process the changes to the name
            if option == "name":
                new_name = input(f"Please enter the new name for {name.capitalize()}: ").strip().lower()
                new_name = Validation.null_validation(new_name, "name").capitalize()
                monkey_dict[new_name] = monkey_dict.pop(name)
                animal.name = new_name
                print(f"Monkey's name has been changed to: {new_name.capitalize()}")
            
            # If country is selected, validate new country, process the changes to the country
            elif option == "country":
                new_country = input(f"Please enter the new country for {name.capitalize()}: ").strip().lower()
                new_country = Validation.null_validation(new_country, "country").capitalize()
                animal.in_service_country = new_country
                print(f"{name.capitalize()} is now assigned to the country: {new_country.capitalize()}.")
            
            # If training is selected, validate new training status, process the changes to the training status
            elif option == "training":
                new_training_status = input(f"Please enter the new training status for {name.capitalize()}: ").strip().lower()
                new_training_status = Validation.status_validation(new_training_status)
                animal.training_status = new_training_status
                print(f"{name.capitalize()} is now assigned to the status: {new_training_status.capitalize()}.")
