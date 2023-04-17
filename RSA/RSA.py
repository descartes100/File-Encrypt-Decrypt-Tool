from cryptography.hazmat.primitives import serialization, padding, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding as asymmetric_padding
from cryptography.hazmat.backends import default_backend

def generate_keys(public_key_filepath, private_key_filepath):
    private_key = rsa.generate_private_key(
        public_exponent=65537, key_size=2048
    )

    with open(private_key_filepath, 'wb') as f:
        f.write(
            private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.PKCS8,
                encryption_algorithm=serialization.NoEncryption(),
            )
        )

    public_key = private_key.public_key()

    with open(public_key_filepath, 'wb') as f:
        f.write(
            public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo,
            )
        )

def encrypt_file(file_path, public_key_filepath):
    with open(public_key_filepath, "rb") as f:
        public_key = serialization.load_pem_public_key(
            f.read(), backend=default_backend()
        )

    with open(file_path, "rb") as f:
        plaintext = f.read()

    ciphertext = public_key.encrypt(
        plaintext,
        asymmetric_padding.OAEP(
            mgf=asymmetric_padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )

    with open(file_path, "wb") as f:
        f.write(ciphertext)

def decrypt_file(file_path, private_key_filepath):
    with open(private_key_filepath, "rb") as f:
        private_key = serialization.load_pem_private_key(
            f.read(), password=None, backend=default_backend()
        )

    with open(file_path, "rb") as f:
        ciphertext = f.read()

    plaintext = private_key.decrypt(
        ciphertext,
        asymmetric_padding.OAEP(
            mgf=asymmetric_padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None,
        ),
    )

    with open(file_path, "wb") as f:
        f.write(plaintext)

def main():
    # get user input
    operation = input("Enter 'g' to generate keys, 'e' to encrypt a file, or 'd' to decrypt a file: ")
    if operation == 'g':

        private_path = input("Enter private-key file path: ")
        public_path = input("Enter public-key file path: ")
        generate_keys(public_path, private_path)

    else:

        file_path = input("Enter file path: ")
        key_path = input("Enter key path: ")

        # perform encryption or decryption based on user input
        if operation == "e":
            encrypt(file_path, key_path)
            print("File encrypted successfully!")
        elif operation == "d":
            decrypt(file_path, key_path)
            print("File decrypted successfully!")
        else:
            print("Invalid input. Please enter 'e' or 'd'.")

if __name__ == "__main__":
    main()