# Grazioso Salvare Animal Rescue Database

This project is designed to manage animal rescue data for Grazioso Salvare, an animal rescue organization. The system helps track rescue animals (dogs and monkeys), including their acquisition, training status, reservation, and service country. It features an organized structure for handling dogs and monkeys, utilizing OOP principles and Python's class inheritance.

## Project Structure

The project contains the following modules:

### 1. driver.py
`driver.py` is the central module for managing the integration of various components within the Grazioso Salvare Animal Rescue database application. It serves as the entry point for initializing the application, handling user inputs, and coordinating the interaction between different modules, such as adding new animals, listing animals, managing reservations, and searching for animals. It also includes a dedicated module to perform input validation for users.

#### Functionality

The main responsibilities of `driver.py` include:

- **Initialization:** Presenting the Dashboard and Terminal Menu after login.
    -  **Revision change from Dictionary to PostgresSQL Database:** With the need for more scalable and persistent data management, transitioning from an in-memory dictionary to a PostgreSQL database enhances both performance and data integrity. While dictionaries offer O(1) average time complexity for search operations, they are limited by memory constraints and lack persistence across sessions. A PostgreSQL database allows for efficient storage and retrieval of larger datasets without being limited by memory. Using SQL queries, we can search the database with high efficiency using indexed columns, such as animal names, ensuring that lookups remain fast even as the database grows in size. In particular, database indexing provides an O(log n) time complexity for search operations in most cases, which remains scalable for large datasets.      
    - PostgreSQL Database Search Time Complexity:
        - Search (with indexes): O(log n)
        - Search (without indexes): O(n)
        - Insertion: O(log n) with indexing
- **User Interaction:** Provides both a menu-driven terminal interface and a graphical user interface for the user to utilize various operations, such as adding new dogs or monkeys, listing animals, and reserving animals.
- **Data Management:** Calling functions from other modules (`intake.py`, `print_animals.py`, `reserve_animal.py`, `search.py`, `dashboard.py`) to perform specific tasks based on user input.

#### Components
- `login()`: The function that drives logging into the environment. It is the first prompt of the system, and will not present the GUI or Menu until authenticated.
- `main()`: The main function that drives the application. It displays a menu, handles user choices, and invokes appropriate functions for each action.
- #### Menu Options:
    - **Add New Dog:** Calls `intake_new_dog()` from `intake.py` to add a new dog to the `Dog` database.
    - **Add New Monkey:** Calls `intake_new_monkey()` from `intake.py` to add a new monkey to the `Monkey` database.
    - **Reserve an Animal:** Calls `reserve_animal()` from `reserve_animal.py` to reserve a dog or monkey based on user input.
    - **List All Dogs:** Calls `print_animals()` from `print_animals.py` to display all dogs.
    - **List All Monkeys:** Calls `print_animals()` from `print_animals.py` to display all monkeys.
    - **Get Available Animals:** Calls `print_animals()` from `print_animals.py` to list available dogs and monkeys.
    - **Search Animals and Update:** Calls `search_animal()` from `search.py` to search for an animal and edit it's name, service country, or training status.
    - **Add New User:** Calls `add_user()` from `security.py` to add a new user to the database.
    - **Display Dashboard:** Calls `Dashboard` Class from `dashboard.py` to present the GUI interface if it is accidentally closed. 

----
### 2. initialize.py
`initialize.py` is responsible for setting up the populating of the database information for the Grazioso Salvare Animal Rescue database application.

#### Functionality

The main responsibility of `initialize.py` include:

- **Initialization:** Populating the `Dog`, `Monkey`, and `Users` databases with existing data.
- **Connection:** Controls connection to the database through the `connect_db()` and `close_db()` methods.
- **Database Access:** Controls accessing data from the database with `fetch_all_dogs()`, `fetch_all_monkeys()`, and `get_user_from_db()`.

#### Components
- `connect_db()`: The function that connects to the PostgreSQL database and creates tables if they do not exist.
- `close_db()`: The function that closes the database connection.
- `create_tables()`: The function that creates the necessary tables in the database if they do not exist.
- `initialize_dog_list()`: The function that adds initial dog data to the database if the table is empty.
- `initialize_monkey_list()`: The function that adds initial monkey data to the database if the table is empty.
- `initialize_user_list()`: The function that adds initial user data to the database if the table is empty.
- `fetch_all_dogs()`: The function that fetches all dog records from the database.
- `fetch_all_monkeys()`: The function that fetches all monkey records from the database.
- `get_user_from_db()`: The function that fetches a user record from the database for login verification.
  
