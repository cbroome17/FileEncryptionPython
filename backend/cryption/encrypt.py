import os
import time
from cryptography.fernet import Fernet
from backend.util.config import *


def encrypt_file():
    """
    Given a filename (str) and key (bytes), it encrypts the file and write it
    """
    print('Please select the key file. ')
    time.sleep(1)
    key = load_key()
    f = Fernet(key)
    userfile = load_file()
    with open(userfile, "rb") as user_file:
        file_data = user_file.read()

    encrypted_data = f.encrypt(file_data)
    with open(userfile, "wb") as user_file:
        user_file.write(encrypted_data)


def encrypt_folder():
    print('Please select the key file. ')
    time.sleep(1)
    key = load_key()
    f = Fernet(key)
    print("Please select directory you wish to encrypt")
    time.sleep(1)
    directory = load_directory()
    for entry in os.scandir(directory):
        if (entry.path.endswith(".txt")
                or entry.path.endswith(".txt")) and entry.is_file():
            navi = (entry.path)
            with open(navi, "rb") as user_file:
                file_data = user_file.read()

            encrypted_data = f.encrypt(file_data)
            with open(navi, "wb") as user_file:
                user_file.write(encrypted_data)
