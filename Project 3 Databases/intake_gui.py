#######################################################################################################################
#                                         Grazioso Salvare Animal Rescue System                                       #
#                                               Rescue Animal Dashboard                                               #
#                                                                                                                     #
# This script provides a graphical user interface (GUI) for adding new rescue animals to the database.                #
# It allows users to input details for new dogs and monkeys through a user-friendly interface, with validation        #
# to ensure data integrity.                                                                                           #
#                                                                                                                     #
# Author: Richard VanSkike                                                                                            #
# Revision: 1.0                                                                                                       #
# Course: CS-499 Computer Science Capstone                                                                            #
# Source: Milestone 3 - Enhancement Two: Algorithms and Data Structure                                                #
# College: Southern New Hampshire University                                                                          #
#                                                                                                                     #
# Dependencies: tkinter, ttk, intake (custom module), validation (custom module)                                      #
#                                                                                                                     #
# Classes:                                                                                                            #
#   IntakeGUI - Class for creating and managing the intake interface.                                                 #
#                                                                                                                     #
# Methods:                                                                                                            #
#     __init__(self, root, dashboard) - Initializes the intake interface.                                             #
#     intake_new_dog(self) - Opens a window to input details for a new dog.                                           #
#     submit_new_dog(self, entries, window) - Validates and submits the new dog data.                                 #
#     intake_new_monkey(self) - Opens a window to input details for a new monkey.                                     #
#     submit_new_monkey(self, entries, window) - Validates and submits the new monkey data.                           #
#                                                                                                                     #
# Usage:                                                                                                              #
#    This script is intended to be used as part of the Rescue Animal Dashboard application.                           #
#######################################################################################################################
import tkinter as tk                    # Import tkinter as tk to provide UI capabilties
from tkinter import ttk, messagebox     # Import ttk and messagebox from tkinter to provide UI capabilities
from initialize import Initialize       # Import Initialize from initialize.py
from validation import Validation       # Import Validation from validation.py