----
### 3. intake.py
`intake.py` contains functions to intake new dogs and monkeys into their respective database. It gathers user input for all required attributes, validates all fields (e.g., checks if the animal already exists, name is not null, etc.), and appends the new animal to the provided database.

- `intake_new_dog()`: Adds a new dog to the `Dog` database based on user input.
- `intake_new_monkey()`: Adds a new monkey to the `Monkey` database, ensuring the species is allowed.

----
### 4. reserve_animal.py
`reserve_animal.py` defines the `reserve_animal` function, which handles the reservation of animals based on user input:

- **Animal Type**: The user can choose between reserving a Dog or a Monkey.
- **In-Service Country**: The function takes the service country as input to find animals available for reservation in that country.
- If an animal is available and not already reserved, the user is given the option to reserve it.
- If no animals are available or already reserved, the user is notified accordingly.

The module uses a simple reservation system, updating the `reserved` status for the animal when the user confirms the reservation.

----
### 5. print_animals.py
`print_animals.py` defines the `print_animals` function, which prints animal details based on the user's choice:

- **Choice 1**: Lists all dogs in the system with details like breed, gender, age, and training status.
- **Choice 2**: Lists all monkeys in the system, including attributes like species, height, body length, and skull length.
- **Choice 3**: Retrieves available animals (both dogs and monkeys) that are in service and not reserved.
  
Each output is clearly formatted for readability, with separator lines between entries for better visualization.

----
### 6. search.py
`search.py` defines the `search_animal` function, which allows users to search and update the details of specific dogs or monkeys in the system.

- **Animal Search**: The function prompts the user to input the animal type (dog or monkey) and the name of the animal they wish to search for. It validates the input to ensure accuracy and returns the details if the animal is found.
- **Dog Details Update**: If the user selects a dog, the function retrieves the dog's details such as name, country of service, and training status. The user can then choose to update any of these attributes, and the function validates the changes before applying them.
- **Monkey Details Update**: Similarly, if the user selects a monkey, the function retrieves and displays its details. The user can update the monkey's name, country of service, or training status, with appropriate validation.
  
Each operation is optimized for quick lookups and updates using indexes, and input is validated to ensure proper handling of data, reducing the risk of errors or data corruption.

- **Time Complexity:** O(log n) on average for database lookups and updates when using indexing, O(n) in case of no indexing.

----
### 7. validation.py
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

----
### 8. security.py
`security.py` provides methods for managing user credentials securely within the Grazioso Salvare Animal Rescue database application. This module handles the addition of new users and the hashing and verification of passwords.

#### Functionality

The main responsibilities of `security.py` include:

- **Add User**: Processes the addition of a new user to the Users database. Prompts for a username and password, validates the inputs, hashes the password, and stores the user in the database.
- **Hash Password**: Processes plaintext passwords into hashed passwords using bcrypt.
- **Verify Password**: Verifies plaintext passwords against hashed passwords to ensure they match.

#### Components

- `add_user()`: Prompts for a new username and password, validates the inputs, hashes the password, and inserts the new user into the database.
- `hash_password()`: Hashes a plaintext password using bcrypt and returns the hashed password.
- `verify_password()`: Verifies a plaintext password against a hashed password to ensure they match.
  
----
### 9. dashboard.py
`dashboard.py` is the main user interface module for the Grazioso Salvare Animal Rescue database application. It provides a graphical dashboard for managing and viewing data related to rescue animals, including dogs and monkeys. 

#### Functionality

The main responsibilities of `dashboard.py` include:

- **Initialization**: Sets up the main attributes and user interface components, including the main window, theme, and tabs for dogs and monkeys.
- **Theme Management**: Allows toggling between dark and light themes.
- **Widget Creation**: Creates and configures the main widgets, including labels, banners, and tabs.
- **Data Display**: Populates the tabs with data from the database, displaying information about dogs and monkeys in a structured format.
- **Sorting and Filtering**: Manages sorting and filtering of data within the tabs.
- **Intake and Edit Buttons**: Provides buttons for adding new animals and editing existing ones.

#### Components

- `__init__()`: Initializes the dashboard, sets up the main window, and creates the main widgets.
- `toggle_theme()`: Toggles between dark and light themes.
- `create_widgets()`: Creates the main widgets for the dashboard, including labels, banners, and tabs.
- `create_treeview()`: Creates a Treeview widget for displaying data in a tab.
- `display_dogs()`: Populates the Dogs tab with data from the database.
- `display_monkeys()`: Populates the Monkeys tab with data from the database.
- `add_intake_buttons()`: Adds buttons for adding new animals to the tabs.
- `add_edit_buttons()`: Adds buttons for editing existing animals in the tabs.

