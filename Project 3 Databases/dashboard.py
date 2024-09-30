########################################################################################################################
#                                         Grazioso Salvare Animal Rescue System                                        #
#                                               Rescue Animal Dashboard                                                #
#                                                                                                                      #
# This script creates a graphical user interface (GUI) for managing and displaying information about rescue animals.   #
# It includes tabs for dogs and monkeys, with options to sort and filter data based on various attributes.             #
# Users can also add new animals and edit existing ones through the interface.                                         #
#                                                                                                                      #
# Author: Richard VanSkike                                                                                             #
# Revision: 1.0                                                                                                        #
# Course: CS-499 Computer Science Capstone                                                                             #
# Source: Milestone 3 - Enhancement Two: Algorithms and Data Structure                                                 #
# College: Southern New Hampshire University                                                                           #
#                                                                                                                      #
# Dependencies: tkinter, ttk, initialize (custom module), intake_gui (custom module), edit_gui (custom module)         #
#                                                                                                                      #
# Classes:                                                                                                             #
#   Dashboard - Main class for creating and managing the dashboard interface.                                          #
#                                                                                                                      #
# Methods:                                                                                                             #
#     __init__(self, root) - Initializes the dashboard.                                                                #
#     toggle_theme(self) - Toggles between light and dark theme for the dashboard.                                     #
#     create_widgets(self) - Creates the main widgets for the dashboard.                                               #
#     create_treeview(self, frame, columns, tab_name) - Creates a Treeview widget with a scrollbar.                    #
#     display_dogs(self) - Populates the Dogs tab.                                                                     #
#     display_monkeys(self) - Populates the Monkeys tab.                                                               #
#     add_intake_buttons(self) - Adds buttons to the tabs for adding new animals.                                      #
#     add_edit_buttons(self) - Adds buttons to the tabs for editing selected animals.                                  #
#                                                                                                                      #
# Usage:                                                                                                               #
#    Run this script to launch the Rescue Animal Dashboard application.                                                #
########################################################################################################################
import tkinter as tk                        # Import tkinter as tk to provide UI capabilties
from tkinter import ttk                     # Import ttk from tkinter to provide UI capabilties
import sv_ttk                               # Import sv_ttk to provide theme capabilities
import os                                   # Import os to provide filepath access
from initialize import Initialize           # Import Initialize class from initialize.py
from intake_gui import IntakeGUI            # Import IntakeGUI from intake_gui.py
from edit_gui import EditGUI                # Import EditGUI from edit_gui.py
from sort_filter import SortFilterManager   # Import SortFilterManager from sort_filter.py

