from backend.cryption import encrypt, decrypt
from backend.util import config


def main():
    encrypt_or_decrypt = input(
        "Are you looking to 'encrypt', or 'decrypt'? \nif seeking to create first time key then enter 'key' as your input\n"
    )
    if encrypt_or_decrypt == 'encrypt':
        choice = input(
            "What do you want to encrypt? \n (1) -Single File  (2) -Directory of files \n")
        if choice == '1':
            encrypt.encrypt_file()
        elif choice == '2':
            encrypt.encrypt_folder()
    elif encrypt_or_decrypt == 'decrypt':
        choice = input(
            "What do you want to decrypt? \n (1) -Single File  (2) -Directory of files \n"
        )
        if choice == '1':
            encrypt.decrypt_file()
        elif choice == '2':
            encrypt.decrypt_folder()
    elif encrypt_or_decrypt == 'key':
        config.write_key()


if __name__ == '__main__':
    main()
