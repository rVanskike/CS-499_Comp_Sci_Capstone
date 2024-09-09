#########################################################################################################################
#                                         Grazioso Salvare Animal Rescue System                                         #
#                                                                                                                       #
# This script provides functions to intake new dogs and monkeys into the Grazioso Salvare Dog and Monkey                #
# database. It allows the user to input details for each animal, verifies if the animal already exists,                 #
# and appends the new animal to the respective list. The intake process ensures that all necessary data                 #
# fields are captured, and valid species are selected for monkeys.                                                      #
#                                                                                                                       #
# Author: Richard VanSkike                                                                                              #
# Revision: 1.0                                                                                                         #
# Course: CS-499 Computer Science Capstone                                                                              #
# Source: IT-145 Foundation in Application Development                                                                  #
# College: Southern New Hampshire University                                                                            #
#                                                                                                                       #
# Dependencies: dog (custom module), monkey (custom module)                                                             #
#                                                                                                                       #
# Functions:                                                                                                            #
#     intake_new_dog(dog_list) - Prompts the user to input details for a new dog, verifies that the dog                 #
#                                does not already exist in the list, and appends the new Dog object to the list.        #
#     intake_new_monkey(monkey_list) - Prompts the user to input details for a new monkey, verifies that the            #
#                                      monkey does not already exist in the list, checks species validity,              #
#                                      and appends the new Monkey object to the list.                                   #
#                                                                                                                       #
# Usage:                                                                                                                #
#     Call `intake_new_dog(dog_list)` to add a new dog to the `dog_list`.                                               #
#     Call `intake_new_monkey(monkey_list)` to add a new monkey to the `monkey_list`.                                   #
#########################################################################################################################
from dog import Dog         # Import the Dog class from dog.py
from monkey import Monkey   # Import the Monkey class from monkey.py

# Method to proccess addtion of dog to dog_list
# It will intake each necessary item for the list
def intake_new_dog(dog_list):
    # Intake for Name
    name = input("What is the dog's name? ")
    for dog in dog_list:
        # Check to confirm Dog name does not already exist in the dog_list
        if dog.name.lower() == name.lower():
            print("\n\nThis dog is already in our system\n\n")
            return  # returns to menu
    
    print(f"Adding Dog: {name}")

    # Intake for Breed
    breed = input("What is the dog's breed? ")
    print(f"Breed: {breed}")
    
    # Intake for Gender
    gender = input("What is the dog's gender? ")
    print(f"Gender: {gender}")

    # Intake for Age 
    age = input("What is the dog's age? ")
    print(f"Age: {age}")
    
    # Intake for Weight
    weight = input("What is the dog's weight? ")
    print(f"Weight: {weight}")

    # Intake for Acquisition date
    acquisition_date = input("When was the dog acquired? Format: mm-dd-yyyy ")
    print(f"Dog Acquired: {acquisition_date}")

    # Intake for Acquisition country
    acquisition_country = input("What Country did the dog come from? ")
    print(f"Country of Origin: {acquisition_country}")

    # Intake for Training status
    print("What is the dog's training status?")
    print("Phase I, Phase II, Phase III, Phase IV, Phase V, or In Service")
    training_status = input()
    print(f"Training Status: {training_status}")

    # Intake for Reserved status
    reserved_temp = input("Has this dog been reserved? (True or False) ")
    print(f"Reservation Status: {reserved_temp}")
    reserved = reserved_temp.lower() == 'true'  # Convert to boolean

    # Intake for In-service
    in_service_country = input("What country is the dog in service? ")
    print(f"Country of Service: {in_service_country}")

    # Create a new Dog object with the provided inputs
    dog4 = Dog(name, breed, gender, age, weight, acquisition_date, 
            acquisition_country, training_status, reserved, in_service_country)

    # Add the new Dog object to the dog_list
    dog_list.append(dog4)
    print(f"New Dog {name} added!")

# Method to proccess addtion of monkey to monkey_list
# It will intake each necessary item for the list
def intake_new_monkey(monkey_list):
    # Intake for Name
    name = input("What is the Monkey's name? ").lower()
    # Check to confirm Monkey name does not already exist in the monkey_list
    for monkey in monkey_list:
        if monkey.name.lower() == name.lower():
            print("\n\nThis Monkey is already in our system\n\n")
            return  # returns to menu
    
    print(f"Adding Monkey: {name}")

    # Intake for Species
    species = input("What is the Monkey's species? ")
    if species.lower() not in ["capuchin", "guenon", "macaque", "marmoset", "squirrel monkey", "tamarin"]:
        print("This monkey species is not allowed. Please choose another.")
        return
    print(f"Species: {species}")

    # Intake for Gender
    gender = input("What is the Monkey's gender? ")
    print(f"Gender: {gender}")

    # Intake for Age
    age = input("What is the Monkey's age? ")
    print(f"Age: {age}")

    # Intake for Weight
    weight = input("What is the Monkey's weight? ")
    print(f"Weight: {weight}")

    # Intake for Tail length
    tail_length = input("What is the Monkey's tail length? ")
    print(f"Tail Length: {tail_length}")

    # Intake for Height
    height = input("What is the Monkey's height? ")
    print(f"Height: {height}")

    # Intake for Body length
    body_length = input("What is the Monkey's body length? ")
    print(f"Body Length: {body_length}")

    # Intake for Torso length
    torso_length = input("What is the Monkey's torso length? ")
    print(f"Torso Length: {torso_length}")

    # Intake for Skull length
    skull_length = input("What is the Monkey's skull length? ")
    print(f"Skull Length: {skull_length}")

    # Intake for Neck length
    neck_length = input("What is the Monkey's neck length? ")
    print(f"Neck Length: {neck_length}")

    # Intake for Acquisition date
    acquisition_date = input("When was the Monkey Acquired? Format: mm-dd-yyyy ")
    print(f"Monkey Acquired: {acquisition_date}")

    # Intake for Acquisition country
    acquisition_country = input("What Country did the Monkey come from? ")
    print(f"Country of Origin: {acquisition_country}")

    # Intake for Training status
    print("What is the Monkey's training status?")
    print("Phase I, Phase II, Phase III, Phase IV, Phase V, or In Service")
    training_status = input().strip().lower()
    print(f"Training Status: {training_status}")

    # Intake for Reserved status
    reserved_temp = input("Has this Monkey been reserved? (True or False) ")
    print(f"Reservation Status: {reserved_temp}")
    reserved = reserved_temp.lower() == 'true'  # Convert to boolean

    # Intake for In-service country
    in_service_country = input("What country is the Monkey in service? ")
    print(f"Country of Service: {in_service_country}")

    # Create a new Monkey object with the provided inputs
    monkey4 = Monkey(name, species, gender, age, weight, tail_length, height, body_length, 
                    torso_length, skull_length, neck_length, acquisition_date, acquisition_country, 
                    training_status, reserved, in_service_country)

    # Add the new Monkey object to the monkey_list
    monkey_list.append(monkey4)
    print(f"New Monkey {name} added!")
