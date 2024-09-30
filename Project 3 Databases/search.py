#######################################################################################################################
#                                         Grazioso Salvare Animal Rescue System                                       #
#                                                                                                                     #
# This script provides a console-based method for searching and updating information about rescue animals.            #
# It allows users to search for an animal by name and update its details, including name, training status,            #
# and in-service country.                                                                                             #
#                                                                                                                     #
# Author: Richard VanSkike                                                                                            #
# Revision: 3.0                                                                                                       #
# Course: CS-499 Computer Science Capstone                                                                            #
# Source: Milestone 3 - Enhancement Two: Algorithms and Data Structure                                                #
# College: Southern New Hampshire University                                                                          #
#                                                                                                                     #
# Dependencies: initialize (custom module), validation (custom module)                                                #
#                                                                                                                     #
# Functions:                                                                                                          #
#     search_animal() - Searches for an animal by name and allows updating its details.                               #
#                                                                                                                     #
# Usage:                                                                                                              #
#    This script is intended to be used as part of the Rescue Animal Database application.                            #
#######################################################################################################################
from initialize import Initialize   # Import Initialize from initialize.py
from validation import Validation   # Import Validation from validation.py

def search_animal():
    # Search for a specific dog or monkey in the respective database and update details.
    #
    # Time Complexity: O(log n) on average for database lookup and updates (assuming indexes; O(n) if none).
    #                  The input/output operations (such as validation and input handling) are constant with respect to time.
    #
    # Space Complexity: O(n) - Data stored on disk, not limited by RAM. Additional space needed for index is minimal.
    name = input("Enter the name of the animal you want to search for: ").strip()
    name = Validation.null_validation(name, "name")
    found_animal = None
    animal_type = None

    # Fetch all dogs and monkeys from the database
    dogs = Initialize.fetch_all_dogs()
    monkeys = Initialize.fetch_all_monkeys()

    # Search in dogs
    for dog in dogs:
        if dog[1].lower() == name.lower():  # Assuming dog[1] is the name column
            found_animal = dog
            animal_type = 'Dog'
            break

    # Search in monkeys if not found in dogs
    if not found_animal:
        for monkey in monkeys:
            if monkey[1].lower() == name.lower():  # Assuming monkey[1] is the name column
                found_animal = monkey
                animal_type = 'Monkey'
                break

    if found_animal:
        # Convert found_animal from tuple to list
        found_animal = list(found_animal)

        print(f"\nAnimal Found: {found_animal[1]}")  # Assuming [1] is the name column
        print(f"The current Name for this {animal_type} is: {found_animal[1]}") # Confirm what name is currently set to.
        print(f"The current Training Status: {found_animal[8] if animal_type == 'Dog' else found_animal[14]}")  # Assuming [8] for dogs and [14] for monkeys is the training status column
        print(f"The current In-Service Country: {found_animal[10] if animal_type == 'Dog' else found_animal[16]}")  # Assuming [10] for dogs and [16] for monkeys is the in-service country column

        # Ask user if they want to change the training status
        # Take input and validate that it is not the correct status
        option = input(f"What would you like to update for this {animal_type}? (Enter: Name, Country, or Training): ").strip().lower()
        option = Validation.name_country_training_validation(option)

        if option == "name":
            new_name = input(f"Please enter the new name for {name.capitalize()}: ").strip().lower()
            new_name = Validation.null_validation(new_name, "name").title()

            found_animal[1] = new_name  # Update in the list
            with Initialize.conn.cursor() as cursor:
                cursor.execute(f"UPDATE {animal_type} SET name = %s WHERE id = %s", (new_name, found_animal[0]))  # Assuming [0] is the id column
            Initialize.conn.commit()
            print(f"In-service country updated to: {new_name}")
        
        elif option == "country":
            new_in_service_country = input("Enter the new in-service country: ").strip().title()
            new_in_service_country = Validation.null_validation(new_in_service_country, "country").title()

            if animal_type == 'Dog':
                found_animal[10] = new_in_service_country  # Update in the list
                with Initialize.conn.cursor() as cursor:
                    cursor.execute("UPDATE Dog SET in_service_country = %s WHERE id = %s", (new_in_service_country, found_animal[0]))  # Assuming [0] is the id column
            else:
                found_animal[16] = new_in_service_country  # Update in the list
                with Initialize.conn.cursor() as cursor:
                    cursor.execute("UPDATE Monkey SET in_service_country = %s WHERE id = %s", (new_in_service_country, found_animal[0]))  # Assuming [0] is the id column
            Initialize.conn.commit()
            print(f"In-service country updated to: {new_in_service_country}")

        elif option == "training":
            new_training_status = input("Enter the new training status (Phase I, Phase II, Phase III, Phase IV, Phase V, In Service): ").strip().lower()
            new_training_status = Validation.status_validation(new_training_status).title()

            if animal_type == 'Dog':
                found_animal[8] = new_training_status  # Update in the list
                with Initialize.conn.cursor() as cursor:
                    cursor.execute("UPDATE Dog SET training_status = %s WHERE id = %s", (new_training_status, found_animal[0]))  # Assuming [0] is the id column
            else:
                found_animal[14] = new_training_status  # Update in the list
                with Initialize.conn.cursor() as cursor:
                    cursor.execute("UPDATE Monkey SET training_status = %s WHERE id = %s", (new_training_status, found_animal[0]))  # Assuming [0] is the id column
            Initialize.conn.commit()
            print(f"Training status updated to: {new_training_status}")

    else:
        print(f"No animal with the name '{name.title()}' was found in the system.")
