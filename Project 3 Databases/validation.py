#######################################################################################################################
#                                         Grazioso Salvare Animal Rescue System                                       #
#                                                                                                                     #
# This script provides validation methods for various types of input used in the Rescue Animal Dashboard application. #
# It includes functions to validate null values, positive integers, gender, floats, dates, statuses, booleans,        #
# species, animal types, yes/no responses, and option choices.                                                        #
#                                                                                                                     #
# Author: Richard VanSkike                                                                                            #
# Revision: 3.0                                                                                                       #
# Course: CS-499 Computer Science Capstone                                                                            #
# Source: Milestone 3 - Enhancement Two: Algorithms and Data Structure                                                #
# College: Southern New Hampshire University                                                                          #
#                                                                                                                     #
# Dependencies: re (regular expressions)                                                                              #
#                                                                                                                     #
# Classes:                                                                                                            #
#   Validation - Class containing static methods for input validation.                                                #
#                                                                                                                     #
# Methods:                                                                                                            #
#     null_validation(value, variable) - Validates that the input is not null.                                        #
#     positive_digit_validation(value, variable) - Validates that the input is a positive integer.                    #
#     gender_validation(value) - Validates that the input is either 'male' or 'female'.                               #
#     float_validation(value, variable) - Validates that the input is a positive float.                               #
#     date_validation(value) - Validates that the input is a date in the format mm-dd-yyyy.                           #
#     status_validation(value) - Validates that the input is a valid training status.                                 #
#     boolean_validation(value) - Validates that the input is either 'true' or 'false'.                               #
#     species_validation(value) - Validates that the input is a valid monkey species.                                 #
#     animal_type_validation(value) - Validates that the input is either 'monkey' or 'dog'.                           #
#     yes_no_validation(value) - Validates that the input is either 'yes' or 'no'.                                    #
#     name_country_training_validation(value) - Validates that the input is a valid option choice.                    #
#                                                                                                                     #
# Usage:                                                                                                              #
#    This script is intended to be used as part of the Rescue Animal Database application.                            #
#######################################################################################################################
import re # Import Regular Expression

class Validation:
    # Method to proccess validation of null values
    # It will intake input value and variable name
    # if it is null, it will advise that it cannot
    # be and request input, then return the results
    def null_validation(value, variable):
        while True:
            if value.strip():
                break
            value = input(f"{variable.capitalize()} cannot be empty. Please enter a valid {variable}: ").strip()
        return value

    # Method to proccess validation of integer values
    # It will intake input value and variable name
    # if it is anything other than a positive value 
    # it will advise that it cannot be and request 
    # input, then return the results
    def positive_digit_validation(value, variable):
        while True:
            if value.isdigit() and int(value) > 0:
                break
            value = input(f"Please enter a valid positive number for {variable}: ")
        return value
        
    # Method to proccess validation of gender values
    # It will intake input value and if it is not 
    # male or female, it will advise that it must 
    # be and request input, then return the results
    def gender_validation(value):
        while True:
            if value in ['male', 'female']:
                break
            value = input("Please enter 'Male' or 'Female' for gender: ").strip().lower()
        return value.capitalize()
    
    # Method to proccess validation of float values
    # It will intake input value and variable name
    # if it is anything other than a positive value
    # it will advise that it cannot be and request 
    # input, then return the results
    def float_validation(value, variable):
        while True:
            try:
                value_float = float(value)
                if value_float > 0:
                    break
                value = input(f"{variable.capitalize()} must be a positive number: ").strip()
            except ValueError:
                value = input(f"Please enter a valid number for {variable}: ").strip()
        return value
    
    # Method to proccess validation of dates
    # It will intake input value ans if it is 
    # anything other than formate mm-dd-yyyy, 
    # it will advise that it cannot be and request 
    # input, then return the results
    def date_validation(value):
        while True:
            if re.match(r"^\d{2}-\d{2}-\d{4}$", value):
                break
            value = input("Please enter a valid date. (mm-dd-yyyy): ").strip()
        return value

    # Method to proccess validation of status
    # It will intake input value if it is anything 
    # other than valid_status, it will advise that 
    # it cannot be and request input, then return 
    # the results  
    def status_validation(value):
        valid_status = ["Phase I", "Phase II", "Phase III", "Phase IV", "Phase V", "In Service"]
        while True:
            normalized_status = [status.lower() for status in valid_status]
            if value in normalized_status:
                # Convert back to the correct format before assigning or using it
                value = valid_status[normalized_status.index(value)]
                break
            value = input(f"Please enter a valid training status ({', '.join(valid_status)}): ").strip().lower()
        return value
    
    # Method to proccess validation of boolean status
    # It will intake input value if it is anything 
    # other than true or false, it will advise that
    # it cannot be and request input, then return 
    # the results
    def boolean_validation(value):
        while True:
            if value in ['true', 'false']:
                reserved = value == 'true'
                return reserved
            value = input("Please enter 'True' or 'False' for reserved status: ").strip().lower()
            
    # Method to proccess validation of species
    # It will intake input value if it is anything 
    # other than valid_species, it will advise that 
    # it cannot be and request input, then return 
    # the results  
    def species_validation(value):
        valid_species = ["Capuchin", "Guenon", "Macaque", "Marmoset", "Squirrel Monkey", "Tamarin"]
        while True:
            if value in valid_species:
                 break
            value = input(f"Please enter a valid monkey species  ({', '.join(valid_species)}): ").strip().title()
        return value
    
    # Method to proccess validation of animal type
    # It will intake input value if it is anything 
    # other than valid_animal, it will advise that 
    # it cannot be and request input, then return 
    # the results  
    def animal_type_validation(value):
        valid_animal = ["monkey", "dog"]
        while True:
            if value in valid_animal:
                 break
            value = input(f"Please enter a valid animal type ({', '.join(valid_animal)}): ").strip().lower()
        return value
    
    # Method to proccess validation of yes or no
    # It will intake input value if it is anything 
    # other than valid_response, it will advise that 
    # it cannot be and request input, then return 
    # the results   
    def yes_no_validation(value):
        valid_response = ["yes", "no"]
        while True:
            if value in valid_response:
                 break
            value = input(f"Please enter a valid response ({', '.join(valid_response)}): ").strip().lower()
        return value

    # Method to proccess validation of option choices
    # It will intake input value if it is anything 
    # other than valid_option, it will advise that 
    # it cannot be and request input, then return 
    # the results    
    def name_country_training_validation(value):
        valid_option = ["name", "country", "training"]
        while True:
            if value in valid_option:
                break
            value = input(f"Please enter a valid option ({', '.join(valid_option)}): ").strip().lower()
        return value