#########################################################################################################################
#                                         Grazioso Salvare Animal Rescue System                                         #
#                                                                                                                       #
# This script provides functions to intake new dogs and monkeys into the Grazioso Salvare Dog and Monkey                #
# database. It allows the user to input details for each animal, verifies if the animal already exists,                 #
# and appends the new animal to the respective list. The intake process ensures that all necessary data                 #
# fields are captured, and valid species are selected for monkeys.                                                      #
#                                                                                                                       #
# Author: Richard VanSkike                                                                                              #
# Revision: 2.0                                                                                                         #
# Course: CS-499 Computer Science Capstone                                                                              #
# Source: Milestone 2 - Enhancement One: Software Design and Engineering                                                #
# College: Southern New Hampshire University                                                                            #
#                                                                                                                       #
# Dependencies: dog (custom module), monkey (custom module), validation (custom module),                                #
#                                                                                                                       #
# Functions:                                                                                                            #
#     intake_new_dog(dog_dict) - Prompts the user to input details for a new dog, verifies that the dog                 #
#                                does not already exist in the list, and appends the new Dog object to the list.        #
#     intake_new_monkey(monkey_dict) - Prompts the user to input details for a new monkey, verifies that the            #
#                                      monkey does not already exist in the list, checks species validity,              #
#                                      and appends the new Monkey object to the list.                                   #
#                                                                                                                       #
# Usage:                                                                                                                #
#     Call `intake_new_dog(dog_dict)` to add a new dog to the `dog_dict`.                                               #
#     Call `intake_new_monkey(monkey_dict)` to add a new monkey to the `monkey_dict`.                                   #
#########################################################################################################################
from dog import Dog                 # Import the Dog class from dog.py
from monkey import Monkey           # Import the Monkey class from monkey.py
from validation import Validation   # Import the Validation class from validation.py

# Method to proccess addtion of dog to dog_dict
# It will intake each necessary item for the dictionary
def intake_new_dog(dog_dict):
    # Intake for Name with validation (should not be null)
    name = input("What is the dog's name?: ").strip().lower()
    name = Validation.null_validation(name, "name").capitalize()
    
    # Check to confirm Dog name does not already exist in the dog_dict
    if name in dog_dict:
        print("\n\nThis dog is already in our system\n\n")
        return  # returns to menu
    
    print(f"Adding Dog: {name}")

    # Intake for Breed with validation (should not be null)
    breed = input("What is the dog's breed?: ").strip()
    breed = Validation.null_validation(breed, "breed").capitalize()
    
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
    acquisition_country = input("What Country did the dog come from?: ").strip()
    acquisition_country = Validation.null_validation(acquisition_country, "country").capitalize()
    
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
    in_service_country = input("What country is the dog in service?: ").strip()
    in_service_country = Validation.null_validation(in_service_country, "country").capitalize()
    
    print(f"Country of Service: {in_service_country}")

    # Create a new Dog object with the provided inputs
    dog = Dog(name, breed, gender, age, weight, acquisition_date, 
              acquisition_country, training_status, reserved, in_service_country)

    # Add the new Dog object to the dog_dict
    dog_dict[name] = dog
    print(f"New Dog {name} added!")

# Method to proccess addtion of monkey to monkey_dict
# It will intake each necessary item for the dictionary
def intake_new_monkey(monkey_dict):
    # Intake for Name with validation (should not be null)
    name = input("What is the Monkey's name?: ").strip().lower()
    name = Validation.null_validation(name, "name").capitalize()
    
    # Check to confirm Monkey name does not already exist in the monkey_dict
    if name in monkey_dict:
        print("\n\nThis Monkey is already in our system\n\n")
        return  # returns to menu
    
    print(f"Adding Monkey: {name}")

    # Intake for Species with validation (should be "Capuchin", "Guenon", "Macaque", "Marmoset", "Squirrel Monkey", "Tamarin")
    species = input("What is the Monkey's species? (Capuchin, Guenon, Macaque, Marmoset, Squirrel Monkey, Tamarin): ").strip().title()
    species = Validation.species_validation(species)
    
    print(f"Species: {species}")

    # Intake for Gender with validation (should be male or female)
    gender = input("What is the Monkey's gender? ").strip().lower()
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
    acquisition_country = input("What country did the Monkey come from?: ").strip()
    acquisition_country = Validation.null_validation(acquisition_country, "country").capitalize()
    
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
    in_service_country = input("What country is the Monkey in service?: ").strip()
    in_service_country = Validation.null_validation(in_service_country, "country").capitalize()

    print(f"Country of Service: {in_service_country}")

    # Create a new Monkey object with the provided inputs
    monkey = Monkey(name, species, gender, age, weight, tail_length,
                    height, body_length, torso_length, skull_length,
                    neck_length, acquisition_date, acquisition_country,
                    training_status, reserved, in_service_country)

    # Add the new Monkey object to the monkey_dict
    monkey_dict[name] = monkey
    print(f"New Monkey {name} added!")
