# Fake File Integrity Checker
# IS Lab Project
# Checks whether a file has been changed using SHA-256 hash

import hashlib
import os

# Function to calculate SHA-256 hash of a file
def calculate_hash(file_path):
    sha256 = hashlib.sha256()

    try:
        with open(file_path, "rb") as file:
            while True:
                data = file.read(4096)

                if not data:
                    break

                sha256.update(data)

        return sha256.hexdigest()

    except FileNotFoundError:
        return None


# Function to save original hash
def save_hash(file_path, hash_value):
    hash_file = file_path + ".hash"

    with open(hash_file, "w") as file:
        file.write(hash_value)

    print("Original hash saved successfully.")


# Function to read saved hash
def load_hash(file_path):
    hash_file = file_path + ".hash"

    try:
        with open(hash_file, "r") as file:
            return file.read()

    except FileNotFoundError:
        return None


# Function to verify file integrity
def verify_integrity(file_path):

    current_hash = calculate_hash(file_path)

    if current_hash is None:
        print("File not found!")
        return

    saved_hash = load_hash(file_path)

    if saved_hash is None:
        print("No previous hash found.")
        print("Creating baseline hash...")

        save_hash(file_path, current_hash)

    else:

        if current_hash == saved_hash:
            print("File Integrity Status: SAFE")
            print("No changes detected.")

        else:
            print("WARNING!")
            print("File has been modified.")
            print("Integrity check FAILED")


# Main Menu
while True:

    print("\n====== Fake File Integrity Checker ======")
    print("1. Check File")
    print("2. Exit")

    choice = input("Enter choice: ")

    if choice == "1":

        path = input("Enter file path: ")

        verify_integrity(path)

    elif choice == "2":
        print("Program Closed")
        break

    else:
        print("Invalid choice")