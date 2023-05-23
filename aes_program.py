from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import padding

def encrypt(plaintext, key):
    # Set up the encryption cipher with AES algorithm and ECB mode
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
    encryptor = cipher.encryptor()

    # Apply PKCS7 padding to the plaintext
    padder = padding.PKCS7(128).padder()
    padded_plaintext = padder.update(plaintext) + padder.finalize()

    # Encrypt the padded plaintext
    ciphertext = encryptor.update(padded_plaintext) + encryptor.finalize()
    return ciphertext

def decrypt(ciphertext, key):
    # Set up the decryption cipher with AES algorithm and ECB mode
    backend = default_backend()
    cipher = Cipher(algorithms.AES(key), modes.ECB(), backend=backend)
    decryptor = cipher.decryptor()

    # Decrypt the ciphertext
    padded_plaintext = decryptor.update(ciphertext) + decryptor.finalize()

    # Remove PKCS7 padding from the decrypted plaintext
    unpadder = padding.PKCS7(128).unpadder()
    plaintext = unpadder.update(padded_plaintext) + unpadder.finalize()
    return plaintext

def main():
    key = b'0123456789abcdef'  # 16-byte AES key

    print("--------------------------------")
    print("AES Encryption/Decryption Program")
    print("--------------------------------")

    while True:
        print("\n---AES Encryption/Decryption---")
        print("Select an option:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            plaintext = input("Enter the message to encrypt: ").encode()
            ciphertext = encrypt(plaintext, key)
            print("Ciphertext:", ciphertext.hex())

        elif choice == '2':
            ciphertext_hex = input("Enter the ciphertext (in hex format): ")
            ciphertext = bytes.fromhex(ciphertext_hex)
            plaintext = decrypt(ciphertext, key)
            print("Decrypted text:", plaintext.decode())

        elif choice == '0':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == '__main__':
    main()
