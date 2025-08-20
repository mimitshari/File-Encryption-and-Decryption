🔐 File Encryption & Decryption Tool

A Python-based tool for secure file encryption and decryption with the flexibility to choose from multiple algorithms:

Fernet

AES (Advanced Encryption Standard)

3DES (Triple Data Encryption Standard)

ChaCha20

This project was developed as part of the Forensic Computing (FC313 – Cyber Security) course. It empowers users to safeguard sensitive data while choosing the algorithm that best suits their needs for security, performance, and compatibility.

📖 Features

🔑 Key Generation & Management: Automatically generate, save, and load encryption keys.

📂 File Encryption & Decryption: Encrypt and decrypt any file type.

⚙️ Multiple Algorithms: Choose between Fernet, AES, 3DES, and ChaCha20.

💻 Cross-Platform: Works on Linux, macOS, and Windows.

🛡️ Enhanced Security: Protects data confidentiality and integrity.

🚀 Getting Started
1. Clone the Repository
git clone https://github.com/yourusername/file-encryption-tool.git
cd file-encryption-tool

2. Install Dependencies

Ensure you have Python 3.7+ installed. Install the required libraries:

pip install cryptography

3. Run the Program

You can run the script using:

python encryption_tool.py


The program will prompt you to:

Choose an algorithm (Fernet / AES / 3DES / ChaCha20)

Generate a key (saved as a .key file)

Select a file to encrypt/decrypt

Choose an operation (Encryption or Decryption)

📂 Project Structure
📁 file-encryption-tool
 ┣ 📄 encryption_tool.py   # Main script
 ┣ 📄 README.md            # Documentation
 ┗ 📂 keys/                # Stores generated encryption keys

🔑 Supported Algorithms
Algorithm	Type	Notes
Fernet	Symmetric	Easy to use, built-in key rotation.
AES	Symmetric	Industry standard; strong security with 128/192/256-bit key support.
3DES	Symmetric	Triple-layer encryption; stronger than DES but slower.
ChaCha20	Symmetric	High-speed, modern stream cipher.


📊 Example Workflow

Choose Algorithm → Fernet

Enter Key File → secret.key

Enter File Name → test.docx

Choose Operation → Encryption

Output → test.docx.encrypted

Decryption works the same way, restoring the original file.


✅ Conclusion

This project demonstrates a flexible and user-driven approach to file security, allowing individuals to tailor encryption methods to their needs. Future improvements include:

Adding more encryption algorithms

Improving the user interface

Enhancing cross-platform support

📜 License

This project is licensed under the MIT License – feel free to use, modify, and share