----
### 10. intake_gui.py
`intake_gui.py` provides the graphical user interface for the intake of new animals into the Grazioso Salvare Animal Rescue database. This module handles the creation of new windows for entering data about dogs and monkeys, validates the input, and inserts the new records into the database.

#### Functionality

The main responsibilities of `intake_gui.py` include:

- **Initialization**: Sets up the main attributes and links the dashboard to the intake GUI.
- **Intake New Dog**: Opens a new window for entering data about a new dog, validates the input, and inserts the new dog into the database.
- **Intake New Monkey**: Opens a new window for entering data about a new monkey, validates the input, and inserts the new monkey into the database.

#### Components

- `__init__()`: Initializes the intake GUI with the main window and dashboard reference.
- `intake_new_dog()`: Creates a new window for dog intake, adds input fields and a submit button.
- `submit_new_dog()`: Collects and validates data from the input fields, inserts the new dog into the database, and refreshes the Dogs Treeview.
- `intake_new_monkey()`: Creates a new window for monkey intake, adds input fields and a submit button.
- `submit_new_monkey()`: Collects and validates data from the input fields, inserts the new monkey into the database, and refreshes the Monkeys Treeview.

----
### 11. edit_gui.py
`edit_gui.py` provides the graphical user interface for editing existing animal records in the Grazioso Salvare Animal Rescue database. This module handles the creation of new windows for editing data about dogs and monkeys, validates the input, and updates the records in the database.

#### Functionality

The main responsibilities of `edit_gui.py` include:

- **Initialization**: Sets up the main attributes and links the dashboard to the edit GUI.
- **Edit Animal**: Determines which tab is currently selected, retrieves the selected item, and opens a new window for editing the selected animal.
- **Open Edit Window**: Creates a new window for editing the selected animal, adds input fields pre-filled with the current values, and a submit button.
- **Submit Edit**: Collects and validates data from the input fields, updates the animal record in the database, and refreshes the Treeview.

#### Components

- `__init__()`: Initializes the edit GUI with the main window and dashboard reference.
- `edit_animal()`: Determines the selected tab and item, and opens the edit window.
- `open_edit_window()`: Creates a new window for editing the selected animal, adds input fields and a submit button.
- `submit_edit()`: Collects and validates data from the input fields, updates the animal record in the database, and refreshes the Treeview.

----
### 12. sort_filter.py
`sort_filter.py` provides methods for sorting and filtering data within the Grazioso Salvare Animal Rescue database application. This module handles the sorting of data in Treeview widgets and the creation and application of filters for specific columns.

#### Functionality

The main responsibilities of `sort_filter.py` include:

- **Sort Data**: Sorts data in a Treeview widget based on a specified column and tab.
- **Create Filters**: Creates dropdown menus and apply buttons for filtering data in specific columns.
- **Apply Filter**: Applies the selected filter to the data in the Treeview widget.

#### Components

- `__init__()`: Initializes the sort and filter manager with dictionaries for sort order, filters, and detached items.
- `sort_data()`: Sorts data in the specified Treeview widget based on the selected column and tab.
- `create_filters()`: Creates dropdown menus and apply buttons for filtering data in the specified columns.
- `get_unique_values()`: Retrieves unique values from a specified column in the Treeview widget for filtering.
- `apply_filter()`: Applies the selected filter to the data in the Treeview widget.

## Usage
To run the application:

1. Ensure all required modules (`initialize.py`, `intake.py`, `reserve_animal.py`, `print_animals.py`, `search.py`, `validation.py`, `dashboard.py`, `security.py`, `intake_gui.py`, `edit_gui.py`, `sort_filter.py`) are in the same directory as driver.py.
2. Edit the `initialize.py` file to add your local database information:
     ```bash
     dbname="DATABASE", user="USERNAME", password="PASSWORD", host="HOST"  
     ```
4. If **necessary** remove the first `#` from lines 99, 100, and 101 in `driver.py` to perform initial population of databases.
     ```bash
     # Initialize.initialize_dog_list()
     # Initialize.initialize_monkey_list()
     # Initialize.initialize_user_list()  
     ```
     - **NOTE:** Remember to either remove or comment these back out after first run, or it will repeatedly add these entries to the databases.
6. Execute the script from the command line:
     ```bash
     python driver.py
     ```
7. Utilize the GUI to access the database, or follow the on-screen prompts to interact with the application.

## Future Enhancements
- **Rolebased Access Control**: Allow access to certain functions based off user role.
- **Account Remove / Update**: Allow deletion of users from database and allow to update password.
- **Animal Deletion:** Allow users to delete animals from their respective databases.

