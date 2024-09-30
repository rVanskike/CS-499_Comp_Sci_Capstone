########################################################################################################################
#                                         Grazioso Salvare Animal Rescue System                                        #
#                                               Rescue Animal Dashboard                                                #
#                                                                                                                      #
# This script provides the ability to sort and filter the  graphical user interface (GUI).                             #
# It allows users to utilize the sort and filter features from the dashboard.                                          #
#                                                                                                                      #
# Author: Richard VanSkike                                                                                             #
# Revision: 1.0                                                                                                        #
# Course: CS-499 Computer Science Capstone                                                                             #
# Source: Milestone 3 - Enhancement Two: Algorithms and Data Structure                                                 #
# College: Southern New Hampshire University                                                                           #
#                                                                                                                      #
# Dependencies: tkinter, ttk,                                                                                          #
#                                                                                                                      #
# Classes:                                                                                                             #
#   SortFilterManager - Main class for sorting and filtering for the dashboard interface.                              #
#                                                                                                                      #
# Methods:                                                                                                             #
#     __init__(self, root) - Initializes the needed dictionaries.                                                      #
#     sort_data(self, tab, column) - Sorts the data in the Treeview based on the selected column.                      #
#     create_filters(self, frame, tree, columns) - Creates filtering options for specified columns.                    #
#     get_unique_values(self, tree, column) - Retrieves unique values from a specified column in the Treeview.         #
#     apply_filter(self, tree, column, combobox) - Filters the data in the Treeview based on the selected filter value.#
#                                                                                                                      #
# Usage:                                                                                                               #
#     This script is intended to be used as part of the Rescue Animal Dashboard application.                           #
########################################################################################################################
import tkinter as tk                        # Import tkinter as tk to provide UI capabilties
from tkinter import ttk                     # Import ttk from tkinter to provide UI capabilties

# Revision change introducing SortFilterManager:
# The SortFilterManager class has been implemented to enhance the data filtering and sorting 
# capabilities within the GUI, allowing users to easily organize and navigate through large 
# datasets. It provides both sorting and filtering functionalities directly within the interface.
#
# The `sort_data` method enables users to sort data by any selected column in either ascending 
# or descending order. When a user clicks on a column header, the method is triggered, and the 
# data is reorganized accordingly, improving the ease of data exploration.
#
# The filter functionality is divided into three dedicated methods: `create_filters`, 
# `get_unique_values`, and `apply_filters`. Each method plays a specific role in the filtering process:
#       Refer to their explanations above.
#
# By structuring the sorting and filtering processes in this way, SortFilterManager allows for 
# a more organized and efficient data management experience, giving users greater control 
# over how they view and interact with the data in the application.
class SortFilterManager:
    def __init__(self):
        self.sort_order = {}
        self.filters = {}
        self.detached_items = {}

    # Method to sort data in a Treeview
    def sort_data(self, tree, column, tab):
        if tab not in self.sort_order:
            self.sort_order[tab] = {col: None for col in tree["columns"]}

        # Get all data from the treeview
        data = [(tree.set(child, column), child) for child in tree.get_children('')]

        # Determine sort order
        if self.sort_order[tab][column] == "ascending":
            data.sort(reverse=True)
            self.sort_order[tab][column] = "descending"
        else:
            data.sort(reverse=False)
            self.sort_order[tab][column] = "ascending"

        # Rearrange items in the treeview
        for index, (val, child) in enumerate(data):
            tree.move(child, '', index)

    # Method to create filters for specific columns
    def create_filters(self, frame, tree, columns):
        # Add frame to hold filtering options
        filter_frame = ttk.Frame(frame)
        filter_frame.pack(fill="x", pady=5)

        # Create dropdown menus and apply buttons for filtering
        for col in columns:
            label = ttk.Label(filter_frame, text=col)
            label.pack(side=tk.LEFT, padx=5)
            combobox = ttk.Combobox(filter_frame, values=["All"] + self.get_unique_values(tree, col))
            combobox.current(0)
            combobox.pack(side=tk.LEFT, padx=5)
            self.filters[col] = combobox

            # Add Apply Filter button for each filter
            apply_button = ttk.Button(filter_frame, text=f"Apply {col} Filter", command=lambda col=col, combobox=combobox: self.apply_filter(tree, col, combobox))
            apply_button.pack(side=tk.LEFT, padx=5)

    # Method to get unique values for filtering from columns
    def get_unique_values(self, tree, column):
        values = set(tree.set(child, column) for child in tree.get_children(''))
        return list(values)

    # Method to actually perform filtering of the data
    def apply_filter(self, tree, column, combobox):
        filter_value = combobox.get()

        if filter_value != "All":
            for child in tree.get_children(''):
                if tree.set(child, column) != filter_value:
                    if child not in self.detached_items:
                        self.detached_items[child] = tree.item(child)
                    tree.detach(child)
        else:
            for child in self.detached_items:
                tree.reattach(child, '', 'end')
            self.detached_items.clear()

        tree.update_idletasks()