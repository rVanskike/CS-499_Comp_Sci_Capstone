#######################################################################################################################
#                                         Grazioso Salvare Animal Rescue System                                       #
#                                                                                                                     #
# This script provides functions to intake new dogs and monkeys into the Grazioso Salvare Dog and Monkey              #
# database. It allows the user to input details for each animal, verifies if the animal already exists,               #
# and appends the new animal to the respective list. The intake process ensures that all necessary data               #
# fields are captured, and valid species are selected for monkeys.                                                    #
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
#   Intake - Class for handling the intake of new rescue animals.                                                     #
#                                                                                                                     #
# Methods:                                                                                                            #
#     intake_new_dog(scanner) - Collects and validates input for a new dog, then adds it to the database.             #
#     intake_new_monkey(scanner) - Collects and validates input for a new monkey, then adds it to the database.       #
#                                                                                                                     #
# Usage:                                                                                                              #
#    This script is intended to be used as part of the Rescue Animal Database application.                            #
#######################################################################################################################
from initialize import Initialize   # Import Initialize from initialize.py
from validation import Validation   # Import Validation from validation.py

class Intake:    
    # Method to proccess addtion of dog to dog database
    # It will intake each necessary item for the list
    # and validate the input against various forms
    # of validation.
    @staticmethod
    def intake_new_dog(scanner):
        # Connect to the database
        dogs = Initialize.fetch_all_dogs()

        # Intake for Name with validation (should not be null)
        name = input("What is the dog's name?: ").strip().title()
        name = Validation.null_validation(name, "name")
        
        for dog in dogs:
            if dog[1].lower() == name.lower():  # Assuming dog[1] is the name column
                print("\n\nThis dog is already in our system\n\n")
                return  # returns to menu
        
        print(f"Adding Dog: {name}")

        # Intake for Breed with validation (should not be null)
        breed = input("What is the dog's breed?: ").strip().title()
        breed = Validation.null_validation(breed, "breed")
        
        print(f"Breed: {breed}")

        # Intake for Gender with validation (should be male or female)
        gender = input("What is the dog's gender?: ").strip().lower()
        gender = Validation.gender_validation(gender)
        
        print(f"Gender: {gender.capitalize()}")

        # Intake for Age with validation (should be a positive integer)
        age = input("What is the dog's age?: ").strip()
        age = Validation.positive_digit_validation(age, "age")
        
        print(f"Age: {age}")

        # Intake for Weight with validation (should be a positive float)
        weight = input("What is the dog's weight?: ").strip()
        weight = Validation.float_validation(weight, "weight")
        
        print(f"Weight: {weight}")

        # Intake for Acquisition date with validation (should match the format mm-dd-yyyy)
        acquisition_date = input("When was the dog acquired? (mm-dd-yyyy): ").strip()
        acquisition_date = Validation.date_validation(acquisition_date)
        
        print(f"Dog Acquired: {acquisition_date}")

        # Intake for Acquisition country with validation (should not be null)
        acquisition_country = input("What Country did the dog come from?: ").strip().title()
        acquisition_country = Validation.null_validation(acquisition_country, "country")
        
        print(f"Country of Origin: {acquisition_country}")

        # Intake for Training status with validation (should match "Phase I", "Phase II", "Phase III", "Phase IV", "Phase V", or "In Service")
        training_status = input("What is the dog's training status? (Phase I, Phase II, Phase III, Phase IV, Phase V, or In Service): ").strip().lower()
        training_status = Validation.status_validation(training_status)
        
        print(f"Training Status: {training_status}")

        # Intake for Reserved status with validation (should be 'True' or 'False')
        reserved = input("Has this dog been reserved? (True or False): ").strip().lower()
        reserved = Validation.boolean_validation(reserved)
        
        print(f"Reservation Status: {reserved}")

        # Intake for In-service country with validation (should not be null)
        in_service_country = input("What country is the dog in service?: ").strip().title()
        in_service_country = Validation.null_validation(in_service_country, "country")
        
        print(f"Country of Service: {in_service_country}")

        # Insert the new Dog object into the database
        with Initialize.conn.cursor() as cursor:
            cursor.execute("""
                INSERT INTO Dog (name, breed, gender, age, weight, acquisition_date, acquisition_country, training_status, reserved, in_service_country)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (name, breed, gender, age, weight, acquisition_date, acquisition_country, training_status, reserved, in_service_country))
            Initialize.conn.commit()

        print(f"New Dog {name} added to the database!")

    # Method to proccess addtion of monkey to monkey database
    # It will intake each necessary item for the list
    # and validate the input against various forms
    # of validation.
    @staticmethod
    def intake_new_monkey(scanner):
        # Fetch all monkeys from the database
        monkeys = Initialize.fetch_all_monkeys()

        # Intake for Name with validation (should not be null)
        name = input("What is the Monkey's name?: ").strip().title()
        name = Validation.null_validation(name, "name")
        
        for monkey in monkeys:
            if monkey[1].lower() == name.lower():  # Assuming monkey[1] is the name column
                print("\n\nThis Monkey is already in our system\n\n")
                return  # returns to menu
        
        print(f"Adding Monkey: {name}")

        # Intake for Species with validation (should be "Capuchin", "Guenon", "Macaque", "Marmoset", "Squirrel Monkey", "Tamarin")
        species = input("What is the Monkey's species? (Capuchin, Guenon, Macaque, Marmoset, Squirrel Monkey, Tamarin): ").strip().title()
        species = Validation.species_validation(species)
        
        print(f"Species: {species}")

        # Intake for Gender with validation with validation (should be male or female)
        gender = input("What is the Monkey's gender?: ").strip().lower()
        gender = Validation.gender_validation(gender)

        print(f"Gender: {gender}")

        # Intake for Age with validation (should be a positive integer)
        age = input("What is the Monkey's age?: ").strip()
        age = Validation.positive_digit_validation(age, "age")

        print(f"Age: {age}")

        # Intake for Weight with validation (should be a positive float)
        weight = input("What is the Monkey's weight?: ").strip()
        weight = Validation.float_validation(weight, "weight")
        
        print(f"Weight: {weight}")

        # Intake for Tail length with validation (should be a positive number)
        tail_length = input("What is the Monkey's tail length?: ").strip()
        tail_length = Validation.positive_digit_validation(tail_length, "tail length")

        print(f"Tail Length: {tail_length}")

        # Intake for Height with validation (should be a positive number)
        height = input("What is the Monkey's height?: ").strip()
        height = Validation.positive_digit_validation(height, "height")

        print(f"Height: {height}")

        # Intake for Body length with validation (should be a positive number)
        body_length = input("What is the Monkey's body length?: ").strip()
        body_length = Validation.positive_digit_validation(body_length, "body length")

        print(f"Body Length: {body_length}")

        # Intake for Torso length with validation (should be a positive number)
        torso_length = input("What is the Monkey's torso length?: ").strip()
        torso_length = Validation.positive_digit_validation(torso_length, "torso length")

        print(f"Torso Length: {torso_length}")

        # Intake for Skull length with validation (should be a positive number)
        skull_length = input("What is the Monkey's skull length?: ").strip()
        skull_length = Validation.positive_digit_validation(skull_length, "skull length")

        print(f"Skull Length: {skull_length}")

        # Intake for Neck length with validation (should be a positive number)
        neck_length = input("What is the Monkey's neck length?: ").strip()
        neck_length = Validation.positive_digit_validation(neck_length, "neck length")

        print(f"Neck Length: {neck_length}")

        # Intake for Acquisition date with validation (should match the format mm-dd-yyyy)
        acquisition_date = input("When was the Monkey Acquired? (mm-dd-yyyy): ").strip()
        acquisition_date = Validation.date_validation(acquisition_date)

        print(f"Acquired: {acquisition_date}")

        # Intake for Acquisition country with validation (should not be null)
        acquisition_country = input("What country did the Monkey come from?: ").strip().title()
        acquisition_country = Validation.null_validation(acquisition_country, "country")
        
        print(f"Country of Origin: {acquisition_country}")

        # Intake for Training status with validation (should match "Phase I", "Phase II", "Phase III", "Phase IV", "Phase V", or "In Service")    
        training_status = input("What is the Monkey's training status? (Phase I, Phase II, Phase III, Phase IV, Phase V, or In Service): ").strip().lower()
        training_status = Validation.status_validation(training_status)

        print(f"Training Status: {training_status.capitalize()}")

        # Intake for Reserved status with validation (should be 'True' or 'False')
        reserved = input("Has this Monkey been reserved? (True or False): ").strip().lower()
        reserved = Validation.boolean_validation(reserved)

        print(f"Reservation Status: {reserved}")

        # Intake for In-service country with validation (should not be null)
        in_service_country = input("What country is the Monkey in service?: ").strip().title()
        in_service_country = Validation.null_validation(in_service_country, "country")

        print(f"Country of Service: {in_service_country}")

        # Insert the new Monkey object into the database
        with Initialize.conn.cursor() as cursor:
            cursor.execute("""
                INSERT INTO Monkey (name, species, gender, age, weight, tail_length, height, body_length, 
                                    torso_length, skull_length, neck_length, acquisition_date, acquisition_country, 
                                    training_status, reserved, in_service_country)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (name, species, gender, age, weight, tail_length, height, body_length, 
                torso_length, skull_length, neck_length, acquisition_date, acquisition_country, 
                training_status, reserved, in_service_country))
            Initialize.conn.commit()

        print(f"New Monkey {name} added to the database!")

