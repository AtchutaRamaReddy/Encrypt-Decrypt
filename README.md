# Encrypt/Decrypt Message Script

This Python script allows you to encrypt and decrypt messages using symmetric encryption. It provides a simple menu to choose between encrypting a message and decrypting an encrypted message.

## Features

- **Encrypt a Message**: Input a message to get an encrypted version.
- **Decrypt a Message**: Input an encrypted message and receive the decrypted text.

## Requirements

- Python 3.x
- `cryptography` library

## Installation

1. Install the required library:
   ```bash
   pip install cryptography

Usage
Run the Script:
    python encrypt_decrypt_menu.py
Menu Options:

1: Encrypt a message.
Enter the message to encrypt.
The script will output the encrypted message.
2: Decrypt a message.
Enter the encrypted message (base64 encoded).
The script will output the decrypted message.
3: Exit the script.

Example
Encrypting a Message:
  Choose an option:
1. Encrypt a message
2. Decrypt a message
3. Exit
Enter your choice (1/2/3): 1
Enter the message to encrypt: Hello World
Encrypted message: gAAAAABf2g...

Decrypting a Message:
   Choose an option:
1. Encrypt a message
2. Decrypt a message
3. Exit
Enter your choice (1/2/3): 2
Enter the encrypted message (base64 encoded): gAAAAABf2g...
Decrypted message: Hello World

Notes
The encrypted message must be base64 encoded for decryption.
The script includes error handling for invalid decryption inputs.

License:
 This README provides a clear overview of how to set up and use the encryption/decryption script, including installation instructions, usage examples, and notes about the password and input formats.
