# Step 1: Create a new file and write to it
with open("my_file.txt", "w") as file:
    file.write("This is the first line with text.\n")
    file.write("Second line, with a number: 42.\n")
    file.write("Third line, with more text.\n")

# Step 2: Read the contents of the file and display them
with open("my_file.txt", "r") as file:
    content = file.read()
    print("File contents:")
    print(content)

# Step 3: Append more lines to the file
with open("my_file.txt", "a") as file:
    file.write("Fourth line, appending more text.\n")
    file.write("Fifth line with another number: 100.\n")
    file.write("Sixth line, appending to the file.\n")

# Step 4: Implement error handling
try:
    # Try to open the file and perform tasks
    with open("my_file.txt", "w") as file:
        file.write("This is the first line with text.\n")
        file.write("Second line, with a number: 42.\n")
        file.write("Third line, with more text.\n")
    
    with open("my_file.txt", "r") as file:
        content = file.read()
        print("File contents:")
        print(content)
    
    with open("my_file.txt", "a") as file:
        file.write("Fourth line, appending more text.\n")
        file.write("Fifth line with another number: 100.\n")
        file.write("Sixth line, appending to the file.\n")

except FileNotFoundError:
    print("Error: The file was not found.")
except PermissionError:
    print("Error: You do not have permission to modify this file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("Execution completed, file handling is done.")