# Revision change introducing the Dashboard:
# The Dashboard serves as a replacement for the terminal window, providing a GUI interface 
# for interacting with the database. This new interface improves user experience by offering 
# a visual and interactive platform for managing the database.
#
# The Dashboard opens with a main landing page that defaults to displaying the dog database. 
# Users can easily switch to the monkey database via a separate tab, allowing for seamless 
# navigation between different datasets.
#
# Key features of the Dashboard include:
#   1. Sorting: Users can sort data by any available column, enabling quick organization and 
#      retrieval of specific information.
#   2. Filtering: Users can apply filters based on training status, reservation status, and 
#      service country, making it easier to locate relevant records.
#   3. Add New Animal: Users can add a new animal to the database, with the tab selection 
#      determining whether the animal is added to the dog or monkey database.
#   4. Edit Existing Animal: Users can edit existing animal records by selecting an animal 
#      from the list, which opens the editing interface for modifications.
#
# In addition, the Dashboard includes several quality-of-life improvements:
#   1. Dark mode is enabled using a Tkinter theme, providing a visually appealing and comfortable 
#      interface.
#   2. Users can toggle between dark and light theme.
#   3. The Dashboard automatically moves to the foreground upon loading, ensuring it is always 
#      easily accessible.
#   4. The Gravioso Salvare logo is prominently displayed, adding a professional touch to the interface.
#
# The Dashboard enhances the usability and efficiency of database interactions, making it 
# easier for users to manage animal records with an intuitive and polished GUI.
class Dashboard:
    # Constructor Method to initialize the main attributes and setup the UI
    def __init__(self, root):
        self.root = root
        self.root.title("Rescue Animal Dashboard")

        # Set the window to always be on top
        self.root.lift()
        self.root.attributes('-topmost', True)

        # Reset 'topmost' attribute so that the window can behave normally after appearing
        self.root.after(1000, lambda: self.root.attributes('-topmost', False))
        
        # Set the theme to dark mode
        sv_ttk.set_theme("dark")
        
        self.sort_order = {}                            # To track sort order for each column in each tab
        self.intake_gui = IntakeGUI(root, self)         # Initialize IntakeGUI
        self.edit_gui = EditGUI(root, self)             # Initialize EditGUI
        self.sort_filter_manager = SortFilterManager()  # Initialize SortFilterManager
        self.create_widgets()                           # Create the main widgets for the dashboard

    # Method to toggle the theme
    def toggle_theme(self):
        current_theme = sv_ttk.get_theme()
        new_theme = "light" if current_theme == "dark" else "dark"
        sv_ttk.set_theme(new_theme)
    
    # Method that creates the main widgets for the dashboard
    def create_widgets(self):
        # Get the directory where the dashboard is located
        dashboard_dir = os.path.dirname(os.path.abspath(__file__))

        # Load the image
        try:
            self.image = tk.PhotoImage(file= os.path.join(dashboard_dir,"GS_Logo.png"))
        except tk.TclError as e:
            print(f"Error loading image: {e}")
            self.image = None

        # Create a label for the image and center it if the image is loaded
        if self.image:
            image_label = ttk.Label(self.root, image=self.image)
            image_label.pack(pady=10, anchor="center")

        # Create a large banner that shows the name of the database and center it
        banner = ttk.Label(self.root, text="Rescue Animal Dashboard", font=("Helvetica", 24))
        banner.pack(pady=10, anchor="center")

        # Create a notebook to put the two databases into their own tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(pady=10, expand=True)

        # Create the Dogs tab
        self.dogs_frame = ttk.Frame(self.notebook)
        self.dogs_frame.pack(fill="both", expand=True)
        self.notebook.add(self.dogs_frame, text="Dogs")

        # Create the Monkeys tab
        self.monkeys_frame = ttk.Frame(self.notebook)
        self.monkeys_frame.pack(fill="both", expand=True)
        self.notebook.add(self.monkeys_frame, text="Monkeys")

        # Initialize Treeviews
        self.dogs_tree = None
        self.monkeys_tree = None

        # Populate the Dogs tab
        self.display_dogs()

        # Populate the Monkeys tab
        self.display_monkeys()
        
        # Create filters after populating data
        self.sort_filter_manager.create_filters(self.dogs_frame, self.dogs_tree, ["Training Status", "Reserved", "Service Country"])
        self.sort_filter_manager.create_filters(self.monkeys_frame, self.monkeys_tree, ["Training Status", "Reserved", "Service Country"])

        # Add intake buttons
        self.add_intake_buttons()

        # Add edit buttons
        self.add_edit_buttons()
        
        # Add a button to toggle the theme
        theme_button = ttk.Button(self.root, text="Toggle Theme", command=self.toggle_theme)
        theme_button.pack(anchor="ne", padx=10, pady=10)

    # Method to create the table that displays data from Dog and Monkey
    def create_treeview(self, frame, columns, tab_name):
        # Create a Treeview widget with a scrollbar
        tree_frame = ttk.Frame(frame)
        tree_frame.pack(fill="both", expand=True)

        tree_scroll = ttk.Scrollbar(tree_frame)
        tree_scroll.pack(side=tk.RIGHT, fill=tk.Y)
           
        # Set up columns with headers for sorting
        tree = ttk.Treeview(tree_frame, columns=columns, show="headings", yscrollcommand=tree_scroll.set)
        tree.pack(fill="both", expand=True)
        tree_scroll.config(command=tree.yview)
        
        for col in columns:
            tree.heading(col, text=col, command=lambda _col=col, _tab=tab_name, _tree=tree: self.sort_filter_manager.sort_data(_tree, _col, _tab))
            tree.column(col, anchor=tk.W, width=100)
        
        self.sort_order[tab_name] = {col: None for col in columns}  # Initialize sort order for columns

        return tree
        
    # Method that populates the Dog tab
    def display_dogs(self):
        # Establish Column header titles
        columns = ("ID", "Name", "Breed", "Gender", "Age", "Weight", "Acquisition Date", "Acquisition Country", "Training Status", "Reserved", "Service Country")
        if self.dogs_tree is None:
            self.dogs_tree = self.create_treeview(self.dogs_frame, columns, "dogs")
        else:
            self.dogs_tree.delete(*self.dogs_tree.get_children())

        # Pull Dog list from database, iterate through dogs and display
        dogs = Initialize.fetch_all_dogs()
        for dog in dogs:
            self.dogs_tree.insert("", "end", values=(dog[0], dog[1], dog[2], dog[3], dog[4], dog[5], dog[6], dog[7], dog[8], dog[9], dog[10]))

        # Hide the ID column
        self.dogs_tree.column("ID", width=0, stretch=tk.NO)
        self.dogs_tree.heading("ID", text="")

    # Method that populates the Monkey tab
    def display_monkeys(self):
        # Establish Column header titles
        columns = ("ID", "Name", "Species", "Gender", "Age", "Weight", "Tail Length", "Height", "Body Length", "Torso Length", "Skull Length", "Neck Length", 
                   "Acquisition Date", "Acquisition Country", "Training Status", "Reserved", "Service Country")
        if self.monkeys_tree is None:
            self.monkeys_tree = self.create_treeview(self.monkeys_frame, columns, "monkeys")
        else:
            self.monkeys_tree.delete(*self.monkeys_tree.get_children())

        # Pull Monkey list from database, iterate through monkeys and display
        monkeys = Initialize.fetch_all_monkeys()
        for monkey in monkeys:
            self.monkeys_tree.insert("", "end", values=(monkey[0], monkey[1], monkey[2], monkey[3], monkey[4], monkey[5], monkey[6], monkey[7], monkey[8], monkey[9], monkey[10], monkey[11], monkey[12], monkey[13], monkey[14], monkey[15], monkey[16]))

        # Hide the ID column
        self.monkeys_tree.column("ID", width=0, stretch=tk.NO)
        self.monkeys_tree.heading("ID", text="")

    # Method to add intake buttons to the tabs
    def add_intake_buttons(self):
        # Add button to Dogs tab
        add_dog_button = ttk.Button(self.dogs_frame, text="Add New Dog", command=self.intake_gui.intake_new_dog)
        add_dog_button.pack(pady=10)

        # Add button to Monkeys tab
        add_monkey_button = ttk.Button(self.monkeys_frame, text="Add New Monkey", command=self.intake_gui.intake_new_monkey)
        add_monkey_button.pack(pady=10)

    # Method to add edit buttons to the tabs
    def add_edit_buttons(self):
        # Add button to Dogs tab
        edit_dog_button = ttk.Button(self.dogs_frame, text="Edit Selected Dog", command=self.edit_gui.edit_animal)
        edit_dog_button.pack(pady=10)

        # Add button to Monkeys tab
        edit_monkey_button = ttk.Button(self.monkeys_frame, text="Edit Selected Monkey", command=self.edit_gui.edit_animal)
        edit_monkey_button.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()               # Create the main window
    dashboard = Dashboard(root)  # Initialize the Dashboard class
    root.mainloop()              # Start the Tkinter event loop