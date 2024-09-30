#######################################################################################################################
#                                         Grazioso Salvare Animal Rescue System                                       #
#                                               Rescue Animal Dashboard                                               #
#                                                                                                                     #
# This script provides a graphical user interface (GUI) for editing information about rescue animals.                 #
# It allows users to select an animal from the dashboard and edit its details, including name, training status,       #
# reserved status, and in-service country.                                                                            #
#                                                                                                                     #
# Author: Richard VanSkike                                                                                            #
# Revision: 1.0                                                                                                       #
# Course: CS-499 Computer Science Capstone                                                                            #
# Source: Milestone 3 - Enhancement Two: Algorithms and Data Structure                                                #
# College: Southern New Hampshire University                                                                          #
#                                                                                                                     #
# Dependencies: tkinter, ttk, initialize (custom module), validation (custom module)                                  #
#                                                                                                                     #
# Classes:                                                                                                            #
#   EditGUI - Class for creating and managing the edit interface.                                                     #
#                                                                                                                     #
# Methods:                                                                                                            #
#     __init__(self, root, dashboard) - Initializes the edit interface.                                               #
#     edit_animal(self) - Determines the selected tab and item, and opens the edit window.                            #
#     open_edit_window(self, item_values, animal_type, item_id, tree) - Opens a window to edit the selected animal.   #
#     submit_edit(self, entries, animal_type, item_id, tree, window) - Validates and submits the edited data.         #
#                                                                                                                     #
# Usage:                                                                                                              #
#    This script is intended to be used as part of the Rescue Animal Dashboard application.                           #
#######################################################################################################################
import tkinter as tk                    # Import tkinter as tk to provide UI capabilties
from tkinter import ttk, messagebox     # Import ttk and messagebox from tkinter to provide UI capabilities
from initialize import Initialize       # Import Initialize from initialize.py
from validation import Validation       # Import Validation from validation.py

# Revision change from reserve_animal.py and search.py to EditGUI:
# The EditGUI class has been introduced to streamline the animal editing process by replacing 
# the functionality of both reserve_animal.py and search.py. Instead of relying on separate 
# command-line scripts, EditGUI provides a more user-friendly graphical interface for managing
# animal records within the database.
#
# The user can select an animal from either of the GUI's tabs and press the "Edit" button. This
# action opens a new window where the user is presented with options to modify key animal 
# attributes, such as name, training status, reservation status, and in-service country. 
#
# After making the desired changes, the system validates the input to ensure that all entries 
# conform to expected formats. Upon successful validation, the necessary updates are applied 
# to the database. The table displaying the animals is then refreshed to reflect the recent 
# changes, ensuring the user is always presented with the most up-to-date information.
#
# The introduction of EditGUI not only simplifies the editing process but also improves 
# the overall user experience by providing an intuitive, interactive platform for managing 
# animal data, with automatic validation and database synchronization.
class EditGUI:
    def __init__(self, root, dashboard):
        self.root = root
        self.dashboard = dashboard

    def edit_animal(self):
        # Determine which tab is currently selected
        selected_tab = self.dashboard.notebook.index(self.dashboard.notebook.select())
        if selected_tab == 0:
            tree = self.dashboard.dogs_tree
            animal_type = 'Dog'
        else:
            tree = self.dashboard.monkeys_tree
            animal_type = 'Monkey'

        # Get the selected item in the Treeview
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showerror("Selection Error", "Please select an item to edit.")
            return

        # Get the values of the selected item
        item_values = tree.item(selected_item, "values")
        self.open_edit_window(item_values, animal_type, selected_item, tree)

    def open_edit_window(self, item_values, animal_type, item_id, tree):
        # Create a new window for editing the selected animal
        edit_window = tk.Toplevel(self.root)
        edit_window.title(f"Edit {animal_type}")

        # Define the fields to be edited and their corresponding indices
        if animal_type == 'Dog':
            fields = {
                "Name": 1,
                "Training Status": 8,
                "Reserved": 9,
                "In Service Country": 10
            }
        else:
            fields = {
                "Name": 1,
                "Training Status": 14,
                "Reserved": 15,
                "In Service Country": 16
            }

        entries = {}
        for field, index in fields.items():
            label = ttk.Label(edit_window, text=field)
            label.pack()
            entry = ttk.Entry(edit_window)
            entry.insert(0, item_values[index])
            entry.pack()
            entries[field] = entry

        # Add a submit button to save the changes
        submit_button = ttk.Button(edit_window, text="Submit", command=lambda: self.submit_edit(entries, animal_type, item_id, tree, edit_window))
        submit_button.pack(pady=10)

    def submit_edit(self, entries, animal_type, item_id, tree, window):
        # Collect data from the entries
        data = {field: entry.get() for field, entry in entries.items()}

        # Validate the data
        try:
            data["Name"] = Validation.null_validation(data["Name"].strip().title(), "name")
            data["Training Status"] = Validation.status_validation(data["Training Status"].strip().lower())
            data["Reserved"] = Validation.boolean_validation(data["Reserved"].strip().lower())
            data["In Service Country"] = Validation.null_validation(data["In Service Country"].strip().title(), "country")
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))
            return

        # Update the database with the new values
        with Initialize.conn.cursor() as cursor:
            if animal_type == 'Dog':
                cursor.execute("""
                    UPDATE Dog SET name = %s, training_status = %s, reserved = %s, in_service_country = %s WHERE id = %s
                """, (data["Name"], data["Training Status"], data["Reserved"], data["In Service Country"], int(tree.item(item_id)["values"][0])))
            else:
                cursor.execute("""
                    UPDATE Monkey SET name = %s, training_status = %s, reserved = %s, in_service_country = %s WHERE id = %s
                """, (data["Name"], data["Training Status"], data["Reserved"], data["In Service Country"], int(tree.item(item_id)["values"][0])))
            Initialize.conn.commit()

        # Refresh the Treeview
        if animal_type == 'Dog':
            self.dashboard.dogs_tree.delete(*self.dashboard.dogs_tree.get_children())
            self.dashboard.display_dogs()
        else:
            self.dashboard.monkeys_tree.delete(*self.dashboard.monkeys_tree.get_children())
            self.dashboard.display_monkeys()

        window.destroy()
        messagebox.showinfo("Success", f"{animal_type} details updated successfully!")