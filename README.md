# SNHU CS499 Computer Science Capstone Project Repository

## Grazioso Salvare Animal Rescue Database
This project is designed to manage animal rescue data for Grazioso Salvare, an animal rescue organization. The system helps track rescue animals (dogs and monkeys), including their acquisition, training status, reservation, and service country. It features an organized structure for handling dogs and monkeys, utilizing OOP principles and Python’s class inheritance.

### Summary of Enhancements
----
#### Enhancement One
**Overview:**

- **Objective:** Transition from Java to Python Programming languages to manage animal rescue data using a structured system.
  - **Key Features:**
    - **Modules:** Includes `driver.py`, `initialize.py`, `rescue_animal.py`, `dog.py`, `monkey.py`, `intake.py`, `reserve_animal.py`, and `print_animals.py`.
    - **Functionality:** Handles user inputs, manages data, and provides a menu-driven interface for operations like adding, listing, and reserving animals.
    - **Future Enhancements:** Input validation, search functionality, database integration, GUI interface, and secure login system.

For more details, refer to the Enhancement One [README](https://github.com/rVanskike/CS-499_Comp_Sci_Capstone/blob/main/Project%201%20Software%20Engineering%20and%20Design/README.md "Enhancement One Readme.md").

----

#### Enhancement Two
**Overview:**

- **Objective:** Change data structure from lists to dictionaries, improve search efficiency, and add input validation.
  - **Key Features:**
    - **Modules:** Adds `search.py` and `validation.py` to the existing modules.
    - **Functionality:** Transitions from list to dictionary for better search efficiency, adds input validation, and includes search and update functionalities.
    - **Future Enhancements:** Database integration, GUI interface, and secure login system.

For more details, refer to the Enhancement Two [README](https://github.com/rVanskike/CS-499_Comp_Sci_Capstone/blob/main/Project%202%20Algorithms%20and%20Data%20Structures/README.md "Enhancement Two Readme.md").

----

#### Enhancement Three
**Overview:**

- **Objective:** Enhance scalability and data persistence with PostgreSQL, and introduce secure login system.
  - **Key Features:**
    - **Modules:** Adds `security.py`, `dashboard.py`, `intake_gui.py`, `edit_gui.py`, and `sort_filter.py`. Removes `rescue_animal.py`, `dog.py`, and `monkey.py`.
    - **Functionality:** Transitions from dictionary to PostgreSQL database, adds GUI, and includes user authentication.
    - **Future Enhancements:** Role-based access control, account management, and animal deletion.

For more details, refer to the Enhancement Three [README](https://github.com/rVanskike/CS-499_Comp_Sci_Capstone/blob/main/Project%203%20Databases/README.md "Enhancement One Readme.md").

----

#### Usage
**To run the application:**

1. Ensure all required modules are in the same directory as driver.py.
2. Execute the script from the command line:
```bash
python driver.py
```
3. Follow the on-screen prompts to interact with the application.
