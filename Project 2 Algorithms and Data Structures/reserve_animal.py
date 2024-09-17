########################################################################################################################
#                                         Grazioso Salvare Animal Rescue System                                        #
#                                                                                                                      #
# This script handles the reservation process for animals in the Grazioso Salvare Dog and Monkey database.             #
# Users can choose to reserve either a dog or a monkey based on their availability in a specified service country.     #
# The script guides the user through selecting the animal type, entering the service country, and confirming           #
# the reservation. If an animal matching the criteria is found, the user can reserve it, and the animal's              #
# reservation status is updated accordingly.                                                                           #
#                                                                                                                      #
# Author: Richard VanSkike                                                                                             #
# Revision: 2.0                                                                                                        #
# Course: CS-499 Computer Science Capstone                                                                             #
# Source: Milestone 2 - Enhancement One: Software Design and Engineering                                               #
# College: Southern New Hampshire University                                                                           #
#                                                                                                                      #
# Dependencies: validation (custom module)                                                                             #
#                                                                                                                      #
# Methods:                                                                                                             #
#     reserve_animal(dog_dict, monkey_dict) - Manages the reservation process for dogs and monkeys.                    #
#                                                                                                                      #
# Usage:                                                                                                               #
#    Call the reserve_animal function with the appropriate dog and monkey lists to initiate the reservation process.   #
########################################################################################################################
from validation import Validation   # Import the Validation class from validation.py

class ReserveAnimal:
    # Method to process reserving an animal
    # ask for animal type and validate 
    # locate animal in specific country for respective dictionary 
    # and if found ask if user would like to reserve
    def reserve_animal(dog_dict, monkey_dict):
        # Intake for animal type with validation (should match "monkey" or "dog")
        animal_type = input("Please enter the animal type you would like to reserve. (Dog or Monkey): ").strip().lower()
        animal_type = Validation.animal_type_validation(animal_type)

        # If Monkey is selected process changing service country or reservation
        if animal_type.lower() == "monkey":
            # Intake for In-service country with validation (should not be null)
            in_service_country = input("Please enter the service country: ").strip()
            in_service_country = Validation.null_validation(in_service_country, "country")
            
            # Search the monkey_dict for a monkey that matches the service country
            for monkey in monkey_dict.values():
                # Check if monkey is in service and matches service country
                if monkey.training_status.lower() != "in service":
                    continue
                # If a monkey is not found, say so, otherwise ask if they want to reserve found monkey
                if monkey.in_service_country.lower() == in_service_country.lower():
                    if monkey.reserved:
                        print(f"\n\nThere are no monkeys available in {in_service_country}")
                        return
                    else:
                        print(f"Monkey {monkey.name} is available in {in_service_country}.")
                        response_reserve = input("Would you like to reserve it? (Enter: Yes or No) ").strip().lower()
                        # Validate that user provide a yes or a no
                        response_reserve = Validation.yes_no_validation(response_reserve)
                        # process the change per user response
                        ReserveAnimal.reserved_response(response_reserve, "monkey", monkey)
        
        # If Dog is selected process changing service country or reservation
        elif animal_type.lower() == "dog":
            # Intake for In-service country with validation (should not be null)
            in_service_country = input("Please enter the service country: ").strip()
            in_service_country = Validation.null_validation(in_service_country, "country")
            
            # Search the dog_dict for a dog that matches the service country
            for dog in dog_dict.values():
                # Check if dog is in service and matches service country
                if dog.training_status.lower() != "in service":
                    continue
                # If a dog is not found, say so, otherwise ask if they want to reserve found dog
                if dog.in_service_country.lower() == in_service_country.lower():
                    if dog.reserved:
                        print(f"\n\nThere are no dogs available in {in_service_country}")
                        return
                    else:
                        print(f"Dog {dog.name} is available in {in_service_country}.")
                        response_reserve = input("Would you like to reserve it? (Enter: Yes or No): ").strip()
                        # Validate that user provide a yes or a no
                        response_reserve = Validation.yes_no_validation(response_reserve)
                        # process the change per user response
                        ReserveAnimal.reserved_response(response_reserve, "dog", dog)
                        return
                        
    # Method to process response for reserved changes
    # If a user says yes, change the status of the animal
    # to reserved, if no make no changes
    def reserved_response(response, animal_type, animal):
        if response.lower() == "yes":
            animal.reserved = True
            print(f"{animal_type.capitalize()} {animal.name} has been reserved!")
            return
        elif response.lower() == "no":
            print(f"Leaving {animal_type.lower()} {animal.name} unreserved.")
            return