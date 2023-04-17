from cryptography.fernet import Fernet

def encrypt(file_path, key):
    with open(file_path, 'rb') as f:
        plaintext = f.read()

    fernet = Fernet(key)
    ciphertext = fernet.encrypt(plaintext)

    with open(file_path, 'wb') as f:
        f.write(ciphertext)

def decrypt(file_path, key):
    with open(file_path, 'rb') as f:
        ciphertext = f.read()

    fernet = Fernet(key)
    plaintext = fernet.decrypt(ciphertext)

    with open(file_path, 'wb') as f:
        f.write(plaintext)

def main():
    # get user input
    operation = input("Enter 'e' to encrypt a file, or 'd' to decrypt a file: ")
    file_path = input("Enter file path: ")

    # perform encryption or decryption based on user input
    if operation == "e":
        encrypt(file_path)
        print("File encrypted successfully!")
    elif operation == "d":
        decrypt(file_path)
        print("File decrypted successfully!")
    else:
        print("Invalid input. Please enter 'e' or 'd'.")

if __name__ == "__main__":
    main()