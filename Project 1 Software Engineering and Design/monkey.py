#########################################################################################################################
#                                         Grazioso Salvare Animal Rescue System                                         #
#                                                                                                                       #
# This script defines the `Monkey` class, which inherits from the `RescueAnimal` class and represents                   #
# a specialized type of rescue animal with additional attributes unique to monkeys, such as species,                    #
# tail length, height, and various body measurements. The class provides property getters and setters                   #
# for these attributes, allowing for detailed management of monkey-specific data within the Grazioso Salvare            #
# Dog and Monkey database.                                                                                              #
#                                                                                                                       #
# Author: Richard VanSkike                                                                                              #
# Revision: 1.0                                                                                                         #
# Course: CS-499 Computer Science Capstone                                                                              #
# Source: IT-145 Foundation in Application Development                                                                  #
# College: Southern New Hampshire University                                                                            #
#                                                                                                                       #
# Dependencies: rescue_animal (custom module)                                                                           #
#                                                                                                                       #
# Classes:                                                                                                              #
#     Monkey - A class representing a monkey, extending the RescueAnimal class, with additional                         #
#              attributes and methods specific to monkeys.                                                              #
#                                                                                                                       #
# Methods:                                                                                                              #
#     __init__(self, name, species, gender, age, weight, tail_length, height, body_length, torso_length, skull_length,  #
#              neck_length, acquisition_date, acquisition_country, training_status, reserved, in_service_country)       #
#              - Initializes a new instance of the Monkey class with the specified attributes.                          #
#     species - Property for getting and setting the species of the monkey.                                             #
#     tail_length - Property for getting and setting the tail length of the monkey.                                     #
#     height - Property for getting and setting the height of the monkey.                                               #
#     body_length - Property for getting and setting the body length of the monkey.                                     #
#     torso_length - Property for getting and setting the torso length of the monkey.                                   #
#     skull_length - Property for getting and setting the skull length of the monkey.                                   #
#     neck_length - Property for getting and setting the neck length of the monkey.                                     #
#                                                                                                                       #
# Usage:                                                                                                                #
#    Create instances of the Monkey class to manage monkey-specific data within the Grazioso Salvare                    #
#    Dog and Monkey database, utilizing the inherited and additional attributes and methods provided.                   #
#########################################################################################################################
from rescue_animal import RescueAnimal # Import RescueAnimal class from rescue_animal.py

class Monkey(RescueAnimal):
    # Constructor method to establish structure for Monkey inheriting it from rescue_animal.
    def __init__(self, name, species, gender, age, weight, tail_length, height, body_length, torso_length, skull_length, neck_length, acquisition_date, acquisition_country, training_status, reserved, in_service_country):
        super().__init__(name, gender, age, weight, acquisition_date, acquisition_country, training_status, reserved, in_service_country)
        self.name = name
        self.species = species
        self.gender = gender
        self.age = age
        self.weight = weight
        self.tail_length = tail_length
        self.height = height
        self.body_length = body_length
        self.torso_length = torso_length
        self.skull_length = skull_length
        self.neck_length = neck_length
        self.acquisition_date = acquisition_date
        self.acquisition_country = acquisition_country
        self.training_status = training_status
        self.reserved = reserved
        self.in_service_country = in_service_country
        

    # Property for species
    @property
    def species(self):
        return self._species

    @species.setter
    def species(self, value):
        self._species = value

    # Property for tail length
    @property
    def tail_length(self):
        return self._tail_length

    @tail_length.setter
    def tail_length(self, value):
        self._tail_length = value

    # Property for height
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    # Property for body length
    @property
    def body_length(self):
        return self._body_length

    @body_length.setter
    def body_length(self, value):
        self._body_length = value

    # Property for torso length
    @property
    def torso_length(self):
        return self._torso_length

    @torso_length.setter
    def torso_length(self, value):
        self._torso_length = value

    # Property for skull length
    @property
    def skull_length(self):
        return self._skull_length

    @skull_length.setter
    def skull_length(self, value):
        self._skull_length = value

    # Property for neck length
    @property
    def neck_length(self):
        return self._neck_length

    @neck_length.setter
    def neck_length(self, value):
        self._neck_length = value

    @tail_length.setter
    def tail_length(self, value):
        self._tail_length = value

    # Property for height
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    # Property for body length
    @property
    def body_length(self):
        return self._body_length

    @body_length.setter
    def body_length(self, value):
        self._body_length = value

    # Property for torso length
    @property
    def torso_length(self):
        return self._torso_length

    @torso_length.setter
    def torso_length(self, value):
        self._torso_length = value

    # Property for skull length
    @property
    def skull_length(self):
        return self._skull_length

    @skull_length.setter
    def skull_length(self, value):
        self._skull_length = value

    # Property for neck length
    @property
    def neck_length(self):
        return self._neck_length

    @neck_length.setter
    def neck_length(self, value):
        self._neck_length = value

