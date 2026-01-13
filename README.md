# Brute Force Wordlist Generator

This project generates a wordlist containing all possible character combinations up to a user-defined length.

It is intended for educational purposes, CTFs, and controlled security testing environments.
#### The project is available as both:
- a Python script
- a standalone Windows .exe file (no Python installation required)

## 🔧 Features:

1. Uses all printable ASCII characters:
- letters (uppercase & lowercase)
- digits
- punctuation

2. User-defined maximum combination length
3. Efficient buffered file writing to reduce I/O overhead
4. Automatic creation of the wordlist/ directory
5. Prevents accidental overwriting of existing files

6. Works as:
- main.py
- compiled.exe

## ▶ How to Use: 
- Python version:

1. Run main.py
2. Enter a file name for the wordlist
3. Enter the maximum length of character combinations

- EXE version: 

1. Run the .exe file
2. Follow the on-screen prompts

#### No Python installation required.

## 🧪 Example: 

Enter the file name: example_wordlist.txt
Enter the maximum length of combinations: 2
Generating wordlist...
Done. The file "example_wordlist.txt" has been created.

## 🛡 Requirements: 

- Python 3.x (only for the script version)
- No dependencies
- EXE version runs standalone on Windows
## ⚠ Notes: 
The number of generated combinations grows exponentially. 

Even small lengths can produce extremely large files. 

A short delay is applied during file writing to reduce CPU load. 

If the output file already exists, the user is asked to choose a different name. 