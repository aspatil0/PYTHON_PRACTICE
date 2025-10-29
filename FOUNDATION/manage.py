import os
import shutil
import re

source_dir = "C:/Users/Aditya/Downloads/files"
destination_dir = "C:/Users/Aditya/Documents/organized_files"

os.makedirs(destination_dir, exist_ok=True)

domain_pattern = re.compile(r'@([\w.-]+)|https?://([\w.-]+)')

for file_name in os.listdir(source_dir):
    file_path = os.path.join(source_dir, file_name)

    if not os.path.isfile(file_path):
        continue

    domain = None
    match = domain_pattern.search(file_name)
    if match:
        domain = match.group(1) or match.group(2)
    else:
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                match = domain_pattern.search(content)
                if match:
                    domain = match.group(1) or match.group(2)
        except Exception as e:
            print(f"Cannot read file {file_name}: {e}")

    if domain:
        domain_folder = os.path.join(destination_dir, domain)
        os.makedirs(domain_folder, exist_ok=True)
        shutil.move(file_path, os.path.join(domain_folder, file_name))
        print(f"Moved {file_name} → {domain}")
    else:
        print(f"No domain found in {file_name}")
