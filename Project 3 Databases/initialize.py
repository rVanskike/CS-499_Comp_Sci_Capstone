#######################################################################################################################
#                                         Grazioso Salvare Animal Rescue System                                       #
#                                                                                                                     #
# This script initializes the database connection and sets up the necessary tables for the Rescue Animal Dashboard.   #
# It includes methods to connect to the database, create tables, add initial data, and fetch data from the database.  #
#                                                                                                                     #
# Author: Richard VanSkike                                                                                            #
# Revision: 3.0                                                                                                       #
# Course: CS-499 Computer Science Capstone                                                                            #
# Source: Milestone 3 - Enhancement Two: Algorithms and Data Structure                                                #
# College: Southern New Hampshire University                                                                          #
#                                                                                                                     #
# Dependencies: psycopg2 (PostgreSQL adapter for Python)                                                              #
#                                                                                                                     #
# Classes:                                                                                                            #
#   Initialize - Class for handling database initialization and operations.                                           #
#                                                                                                                     #
# Methods:                                                                                                            #
#     connect_db() - Connects to the PostgreSQL database and creates tables if they do not exist.                     #
#     close_db() - Closes the database connection.                                                                    #
#     create_tables() - Creates the necessary tables in the database if they do not exist.                            #
#     initialize_dog_list() - Adds initial dog data to the database if the table is empty.                            #
#     initialize_monkey_list() - Adds initial monkey data to the database if the table is empty.                      #
#     initialize_user_list() - Adds initial user data to the database if the table is empty.                          #
#     fetch_all_dogs() - Fetches all dog records from the database.                                                   #
#     fetch_all_monkeys() - Fetches all monkey records from the database.                                             #
#     get_user_from_db(username) - Fetches a user record from the database for login verification.                    #
#                                                                                                                     #
# Usage:                                                                                                              #
#    This script is intended to be used as part of the Rescue Animal Database application.                            #
#                                                                                                                     #
#    To connect to your local database, you must replace the parameters below at line 63.                             #
#       dbname="DATABASE", user="USERNAME", password="PASSWORD", host="HOST"                                          #
#######################################################################################################################
import psycopg2 # Import psycopg2 to manage connection to db

