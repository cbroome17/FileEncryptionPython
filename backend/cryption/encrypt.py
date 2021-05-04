import os
import time
from cryptography.fernet import Fernet
from backend.util.config import *


def encrypt_file(key, file):
    """
    Given a filename (str) and key (bytes), it encrypts the file and write it
    """
    time.sleep(1)
    f = Fernet(key)
    with open(file, "rb") as user_file:
        file_data = user_file.read()

    encrypted_data = f.encrypt(file_data)
    with open(file, "wb") as user_file:
        user_file.write(encrypted_data)


def encrypt_folder(key, file):
    f = Fernet(key)
    print("Please select directory you wish to encrypt")
    time.sleep(1)
    for entry in os.scandir(file):
        if (entry.path.endswith(".txt")
                or entry.path.endswith(".txt")) and entry.is_file():
            folder = (entry.path)
            with open(folder, "rb") as user_file:
                file_data = user_file.read()

            encrypted_data = f.encrypt(file_data)
            with open(folder, "wb") as user_file:
                user_file.write(encrypted_data)
