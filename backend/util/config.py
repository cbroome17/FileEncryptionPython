import os
import fileinput
import time
from cryptography.fernet import Fernet
from tkinter import Tk
from tkinter.filedialog import askopenfilename, askdirectory


def write_key():
    '''
    Generates a key and saves to a file
    '''

    key = Fernet.generate_key()
    with open("key.key", 'wb') as key_file:
        key_file.write(key)


def load_key():
    '''
    Loads key from user selected file
    '''
    Tk().withdraw()
    filename = askopenfilename()
    return open(filename, "rb").read()


def load_file():
    '''
    Loads file from user selection
    '''
    Tk().withdraw()
    filename = askopenfilename()
    return filename


def load_directory():
    '''
    Selects a directory then stores specified location in variable
    '''
    Tk().withdraw()
    dirname = askdirectory()
    return dirname
