filename = input("Enter the filename to read: ")
try:
    with open(filename, 'r') as file:
        text = file.read()
except FileNotFoundError:
    print("Sorry, that file does not exist.")
    exit()
except Exception as error:
    print("Could not read the file:", error)
    exit()

# Change the text to uppercase
new_text = text.upper()
new_filename = "modified_" + filename
try:
    with open(new_filename, 'w') as file:
        file.write(new_text)
    print("Modified contents written to", new_filename)
except Exception as error:
    print("Could not write to the new file:", error)

