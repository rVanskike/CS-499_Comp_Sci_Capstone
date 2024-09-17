#########################################################################################################################
#                                         Grazioso Salvare Animal Rescue System                                         #
#                                                                                                                       #
# This script defines the `RescueAnimal` class, which serves as a blueprint for creating and managing                   #
# rescue animal objects in the Grazioso Salvare Dog and Monkey database. Each animal is represented                     #
# by attributes such as name, gender, age, weight, acquisition details, training status, reservation status,            #
# and service location. The class provides getter and setter methods for accessing and modifying these                  #
# attributes, allowing for dynamic interaction with rescue animal data.                                                 #
#                                                                                                                       #
# Author: Richard VanSkike                                                                                              #
# Revision: 2.0                                                                                                         #
# Course: CS-499 Computer Science Capstone                                                                              #
# Source: Milestone 2 - Enhancement One: Software Design and Engineering                                                #
# College: Southern New Hampshire University                                                                            #
#                                                                                                                       #
# Classes:                                                                                                              #
#     RescueAnimal - A class representing a rescue animal with various attributes and methods to manage them.           #
#                                                                                                                       #
# Methods:                                                                                                              #
#     __init__(self, name, gender, age, weight, acquisition_date, acquisition_country, training_status, reserved,       #
#              in_service_country) - Initializes a new instance of the RescueAnimal class with the specified attributes.#
#     get_name(self) - Returns the name of the animal.                                                                  #
#     set_name(self, name) - Sets the name of the animal.                                                               #
#     get_gender(self) - Returns the gender of the animal.                                                              #
#     set_gender(self, gender) - Sets the gender of the animal.                                                         #
#     get_age(self) - Returns the age of the animal.                                                                    #
#     set_age(self, age) - Sets the age of the animal.                                                                  #
#     get_weight(self) - Returns the weight of the animal.                                                              #
#     set_weight(self, weight) - Sets the weight of the animal.                                                         #
#     get_acquisition_date(self) - Returns the acquisition date of the animal.                                          #
#     set_acquisition_date(self, acquisition_date) - Sets the acquisition date of the animal.                           #
#     get_acquisition_location(self) - Returns the acquisition location of the animal.                                  #
#     set_acquisition_location(self, acquisition_country) - Sets the acquisition location of the animal.                # 
#     get_reserved(self) - Returns the reservation status of the animal.                                                #
#     set_reserved(self, reserved) - Sets the reservation status of the animal.                                         #
#     get_in_service_location(self) - Returns the in-service country of the animal.                                     #
#     set_in_service_country(self, in_service_country) - Sets the in-service country of the animal.                     #
#     get_training_status(self) - Returns the training status of the animal.                                            #
#     set_training_status(self, training_status) - Sets the training status of the animal.                              #
#                                                                                                                       #
# Usage:                                                                                                                #
#    Create instances of the RescueAnimal class to manage individual rescue animals' data within the Grazioso           #
#    Salvare Dog and Monkey database.                                                                                   #
#########################################################################################################################
class RescueAnimal:
    # Constructor method to establish structure for rescue_animal.
    def __init__(self, name, gender, age, weight, acquisition_date, acquisition_country, training_status, reserved, in_service_country):
        self.name = name
        self.gender = gender
        self.age = age
        self.weight = weight
        self.acquisition_date = acquisition_date
        self.acquisition_country = acquisition_country
        self.training_status = training_status
        self.reserved = reserved
        self.in_service_country = in_service_country

    # Getters and Setters    
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_gender(self):
        return self.gender

    def set_gender(self, gender):
        self.gender = gender

    def get_age(self):
        return self.age

    def set_age(self, age):
        self.age = age

    def get_weight(self):
        return self.weight

    def set_weight(self, weight):
        self.weight = weight

    def get_acquisition_date(self):
        return self.acquisition_date

    def set_acquisition_date(self, acquisition_date):
        self.acquisition_date = acquisition_date

    def get_acquisition_location(self):
        return self.acquisition_country

    def set_acquisition_location(self, acquisition_country):
        self.acquisition_country = acquisition_country

    def get_reserved(self):
        return self.reserved

    def set_reserved(self, reserved):
        self.reserved = reserved

    def get_in_service_location(self):
        return self.in_service_country

    def set_in_service_country(self, in_service_country):
        self.in_service_country = in_service_country

    def get_training_status(self):
        return self.training_status

    def set_training_status(self, training_status):
        self.training_status = training_status