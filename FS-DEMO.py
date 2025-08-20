#!/usr/bin/env python
# coding: utf-8

# In[1]:


from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.fernet import Fernet


def generate_aes_key():
    return Fernet.generate_key()[:32]  # Use the first 32 bytes for AES


def generate_des3_key():
    return Fernet.generate_key()[:24]  # Use the first 24 bytes for Triple DES


def generate_chacha20_key():
    return Fernet.generate_key()[:32]  # Use the first 32 bytes for ChaCha20


def generate_fernet_key():
    return Fernet.generate_key()


def write_key(key, key_filename):
    with open(key_filename, 'wb') as key_file:
        key_file.write(key)


def load_key(key_filename):
    return open(key_filename, 'rb').read()


def generate_and_save_key(algorithm, key_filename):
    if algorithm == 1:
        key = generate_fernet_key()
    elif algorithm == 2:
        key = generate_aes_key()
    elif algorithm == 3:
        key = generate_des3_key()
    elif algorithm == 4:
        key = generate_chacha20_key()
    else:
        raise ValueError("Invalid algorithm. Supported algorithms are 1 for 'fernet', 2 for 'aes', 3 for 'des3', and 4 for 'chacha20'.")
    write_key(key, key_filename)
    print(f"Key generated and saved to '{key_filename}'.")


def encrypt_file(file_path, key, algorithm):
    if algorithm == 1:
        cipher = Fernet(key)
        with open(file_path, 'rb') as file:
            data = file.read()
        encrypted_data = cipher.encrypt(data)
    elif algorithm == 2:
        backend = default_backend()
        cipher = Cipher(algorithms.AES(key), modes.CFB(b'\0' * 16), backend=backend)
        encryptor = cipher.encryptor()
        with open(file_path, 'rb') as file:
            data = file.read()
        encrypted_data = encryptor.update(data) + encryptor.finalize()
    elif algorithm == 3:
        backend = default_backend()
        cipher = Cipher(algorithms.TripleDES(key), modes.CFB(b'\0' * 8), backend=backend)
        encryptor = cipher.encryptor()
        with open(file_path, 'rb') as file:
            data = file.read()
        encrypted_data = encryptor.update(data) + encryptor.finalize()
    elif algorithm == 4:
        nonce = b'\0' * 16
        cipher = Cipher(algorithms.ChaCha20(key, nonce), mode=None, backend=default_backend())
        encryptor = cipher.encryptor()
        with open(file_path, 'rb') as file:
            data = file.read()
        encrypted_data = encryptor.update(data) + encryptor.finalize()
    else:
        raise ValueError("Invalid algorithm. Supported algorithms are 1 for 'fernet', 2 for 'aes', 3 for 'des3', and 4 for 'chacha20'.")

    with open(file_path + '.encrypted', 'wb') as encrypted_file:
        encrypted_file.write(encrypted_data)


def decrypt_file(encrypted_file_path, key, algorithm):
    if algorithm == 1:
        cipher = Fernet(key)
        with open(encrypted_file_path, 'rb') as encrypted_file:
            encrypted_data = encrypted_file.read()
        decrypted_data = cipher.decrypt(encrypted_data)
    elif algorithm == 2:
        backend = default_backend()
        cipher = Cipher(algorithms.AES(key), modes.CFB(b'\0' * 16), backend=backend)
        decryptor = cipher.decryptor()
        with open(encrypted_file_path, 'rb') as encrypted_file:
            encrypted_data = encrypted_file.read()
        decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()
    elif algorithm == 3:
        backend = default_backend()
        cipher = Cipher(algorithms.TripleDES(key), modes.CFB(b'\0' * 8), backend=backend)
        decryptor = cipher.decryptor()
        with open(encrypted_file_path, 'rb') as encrypted_file:
            encrypted_data = encrypted_file.read()
        decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()
    elif algorithm == 4:
        nonce = b'\0' * 16
        cipher = Cipher(algorithms.ChaCha20(key, nonce), mode=None, backend=default_backend())
        decryptor = cipher.decryptor()
        with open(encrypted_file_path, 'rb') as encrypted_file:
            encrypted_data = encrypted_file.read()
        decrypted_data = decryptor.update(encrypted_data) + decrypt


# In[ ]:




