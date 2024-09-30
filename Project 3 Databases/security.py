#######################################################################################################################
#                                         Grazioso Salvare Animal Rescue System                                       #
#                                                                                                                     #
# This script provides security methods for managing user authentication in the Rescue Animal Dashboard application.  #
# It includes functions to add new users, hash passwords, and verify passwords against stored hashes.                 #
#                                                                                                                     #
# Author: Richard VanSkike                                                                                            #
# Revision: 1.0                                                                                                       #
# Course: CS-499 Computer Science Capstone                                                                            #
# Source: Milestone 3 - Enhancement Two: Algorithms and Data Structure                                                #
# College: Southern New Hampshire University                                                                          #
#                                                                                                                     #
# Dependencies: bcrypt, initialize (custom module), validation (custom module)                                        #
#                                                                                                                     #
# Classes:                                                                                                            #
#   Security - Class for handling user authentication and security.                                                   #
#                                                                                                                     #
# Methods:                                                                                                            #
#     add_user(scanner) - Adds a new user to the Users database with a hashed password.                               #
#     hash_password(password) - Hashes a plaintext password for secure storage.                                       #
#     verify_password(password, hashed) - Verifies a plaintext password against a stored hashed password.             #
#                                                                                                                     #
# Usage:                                                                                                              #
#    This script is intended to be used as part of the Rescue Animal Database application.                            #
#######################################################################################################################
import bcrypt                       # Import bcrypt to handle password hashing functions
from initialize import Initialize   # Import Initialize from initialize.py
from validation import Validation   # Import Validation from validation.py

# Revision change introducing the Security class:
# The Security class is a newly added functionality that enhances the application's security by 
# leveraging the database to maintain a user login system. This feature provides an additional 
# layer of protection by controlling access to the system.
#
# The `add_user` method allows an authenticated user to add new users to the database. It validates 
# the entries for username and password, ensuring that both fields are not null. 
#
# Once the inputs are validated, the password is hashed to securely obfuscate the plaintext 
# information before storing it in the database. This protects sensitive user credentials from 
# being exposed in the event of unauthorized access to the database.
#
# During the login process, a user will enter their username and password. The application 
# verifies the provided password against the stored hashed password in the database. If both 
# the username and password are validated, the user is granted access to the system.
#
# This class introduces essential security measures, ensuring that user credentials are 
# stored securely and that access is restricted to authenticated users only.
class Security:
    # Method to proccess addtion of user to Users database
    def add_user(scanner):
            username = input("Please enter the new username (Cannot be blank): ").strip().lower()
            username = Validation.null_validation(username, "username")

            password = input("Please enter the password for the new user (Cannot be blank): ").strip().lower()
            password = Validation.null_validation(password, "password")
            hashed_password = Security.hash_password(password)

            with Initialize.conn.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO Users (username, hashed_password)
                    VALUES (%s, %s)
                """, (username, hashed_password))
                Initialize.conn.commit()

            print(f"New user {username} added to the database!")
            
    # Method to proccess plaintext passwords into hash
    def hash_password(password):
        password_bytes = password.encode('utf-8') # Encode the password string to bytes
        salt = bcrypt.gensalt()                   # Generate a salt using bcrypt

        hashed_password_bytes = bcrypt.hashpw(password_bytes, salt) # Hash the password bytes with the generated salt
        hashed_password = hashed_password_bytes.decode('utf-8')     # Decode the hashed password from bytes back to a string

        return hashed_password  # Return the hashed password string

    # Method to proccess plaintext passwords to verify
    def verify_password(password, hashed):
        password_bytes = password.encode('utf-8')   # Encode the plain text password string to bytes
        hashed_bytes = hashed.encode('utf-8')       # Encode the hashed password string to bytes

        password_matches = bcrypt.checkpw(password_bytes, hashed_bytes) # Verify the password by comparing the plain text password bytes with the hashed password bytes

        return password_matches # Return the result of the comparison (True if they match, False otherwise)