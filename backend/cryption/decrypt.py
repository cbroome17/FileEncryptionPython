import os
import time
from cryptography.fernet import Fernet
from backend.util.config import *


def decrypt_file(key, file):
    f = Fernet(key)
    with open(file, "rb") as user_file:
        file_data = user_file.read()

    decrypted_data = f.decrypt(file_data)

    with open(file, "wb") as user_file:
        user_file.write(decrypted_data)


def decrypt_folder(key, file):
    f = Fernet(key)
    for entry in os.scandir(file):
        if (entry.path.endswith(".txt")
                or entry.path.endswith(".txt")) and entry.is_file():
            navi = (entry.path)
            with open(navi, "rb") as user_file:
                file_data = user_file.read()

            encrypted_data = f.decrypt(file_data)
            with open(navi, "wb") as user_file:
                user_file.write(encrypted_data)
