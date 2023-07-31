import os

# Get a list of all files in the current directory
files = os.listdir()

# Loop through the list of files
for file in files:
    # If the file is an mp3 file
    if file.endswith('.mp3'):
        # Delete the file
        os.remove(file)
