#######################################################################################################################
#                                         Grazioso Salvare Animal Rescue System                                       #
#                                                                                                                     #
# This script provides a console-based method for reserving rescue animals.                                           #
# It allows users to specify the type of animal and the service country, then reserves the animal if available.       #
#                                                                                                                     #
# Author: Richard VanSkike                                                                                            #
# Revision: 3.0                                                                                                       #
# Course: CS-499 Computer Science Capstone                                                                            #
# Source: Milestone 3 - Enhancement Two: Algorithms and Data Structure                                                #
# College: Southern New Hampshire University                                                                          #
#                                                                                                                     #
# Dependencies: initialize (custom module), validation (custom module)                                                #
#                                                                                                                     #
# Classes:                                                                                                            #
#   ReserveAnimal - Class for handling the reservation of rescue animals.                                             #
#                                                                                                                     #
# Methods:                                                                                                            #
#     reserve_animal(scanner) - Processes the reservation of an animal based on user input.                           #
#                                                                                                                     #
# Usage:                                                                                                              #
#    This script is intended to be used as part of the Rescue Animal Database application.                            #
#######################################################################################################################
from initialize import Initialize   # Import Initialize from initialize.py
from validation import Validation   # Import Validation from validation.py

class ReserveAnimal:
    # Method to process reserving an animal
    # ask for animal type and validate 
    # locate animal in specific country for respective list 
    # and if found ask if user would like to reserve
    def reserve_animal(scanner):    
        # Intake for animal type with validation (should match "monkey" or "dog")
        animal_type = input("Please enter the animal type you would like to reserve. (Dog or Monkey): ").strip().lower()
        animal_type = Validation.animal_type_validation(animal_type)
        
        if animal_type in ["monkey", "dog"]:
            # Intake for In-service country with validation (should not be null)
            in_service_country = input("Please enter the service country: ").strip()
            in_service_country = Validation.null_validation(in_service_country, "country")

            # Fetch available animals from the database
            query = f"""
                SELECT id, name, reserved
                FROM {animal_type.capitalize()}
                WHERE in_service_country = %s
            """
            
            with Initialize.conn.cursor() as cursor:
                cursor.execute(query, (in_service_country,))
                animals = cursor.fetchall()

                if not animals:
                    print(f"\n\nThere are no {animal_type}s available in {in_service_country}")
                    return
                
                for animal in animals:
                    animal_id, name, reserved = animal
                    if reserved:
                        print(f"\n\nThere are no {animal_type}s available in {in_service_country}")
                        return
                    else:
                        print(f"{animal_type.capitalize()} {name} is available in {in_service_country}.")
                        response_temp = input(f"Would you like to reserve {name}? (Enter: Yes or No): ").strip().lower()
                        response_temp = Validation.yes_no_validation(response_temp)
                        
                        if response_temp == "yes":
                            # Update the reservation status in the database
                            update_query = f"""
                                UPDATE {animal_type.capitalize()}
                                SET reserved = TRUE
                                WHERE id = %s
                            """
                            cursor.execute(update_query, (animal_id,))
                            Initialize.conn.commit()
                            
                            print(f"{animal_type.capitalize()} {name} has been reserved!")
                            return
                        elif response_temp == "no":
                            print(f"Leaving {animal_type.capitalize()} {name} unreserved.")
                            return
        else:
            print("Invalid animal type. Please enter 'Dog' or 'Monkey'.")