# Revision change introducing IntakeGUI:
# The IntakeGUI class has been introduced to replace the terminal-based menu intake method 
# for the dashboard, providing a more intuitive and user-friendly interface for adding 
# new animals to the system.
#
# IntakeGUI presents a new window where users can input the required fields for an animal's 
# information. Once the user fills in the data and presses "Submit," the submit method is 
# invoked to handle the intake process.
#
# The submit method validates each input by checking it against its corresponding validation 
# rules. If any of the inputs fail validation, the user is informed about the specific errors 
# and prompted to correct them. Once all inputs pass validation, the new animal is added to 
# the database.
#
# After successfully adding the animal, the system refreshes the displayed list of animals to 
# reflect the newly added entry and closes the intake window, ensuring the user can continue 
# working with the most up-to-date data in the application.
#
# IntakeGUI enhances the overall workflow by providing an efficient, interactive, and 
# error-resistant intake process, making it easier for users to input new animal data 
# and reducing the likelihood of incorrect entries.
class IntakeGUI:
    def __init__(self, root, dashboard):
        self.root = root
        self.dashboard = dashboard

    def intake_new_dog(self):
        # Create a new window for dog intake
        intake_window = tk.Toplevel(self.root)
        intake_window.title("Intake New Dog")

        # Add input fields and labels
        fields = ["Name", "Breed", "Gender", "Age", "Weight", "Acquisition Date", "Acquisition Country", "Training Status", "Reserved", "In Service Country"]
        entries = {}
        for field in fields:
            label = ttk.Label(intake_window, text=field)
            label.pack()
            entry = ttk.Entry(intake_window)
            entry.pack()
            entries[field] = entry

        # Add submit button
        submit_button = ttk.Button(intake_window, text="Submit", command=lambda: self.submit_new_dog(entries, intake_window))
        submit_button.pack(pady=10)

    def submit_new_dog(self, entries, window):
        # Collect data from entries
        data = {field: entry.get() for field, entry in entries.items()}

        # Validate data
        try:
            data["Name"] = Validation.null_validation(data["Name"].strip().title(), "name")
            data["Breed"] = Validation.null_validation(data["Breed"].strip().title(), "breed")
            data["Gender"] = Validation.gender_validation(data["Gender"].strip().lower())
            data["Age"] = Validation.positive_digit_validation(data["Age"].strip(), "age")
            data["Weight"] = Validation.float_validation(data["Weight"].strip(), "weight")
            data["Acquisition Date"] = Validation.date_validation(data["Acquisition Date"].strip())
            data["Acquisition Country"] = Validation.null_validation(data["Acquisition Country"].strip().title(), "country")
            data["Training Status"] = Validation.status_validation(data["Training Status"].strip().lower())
            data["Reserved"] = Validation.boolean_validation(data["Reserved"].strip().lower())
            data["In Service Country"] = Validation.null_validation(data["In Service Country"].strip().title(), "country")
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))
            return

        # Insert the new Dog object into the database
        with Initialize.conn.cursor() as cursor:
            cursor.execute("""
                INSERT INTO Dog (name, breed, gender, age, weight, acquisition_date, acquisition_country, training_status, reserved, in_service_country)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (data["Name"], data["Breed"], data["Gender"], data["Age"], data["Weight"], data["Acquisition Date"], data["Acquisition Country"], data["Training Status"], data["Reserved"], data["In Service Country"]))
            Initialize.conn.commit()

        # Refresh the Dogs Treeview
        self.dashboard.dogs_tree.delete(*self.dashboard.dogs_tree.get_children())
        self.dashboard.display_dogs()

        # Close the intake window
        window.destroy()
        messagebox.showinfo("Success", f"{data["Name"]} has been added successfully!")

    def intake_new_monkey(self):
        # Create a new window for monkey intake
        intake_window = tk.Toplevel(self.root)
        intake_window.title("Intake New Monkey")

        # Add input fields and labels
        fields = ["Name", "Species", "Gender", "Age", "Weight", "Tail Length", "Height", "Body Length", "Torso Length", "Skull Length", "Neck Length", "Acquisition Date", "Acquisition Country", "Training Status", "Reserved", "In Service Country"]
        entries = {}
        for field in fields:
            label = ttk.Label(intake_window, text=field)
            label.pack()
            entry = ttk.Entry(intake_window)
            entry.pack()
            entries[field] = entry

        # Add submit button
        submit_button = ttk.Button(intake_window, text="Submit", command=lambda: self.submit_new_monkey(entries, intake_window))
        submit_button.pack(pady=10)

    def submit_new_monkey(self, entries, window):
        # Collect data from entries
        data = {field: entry.get() for field, entry in entries.items()}

        # Validate data
        try:
            data["Name"] = Validation.null_validation(data["Name"].strip().title(), "name")
            data["Species"] = Validation.species_validation(data["Species"].strip().title())
            data["Gender"] = Validation.gender_validation(data["Gender"].strip().lower())
            data["Age"] = Validation.positive_digit_validation(data["Age"].strip(), "age")
            data["Weight"] = Validation.float_validation(data["Weight"].strip(), "weight")
            data["Tail Length"] = Validation.positive_digit_validation(data["Tail Length"].strip(), "tail length")
            data["Height"] = Validation.positive_digit_validation(data["Height"].strip(), "height")
            data["Body Length"] = Validation.positive_digit_validation(data["Body Length"].strip(), "body length")
            data["Torso Length"] = Validation.positive_digit_validation(data["Torso Length"].strip(), "torso length")
            data["Skull Length"] = Validation.positive_digit_validation(data["Skull Length"].strip(), "skull length")
            data["Neck Length"] = Validation.positive_digit_validation(data["Neck Length"].strip(), "neck length")
            data["Acquisition Date"] = Validation.date_validation(data["Acquisition Date"].strip())
            data["Acquisition Country"] = Validation.null_validation(data["Acquisition Country"].strip().title(), "country")
            data["Training Status"] = Validation.status_validation(data["Training Status"].strip().lower())
            data["Reserved"] = Validation.boolean_validation(data["Reserved"].strip().lower())
            data["In Service Country"] = Validation.null_validation(data["In Service Country"].strip().title(), "country")
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))
            return

        # Insert the new Monkey object into the database
        with Initialize.conn.cursor() as cursor:
            cursor.execute("""
                INSERT INTO Monkey (name, species, gender, age, weight, tail_length, height, body_length, 
                                    torso_length, skull_length, neck_length, acquisition_date, acquisition_country, 
                                    training_status, reserved, in_service_country)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (data["Name"], data["Species"], data["Gender"], data["Age"], data["Weight"], data["Tail Length"], data["Height"], data["Body Length"], 
                data["Torso Length"], data["Skull Length"], data["Neck Length"], data["Acquisition Date"], data["Acquisition Country"], 
                data["Training Status"], data["Reserved"], data["In Service Country"]))
            Initialize.conn.commit()

        # Refresh the Monkeys Treeview
        self.dashboard.monkeys_tree.delete(*self.dashboard.monkeys_tree.get_children())
        self.dashboard.display_monkeys()

        # Close the intake window
        window.destroy()
        messagebox.showinfo("Success", f"{data["Name"]} has been added successfully!")