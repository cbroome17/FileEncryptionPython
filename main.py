from backend.cryption import encrypt, decrypt
from backend.util import config


def main():

    key = config.load_key()
    encrypt_or_decrypt = input(
        "Are you looking to 'encrypt', or 'decrypt'? \nif seeking to create first time key then enter 'key' as your input\n"
    )
    file_or_folder = input("(file) or (folder):\n")
    
    
    if encrypt_or_decrypt == 'encrypt':
        
        if file_or_folder == 'file':
            file = config.load_file()
            encrypt.encrypt_file(key, file)
            
        elif file_or_folder == 'folder':
            file = config.load_directory
            encrypt.encrypt_folder(key, file)
            
            
    elif encrypt_or_decrypt == 'decrypt':
        
        if file_or_folder == 'file':
            file = config.load_file()
            decrypt.decrypt_file(key, file)
            
        elif file_or_folder == 'folder':
            file = config.load_directory()
            decrypt.decrypt_folder(key, file)
            
            
    elif encrypt_or_decrypt == 'key':
        config.write_key()

        

if __name__ == '__main__':
    main()