# Revision change introducing Initialize class refactoring:
# The Initialize class has been completely refactored to transition from an in-memory 
# database system to a remote PostgreSQL database. This change provides a persistent and 
# accessible solution for managing the dog and monkey classes, allowing for better scalability 
# and multi-user access.
#
# By utilizing PostgreSQL, the application now benefits from a reliable, long-term storage 
# solution, ensuring that data remains accessible across sessions and devices, unlike the 
# previous in-memory system that lost data upon termination of the program.
#
# Several new methods have been introduced as part of this refactoring, each designed to 
# handle specific functionalities related to database management. These methods enable 
# efficient communication with the PostgreSQL database, including data retrieval, insertion, 
# and updates for both dog and monkey records.
#
# This refactor not only enhances data persistence but also provides a more robust foundation 
# for future scalability, allowing multiple users to interact with the database concurrently 
# while maintaining data integrity.
class Initialize:
    conn = None
    
    # Method to connect to database
    @staticmethod
    def connect_db():
        try:
            Initialize.conn = psycopg2.connect(
                dbname="DATABASE", user="USERNAME", password="PASSWORD", host="HOST"
            )
            Initialize.create_tables()
        except Exception as e:
            print("Failed to connect to the database:", e)
            Initialize.conn = None

    # Method to close connection to database
    @staticmethod
    def close_db():
        if Initialize.conn:
            Initialize.conn.close()

    # Method to create tables if they do not already exist in the database
    @staticmethod
    def create_tables():
        with Initialize.conn.cursor() as cursor:
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS Dog (
                id SERIAL PRIMARY KEY,
                name VARCHAR(50),
                breed VARCHAR(50),
                gender VARCHAR(10),
                age VARCHAR(10),
                weight VARCHAR(10),
                acquisition_date VARCHAR(20),
                acquisition_country VARCHAR(50),
                training_status VARCHAR(50),
                reserved BOOLEAN,
                in_service_country VARCHAR(50)
            );
            """)
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS Monkey (
                id SERIAL PRIMARY KEY,
                name VARCHAR(50),
                species VARCHAR(50),
                gender VARCHAR(10),
                age VARCHAR(10),
                weight VARCHAR(10),
                tail_length VARCHAR(10),
                height VARCHAR(10),
                body_length VARCHAR(10),
                torso_length VARCHAR(10),
                skull_length VARCHAR(10),
                neck_length VARCHAR(10),
                acquisition_date VARCHAR(20),
                acquisition_country VARCHAR(50),
                training_status VARCHAR(50),
                reserved BOOLEAN,
                in_service_country VARCHAR(50)
            );
            """)
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS Users (
                id SERIAL PRIMARY KEY,
                username VARCHAR(50) UNIQUE NOT NULL,
                hashed_password VARCHAR(255) NOT NULL
            );
            """)
            Initialize.conn.commit()

    # Method to add dogs to database if the page is blank
    @staticmethod
    def initialize_dog_list():
        with Initialize.conn.cursor() as cursor:
            cursor.execute("""
            INSERT INTO Dog (name, breed, gender, age, weight, acquisition_date, acquisition_country, training_status, reserved, in_service_country)
            VALUES 
                ('Spot', 'German Shepherd', 'male', '1', '25.6', '05-12-2019', 'United States', 'intake', False, 'United States'),
                ('Rex', 'Great Dane', 'male', '3', '35.2', '02-03-2020', 'United States', 'in service', False, 'United States'),
                ('Bella', 'Chihuahua', 'female', '4', '25.6', '12-12-2019', 'Canada', 'in service', True, 'Canada');
            """)
            Initialize.conn.commit()

    # Method to add monkeys to database if the page is blank
    @staticmethod
    def initialize_monkey_list():
        with Initialize.conn.cursor() as cursor:
            cursor.execute("""
            INSERT INTO Monkey (name, species, gender, age, weight, tail_length, height, body_length, torso_length, skull_length, neck_length, acquisition_date, acquisition_country, training_status, reserved, in_service_country)
            VALUES 
                ('Chunky', 'Capuchin', 'male', '2', '35.6', '12', '6', '6', '1', '2', '1', '12-12-2020', 'India', 'in service', False, 'Canada'),
                ('Becky', 'Macaque', 'female', '5', '32.3', '10', '2', '3', '2', '3', '1', '01-11-2017', 'China', 'in service', True, 'Mexico');
            """)
            Initialize.conn.commit()

    # Method to add user to database if the page is blank            
    def initialize_user_list():
        if Initialize.conn is None:
            Initialize.connect_db()  # Ensure the connection is established

        if Initialize.conn:  # Proceed only if the connection is successful
            with Initialize.conn.cursor() as cursor:
                cursor.execute("""
                INSERT INTO Users (username, hashed_password)
                VALUES
                    ('admin', '$2b$12$8GGWXqOO.oGMVSHfGRoWGe/x1lsj2Dstw1qSd2mu.K.YpIRd92OWS');
                """)
                Initialize.conn.commit()

    # Method to pull list of all dogs from database
    @staticmethod
    def fetch_all_dogs():
        with Initialize.conn.cursor() as cursor:
            cursor.execute("SELECT * FROM Dog")
            dogs = cursor.fetchall()
            return dogs

    # Method to pull list of all monkeys from database
    @staticmethod
    def fetch_all_monkeys():
        with Initialize.conn.cursor() as cursor:
            cursor.execute("SELECT * FROM Monkey")
            monkeys = cursor.fetchall()
            return monkeys
            
    # Method to pull single user from database for login verification
    # Method is setup to stand along connect to the database and close 
    # the connection while user is not authenticated
    def get_user_from_db(username: str):
        Initialize.connect_db()  # Connect to the database
        if Initialize.conn is None:
            return None
        
        with Initialize.conn.cursor() as cursor:
            cursor.execute("SELECT id, username, hashed_password FROM Users WHERE username = %s", (username,))
            user = cursor.fetchone()
        
        Initialize.close_db()
        return user