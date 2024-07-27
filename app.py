from cryptography.fernet import Fernet
import base64
import hashlib

def generate_key(password):
    # Generate a key from the password
    sha256 = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(sha256[:32])

def encrypt_message(message, password):
    key = generate_key(password)
    fernet = Fernet(key)
    encrypted_message = fernet.encrypt(message.encode())
    return encrypted_message

def decrypt_message(encrypted_message, password):
    key = generate_key(password)
    fernet = Fernet(key)
    decrypted_message = fernet.decrypt(encrypted_message).decode()
    return decrypted_message

if __name__ == "__main__":
    password = "heyitsmeagain"

    while True:
        print("Choose an option:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            message = input("Enter the message to encrypt: ")
            encrypted = encrypt_message(message, password)
            print(f"Encrypted message: {encrypted.decode()}")

        elif choice == '2':
            encrypted_message = input("Enter the encrypted message (base64 encoded): ")
            try:
                encrypted_message = encrypted_message.encode()
                decrypted = decrypt_message(encrypted_message, password)
                print(f"Decrypted message: {decrypted}")
            except Exception as e:
                print(f"Error: {e}")

        elif choice == '3':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please choose 1, 2, or 3.")
