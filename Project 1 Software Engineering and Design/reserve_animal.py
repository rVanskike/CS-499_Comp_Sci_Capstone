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
# Revision: 1.0                                                                                                        #
# Course: CS-499 Computer Science Capstone                                                                             #
# Source: IT-145 Foundation in Application Development                                                                 #
# College: Southern New Hampshire University                                                                           #
#                                                                                                                      #
# Methods:                                                                                                             #
#     reserve_animal(dog_list, monkey_list) - Manages the reservation process for dogs and monkeys.                    #
#                                                                                                                      #
# Usage:                                                                                                               #
#    Call the reserve_animal function with the appropriate dog and monkey lists to initiate the reservation process.   #
########################################################################################################################
# Method to process reserving an animal
# ask for animal type and locate animal 
# in specific country for respective list 
# and if found ask if user would like to reserve
def reserve_animal(dog_list, monkey_list):
    # Intake for animal type
    animal_type = input("Please enter the animal type you would like to reserve. (Dog or Monkey) ").strip()
    
    # If Monkey is selected process changing service country or reservation
    if animal_type.lower() == "monkey":
        # Intake for In-service country
        in_service_country = input("Please enter the service country: ").strip()
        
        # Loop through the monkey_list searching for a monkey that matches the service country
        for monkey in monkey_list:
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
                    response_temp = input("Would you like to reserve it? (Enter: Yes or No) ").strip()
                    # process the change per user response
                    if response_temp.lower() == "yes":
                        monkey.reserved = True
                        print(f"Monkey {monkey.name} has been reserved!")
                        return
                    elif response_temp.lower() == "no":
                        print(f"Leaving monkey {monkey.name} unreserved.")
                        return
    
    # If Dog is selected process changing service country or reservation
    elif animal_type.lower() == "dog":
        # Intake for In-service country
        in_service_country = input("Please enter the service country: ").strip()
        
        # Loop through the dog_list searching for a dog that matches the service country
        for dog in dog_list:
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
                    response_temp = input("Would you like to reserve it? (Enter: Yes or No) ").strip()
                    # process the change per user response
                    if response_temp.lower() == "yes":
                        dog.reserved = True
                        print(f"Dog {dog.name} has been reserved!")
                        return
                    elif response_temp.lower() == "no":
                        print(f"Leaving dog {dog.name} unreserved.")
                        return
