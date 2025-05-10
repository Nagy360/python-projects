import os , shutil
path  = r"C:\Users\m-nag\Desktop\august"
print(os.listdir(path)) 

folder_names = ['dwg', 'pdf', 'txt', 'images', 'excel', 'others']

for loop in folder_names:
    os.makedirs(os.path.join(path, loop), exist_ok=True)
import os
import shutil

# This code creates folders for different file types in the specified directory.

# Sorting files into folders
for file in os.listdir(path):
    file_path = os.path.join(path, file)
    if os.path.isfile(file_path):
        if file.endswith('.dwg'):
            shutil.move(file_path, os.path.join(path, 'dwg'))
        elif file.endswith('.pdf'):
            shutil.move(file_path, os.path.join(path, 'pdf'))
        elif file.endswith('.txt'):
            shutil.move(file_path, os.path.join(path, 'txt'))
        elif file.lower().endswith(('.jpg', '.png', '.jpeg')):
            shutil.move(file_path, os.path.join(path, 'images'))
        elif file.endswith('.xlsx'):
            shutil.move(file_path, os.path.join(path, 'excel'))
        else:
            shutil.move(file_path, os.path.join(path, 'others'))