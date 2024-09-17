# Grazioso Salvare Animal Rescue Database

This project is designed to manage animal rescue data for Grazioso Salvare, an animal rescue organization. The system helps track rescue animals (dogs and monkeys), including their acquisition, training status, reservation, and service country. It features an organized structure for handling dogs and monkeys, utilizing OOP principles and Python's class inheritance.

## Project Structure

The project contains the following modules:

### 1. driver.py
`driver.py` is the central module for managing the integration of various components within the Grazioso Salvare Animal Rescue database application. It serves as the entry point for initializing the application, handling user inputs, and coordinating the interaction between different modules, such as adding new animals, listing animals, and managing reservations

#### Functionality

The main responsibilities of `driver.py` include:

- **Initialization:** Setting up and populating the `dog_list` and `monkey_list` with existing data or preparing them for new entries.
- **User Interaction:** Providing a menu-driven interface for the user to select various operations, such as adding new dogs or monkeys, listing animals, and reserving animals.
- **Data Management:** Calling functions from other modules (`intake.py`, `print_animals.py`, `reserve_animal.py`) to perform specific tasks based on user input.

#### Components
- `main()`: The main function that drives the application. It displays a menu, handles user choices, and invokes appropriate functions for each action.
- #### Menu Options:
    - **Add New Dog:** Calls `intake_new_dog()` from `intake.py` to add a new dog to the `dog_list`.
    - **Add New Monkey:** Calls `intake_new_monkey()` from `intake.py` to add a new monkey to the `monkey_list`.
    - **Reserve an Animal:** Calls `reserve_animal()` from `reserve_animal.py` to reserve a dog or monkey based on user input.
    - **List All Dogs:** Calls `print_animals()` from `print_animals.py` to display all dogs.
    - **List All Monkeys:** Calls `print_animals()` from `print_animals.py` to display all monkeys.
    - **Get Available Animals:** Calls `print_animals()` from `print_animals.py` to list available dogs and monkeys.

----
### 2. `initialize.py`
`initialize.py` is responsible for setting up the populating of the database information for the Grazioso Salvare Animal Rescue database application.

#### Functionality

The main responsibility of `initialize.py` include:

- **Initialization:** Populating the `dog_list` and `monkey_list` with existing data.

#### Components
- `initialize_dog_list()`: The function that drives the populating of the database information for the Grazioso Salvare Animal Rescue database application for the `dog_list`.
- `initialize_monkey_list()`: The function that drives the populating of the database information for the Grazioso Salvare Animal Rescue database application for the `monkey_list`.
----
### 3. rescue_animal.py
`rescue_animal.py` defines the `RescueAnimal` class, which serves as the base class for all rescued animals. It includes the following attributes:

- `name`
- `gender`
- `age`
- `weight`
- `acquistion_date`
- `acquistion_country`
- `training_status`
- `reserved`
- `in_service_country`
  
This class also provides getter and setter methods for each of the attributes.

----
### 4. dog.py
`dog.py` defines the `Dog` class, which inherits from `RescueAnimal`. The `Dog` class adds a `breed` attribute and has corresponding getter and setter methods. It uses the `super()` function to call the `RescueAnimal` constructor for common attributes.

----
### 5. monkey.py
`monkey.py` is similar to the `Dog` class, the `Monkey` class inherits from `RescueAnimal`. It adds additional attributes specific to monkeys:

- `species`
- `tail_length`
- `height`
- `body_length`
- `torso_length`
- `skull_length`
- `neck_length`

Each of these attributes has getter and setter methods, allowing you to interact with the data appropriately.

----
### 6. intake.py
`intake.py` contains functions to intake new dogs and monkeys into their respective lists. It gathers user input for all required attributes, validates some fields (e.g., checks if the animal already exists), and appends the new animal to the provided list.

- `intake_new_dog()`: Adds a new dog to the `dog_list` based on user input.
- `intake_new_monkey()`: Adds a new monkey to the `monkey_list`, ensuring the species is allowed.

----
### 7. reserve_animal.py
`reserve_animal.py` defines the `reserve_animal` function, which handles the reservation of animals based on user input:

- **Animal Type**: The user can choose between reserving a Dog or a Monkey.
- **In-Service Country**: The function takes the service country as input to find animals available for reservation in that country.
- If an animal is available and not already reserved, the user is given the option to reserve it.
- If no animals are available or already reserved, the user is notified accordingly.

The module uses a simple reservation system, updating the `reserved` status for the animal when the user confirms the reservation.

----
### 8. print_animals.py
`print_animals.py` defines the `print_animals` function, which prints animal details based on the user's choice:

- **Choice 1**: Lists all dogs in the system with details like breed, gender, age, and training status.
- **Choice 2**: Lists all monkeys in the system, including attributes like species, height, body length, and skull length.
- **Choice 3**: Retrieves available animals (both dogs and monkeys) that are in service and not reserved.
  
Each output is clearly formatted for readability, with separator lines between entries for better visualization.

## Usage
To run the application:

1. Ensure all required modules (`initialize.py`, `rescue_animal.py`, `dog.py`, `monkey.py`, `intake.py`, `reserve_animal.py`, `print_animals.py`) are in the same directory as driver.py.
2. Execute the script from the command line:
     ```bash
     python driver.py
     ```
3. Follow the on-screen prompts to interact with the application. Choose from the menu options to add animals, list them, or reserve them.

## Future Enhancements
- **Input Validation**: Implement input validation when entering data into the database to provide consistency.
- **Search Functionality**: Implement search methods for the animals based on their attributes.
- **Database Integration**: Add persistent storage (e.g., PostgreSQL) to save animals in a database.
- **GUI Interface**: Create a simple UI using Tkinter for easier interaction.
- **Secure Login System**: Create a user database and login system to control access.
