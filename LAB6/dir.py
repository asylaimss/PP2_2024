#1
import os

def list_directories_files(path):
    print("Directories:")
    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        if os.path.isdir(full_path):
            print(item)

    print("\nFiles:")
    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        if os.path.isfile(full_path):
            print(item)

    print("\nAll Directories and Files:")
    for root, dirs, files in os.walk(path):
        for dir_name in dirs:
            print(os.path.join(root, dir_name))
        for file_name in files:
            print(os.path.join(root, file_name))

# Example
specified_path = input("Enter the path: ")
list_directories_files(specified_path)

#2
import os

def check_path_access(path):
    if not os.path.exists(path):
        print("Path does not exist")
        return
    print("Path exists")

    if os.access(path, os.R_OK):
        print("Readable")
    else:
        print("Not readable")

    if os.access(path, os.W_OK):
        print("Writable")
    else:
        print("Not writable")

    if os.access(path, os.X_OK):
        print("Executable")
    else:
        print("Not executable")

# Example 
specified_path = input("Enter the path: ")
check_path_access(specified_path)

#3
import os

def analyze_path(path):
    if os.path.exists(path):
        print("Path exists.")
        dirname = os.path.dirname(path)
        filename = os.path.basename(path)
        print("Directory portion:", dirname)
        print("Filename portion:", filename)
    else:
        print("Path does not exist.")

# Example 
specified_path = input("Enter the path: ")
analyze_path(specified_path)

#4
def count_lines(file_path):
    try:
        with open(file_path, 'r') as file:
            line_count = sum(1 for line in file)
        return line_count
    except FileNotFoundError:
        print("File not found.")
        return None
    except PermissionError:
        print("Permission denied to open the file.")
        return None

# Example 
file_path = input("Enter the path to the text file: ")
line_count = count_lines(file_path)
if line_count is not None:
    print("Number of lines in the file:", line_count)

#5
def write_list_to_file(file_path, data):
    try:
        with open(file_path, 'w') as file:
            for item in data:
                file.write(str(item) + '\n')
        print("List written to file successfully.")
    except PermissionError:
        print("Permission denied to write to the file.")
    except Exception as e:
        print("An error occurred:", e)

# Example 
file_path = input("Enter the path to the file: ")
data = ['apple', 'banana', 'orange', 'grape']
write_list_to_file(file_path, data)

#6
import string

def generate_text_files():
    alphabet = string.ascii_uppercase
    for char in alphabet:
        file_name = char + ".txt"
        with open(file_name, 'w') as file:
            file.write(f"This is the content of file {file_name}")

generate_text_files()

#7
def copy_file(source_file, destination_file):
    try:
        with open(source_file, 'r') as source:
            with open(destination_file, 'w') as destination:
                destination.write(source.read())
        print("File copied successfully.")
    except FileNotFoundError:
        print("File not found.")
    except PermissionError:
        print("Permission denied to open the file.")
    except Exception as e:
        print("An error occurred:", e)

# Example
source_file = input("Enter the path to the source file: ")
destination_file = input("Enter the path to the destination file: ")
copy_file(source_file, destination_file)

#8
import os

def delete_file(file_path):
    if not os.path.exists(file_path):
        print("File does not exist.")
        return

    if not os.access(file_path, os.R_OK | os.W_OK):
        print("Permission denied to delete the file.")
        return

    try:
        os.remove(file_path)
        print("File deleted successfully.")
    except Exception as e:
        print("An error occurred:", e)

# Example 
specified_path = input("Enter the path to the file you want to delete: ")
delete_file(specified_path)