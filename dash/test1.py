import os

# Set the directory path and the prefix string
directory_path = '.\Data_files'
prefix = 'uploaded'

# List all files in the directory
for filename in os.listdir(directory_path):
    if filename.startswith(prefix):
        print(filename)
        file_path = os.path.join(directory_path, filename)
        print(file_path)
        os.remove(file_path)
        print(f'Removed file: {file_path}')
