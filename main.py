import itertools
import string
import time as t
import os

buffer_size = 1000  # Number of combinations to buffer
buffer = []  # Buffer for combinations
chars = string.ascii_letters + string.digits + string.punctuation
# Create directory for wordlist files if it doesn't exist
os.mkdir("wordlist") if not os.path.exists("wordlist") else None
os.chdir("wordlist")
# Get file name from user
file_name = input("Enter the file name: ").strip()
if os.path.exists(file_name):
    print(f"The file {file_name} already exists. Please choose another name.")
    exit()

def length_input():
    print("Enter the desired length of character combinations:")
    try:
        length = int(input().strip())
        return length
    except ValueError:
        print("Invalid input.")
        return None

def open_file(length):
    with open(file_name, "w", encoding="utf-8") as f:
        for i in range(length):
            for combo in itertools.product(chars, repeat=i+1):
                buffer.append("".join(combo) + "\n")
                # Write the buffer to the file when it is full
                if len(buffer) >= buffer_size:
                    f.writelines(buffer)
                    buffer.clear()
                    t.sleep(0.01)  # Short pause to reduce CPU usage 
        if buffer:
            f.writelines(buffer) # Write remaining combinations in the buffer to the file

def main():
    # Characters to be combined
    length = length_input()
    if length is not None:
        open_file(length)
        print(f"Done. The file {file_name} has been created.")
        input("Press Enter to exit.")
if __name__ == "__main__": 
    main()
