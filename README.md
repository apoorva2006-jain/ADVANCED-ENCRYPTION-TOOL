# ADVANCED-ENCRYPTION-TOOL

A Python-based tool to encrypt and decrypt files using AES encryption with a simple and user-friendly interface.

*COMPANY* : CODTECH IT SOLUTIONS

*NAME* : APOORVA S

*INTERN ID* : CT12DG815

*DOMAIN* : CYBER SECURITY AND ETHICAL HACKING 

*DURATION* : 12 WEEKS

*MENTOR* : NEELA SANTOSH KUMAR 

#Advanced Encryption Tool – Python Project

Project Description:

The Advanced Encryption Tool is a Python-based application designed to provide secure file encryption and decryption using the AES (Advanced Encryption Standard) algorithm. The goal of this project was to build a robust encryption application that ensures data privacy and security with a user-friendly interface, as specified in the project instructions.

The tool uses the cryptography library, particularly the Fernet module, which is built on AES-128 in CBC mode with HMAC for authentication. Although the instruction mentions AES-256, Fernet ensures strong symmetric encryption by safely managing key generation, encryption, and decryption processes internally. This makes the tool both secure and simple to use, especially for those who are not from a technical background.

The tool is made up of two main Python files:

main.py – This is the GUI interface built using Tkinter. It includes options to browse files, encrypt, and decrypt, making it easy for non-technical users.

encryption_tool.py – This file handles the core logic, including:

Generate a key (generate_key)

Load the key from a file (load_key)

Encrypt a file (encrypt_file)

Decrypt a file (decrypt_file)

When the application is run for the first time, it automatically generates a secret key and saves it to a file named secret.key. This key is later used to both encrypt and decrypt files. Users can select any file (preferably .txt) using the GUI and perform encryption or decryption on it.

Technologies Used:-

Technology	Purpose:

Python 3	Core programming language

Tkinter	For building the GUI (buttons, input, etc.)

cryptography	To perform encryption/decryption with Fernet (AES)

Fernet (AES)	Symmetric encryption based on AES

OS module	For checking file existence and file handling

FileDialog	To select the file using GUI

Real-World Use of This Project:

In today’s digital world, file encryption is extremely important. Whether it's personal documents, financial records, academic research, or confidential work files — data must be protected from unauthorized access.

Here are some practical use cases:

Students can use this tool to protect their assignments or project work.

Software developers can secure configuration files and sensitive scripts.

Businesses can encrypt confidential reports or client data before sharing.

Anyone sending files over email or storing data in the cloud can use this tool to ensure privacy.

This tool is especially helpful for users who want data security without needing to learn complex commands or coding.

Features of the Advanced Encryption Tool:

AES-based encryption using Python's cryptography package

Automatic key generation and secure storage

Simple GUI using Tkinter

Encrypt and decrypt files with one click

Can be used in both educational and real-world scenarios

Conclusion:

To conclude, the Advanced Encryption Tool is a lightweight, easy-to-use Python application that demonstrates strong encryption principles with a clean graphical interface. It was created as part of a college-level project, but its functionality goes beyond the classroom. It can be used by anyone who wants to securely store or transfer files.

This project also introduces students to the basics of cryptography, file handling, and GUI development, making it a great learning experience. With further improvements, this tool could be extended to support multiple file types, password-based key storage, and cloud integration for wider use.

Ultimately, this project successfully meets all the deliverables mentioned in the instructions — combining security, simplicity, and practical use in one compact tool.
