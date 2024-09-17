# Grazioso Salvare Animal Rescue Database

This project is designed to manage animal rescue data for Grazioso Salvare, an animal rescue organization. The system helps track rescue animals (dogs and monkeys), including their acquisition, training status, reservation, and service country. It features an organized structure for handling dogs and monkeys, utilizing OOP principles and Python's class inheritance.

## Project Structure

The project contains the following modules:

### 1. driver.py
`driver.py` is the central module for managing the integration of various components within the Grazioso Salvare Animal Rescue database application. It serves as the entry point for initializing the application, handling user inputs, and coordinating the interaction between different modules, such as adding new animals, listing animals, managing reservations, and searching for animals. It also includes a dedicated module to perform input validation for users.

#### Functionality

The main responsibilities of `driver.py` include:

- **Initialization:** Setting up and populating the `dog_dict` and `monkey_dict` with existing data or preparing them for new entries.
    -  **Revision change from List to Dictionary:** With the expected expansion of the database, transitioning from a list to a dictionary improves search efficiency. A list has O(n) time complexity for searching, where "n" represents the size of the list. This means that as the number of animals increases, searching through the list would take longer, growing linearly with the number of entries. By switching to a dictionary, which uses hash-based indexing, we achieve an O(1) average time complexity for search operations. This provides constant time lookups regardless of the number of animals in the dictionary, making it significantly faster for retrieving an animal by its name. This decision optimizes search operations, especially as the database grows, providing much more efficient performance compared to lists.
    -  Dictionary Time Complexity:
    - Search: O(1) average, O(n) worst-case (in case of hash collisions)
    - Insertion: O(1) average, O(n) worst-case (in case of hash collisions)
    - Deletion: O(1) average, O(n) worst-case (in case of hash collisions)
- **User Interaction:** Providing a menu-driven interface for the user to select various operations, such as adding new dogs or monkeys, listing animals, and reserving animals.
- **Data Management:** Calling functions from other modules (`intake.py`, `print_animals.py`, `reserve_animal.py`, `search.py`) to perform specific tasks based on user input.

#### Components
- `main()`: The main function that drives the application. It displays a menu, handles user choices, and invokes appropriate functions for each action.
- #### Menu Options:
    - **Add New Dog:** Calls `intake_new_dog()` from `intake.py` to add a new dog to the `dog_dict`.
    - **Add New Monkey:** Calls `intake_new_monkey()` from `intake.py` to add a new monkey to the `monkey_dict`.
    - **Reserve an Animal:** Calls `reserve_animal()` from `reserve_animal.py` to reserve a dog or monkey based on user input.
    - **List All Dogs:** Calls `print_animals()` from `print_animals.py` to display all dogs.
    - **List All Monkeys:** Calls `print_animals()` from `print_animals.py` to display all monkeys.
    - **Get Available Animals:** Calls `print_animals()` from `print_animals.py` to list available dogs and monkeys.
    - **Search Animals and Update:** Calls `search_animal()` from `search.py` to search for an animal and edit it's name, service country, or training status. 

----
### 2. `initialize.py`
`initialize.py` is responsible for setting up the populating of the database information for the Grazioso Salvare Animal Rescue database application.

#### Functionality

The main responsibility of `initialize.py` include:

- **Initialization:** Populating the `dog_dict` and `monkey_dict` with existing data.

#### Components
- `initialize_dog_dict()`: The function that drives the populating of the database information for the Grazioso Salvare Animal Rescue database application for the `dog_dict`.
- `initialize_monkey_dict()`: The function that drives the populating of the database information for the Grazioso Salvare Animal Rescue database application for the `monkey_dict`.
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
`intake.py` contains functions to intake new dogs and monkeys into their respective lists. It gathers user input for all required attributes, validates all fields (e.g., checks if the animal already exists, name is not null, etc.), and appends the new animal to the provided dictionary.

- `intake_new_dog()`: Adds a new dog to the `dog_dict` based on user input.
- `intake_new_monkey()`: Adds a new monkey to the `monkey_dict`, ensuring the species is allowed.

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

----
### 8. search.py
`search.py` defines the `search_animal` function, which allows users to search and update the details of specific dogs or monkeys in the system.

- **Animal Search**: The function prompts the user to input the animal type (dog or monkey) and the name of the animal they wish to search for. It validates the input to ensure accuracy and returns the details if the animal is found.
- **Dog Details Update**: If the user selects a dog, the function retrieves the dog's details such as name, country of service, and training status. The user can then choose to update any of these attributes, and the function validates the changes before applying them.
- **Monkey Details Update**: Similarly, if the user selects a monkey, the function retrieves and displays its details. The user can update the monkey's name, country of service, or training status, with appropriate validation.
  
Each operation is optimized for quick lookups and updates using dictionaries, and input is validated to ensure proper handling of data, reducing the risk of errors or data corruption.

- **Time Complexity:** O(1) on average for dictionary lookups and updates, with the worst-case scenario being O(n) in case of hash collisions.
- **Space Complexity:** O(1), as the space requirements are constant and independent of the input size, with the exception of minor variables for input/output operations.

----
### 8. validation.py
`validation.py` provides a suite of validation methods to ensure the integrity of user inputs within the Grazioso Salvare Animal Rescue database application. This module handles various types of input validation, including null values, numeric values, gender, float values, dates, status, boolean values, species, animal types, yes/no responses, and option choices.

#### Functionality

The main responsibilities of `validation.py` include:

- **Null Value Validation:** Ensures that user inputs are not empty. Prompts the user until a valid input is provided.
- **Positive Digit Validation:** Validates that a numeric input is a positive integer. Continuously prompts the user until a valid positive number is entered.
- **Gender Validation:** Confirms that the input is either 'male' or 'female'. Re-prompts if the input does not match these options.
- **Float Validation:** Ensures that numeric inputs are positive floating-point numbers. Handles input errors and prompts until a valid positive number is entered.
- **Date Validation:** Validates dates to ensure they match the format `mm-dd-yyyy`. Continues prompting the user until the correct format is provided.
- **Status Validation:** Checks that the training status is among predefined valid statuses. Converts input to a standardized format before returning.
- **Boolean Validation:** Ensures that inputs are either 'true' or 'false', converting the input to a boolean value.
- **Species Validation:** Validates that the species input matches one of the predefined monkey species. Prompts until a valid species is provided.
- **Animal Type Validation:** Ensures the input is either 'dog' or 'monkey'. Re-prompts until a valid type is entered.
- **Yes/No Validation:** Confirms that responses are either 'yes' or 'no'. Continuously prompts until a valid response is provided.
- **Option Choice Validation:** Validates that the input corresponds to one of the valid update options ('name', 'country', or 'training').

Each method is designed to provide clear prompts to the user and ensures that inputs adhere to expected formats and constraints, improving the overall reliability and usability of the application.

## Usage
To run the application:

1. Ensure all required modules (`initialize.py`, `rescue_animal.py`, `dog.py`, `monkey.py`, `intake.py`, `reserve_animal.py`, `print_animals.py`, `search.py`, `validation.py`) are in the same directory as driver.py.
2. Execute the script from the command line:
     ```bash
     python driver.py
     ```
3. Follow the on-screen prompts to interact with the application. Choose from the menu options to add animals, list them, or reserve them.

## Future Enhancements
- **Database Integration**: Add persistent storage (e.g., PostgreSQL) to save animals in a database.
- **GUI Interface**: Create a simple UI using Tkinter for easier interaction.
- **Secure Login System**: Create a user database and login system to control access.
