########################################################################################################################
#                                         Grazioso Salvare Animal Rescue System                                        #
#                                                                                                                      #
# This module defines the Dog class, which inherits from the RescueAnimal class. It is used to represent a dog         #
# within the Grazioso Salvare Dog and Monkey database project. The Dog class includes attributes specific to dogs,     #
# such as breed, and inherits common attributes and methods from the RescueAnimal base class.                          #
#                                                                                                                      #
# Author: Richard VanSkike                                                                                             #
# Revision: 1.0                                                                                                        #
# Course: CS-499 Computer Science Capstone                                                                             #
# Source: IT-145 Foundation in Application Development                                                                 #
# College: Southern New Hampshire University                                                                           #
#                                                                                                                      #
# Dependencies: rescue_animal (custom module)                                                                          #
#                                                                                                                      #
# Class:                                                                                                               #
#     Dog - Inherits from the RescueAnimal class and represents a dog with attributes like breed, gender, age,         #
#           weight, acquisition date, acquisition country, training status, reserved status, and in-service country.   #
#                                                                                                                      #
# Methods:                                                                                                             #
#     __init__() - Constructor method to initialize a Dog object with the provided attributes.                         #
#     breed() - Property to get and set the breed of the dog.                                                          #
#                                                                                                                      #
# Usage:                                                                                                               #
#     This module is used by other parts of the application to create, manage, and retrieve information about dogs     #
#     in the Grazioso Salvare Animal Rescue System.                                                                    #
########################################################################################################################
from rescue_animal import RescueAnimal # Import RescueAnimal class from rescue_animal.py

class Dog(RescueAnimal):
    # Constructor method to establish structure for Dog inheriting it from rescue_animal.
    def __init__(self, name, breed, gender, age, weight, acquisition_date, acquisition_country, training_status, reserved, in_service_country):
        super().__init__(name, gender, age, weight, acquisition_date, acquisition_country, training_status, reserved, in_service_country)
        self.name = name
        self.breed = breed
        self.gender = gender
        self.age = age
        self.weight = weight
        self.acquisition_date = acquisition_date
        self.acquisition_country = acquisition_country
        self.training_status = training_status
        self.reserved = reserved
        self.in_service_country = in_service_country

    # Property for breed
    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value):
        self._breed = value