import os
import shutil
import re

source = "C:/Users/Aditya/Downloads/files"
dest = "C:/Users/Aditya/Documents/organized_files"

os.makedirs(dest, exist_ok=True)
pattern = re.compile(r'@([\w.-]+)|https?://([\w.-]+)')

for name in os.listdir(source):
    path = os.path.join(source, name)
    if not os.path.isfile(path):
        continue

    domain = None
    match = pattern.search(name)

    if not match:
        try:
            with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                text = f.read()
                match = pattern.search(text)
                if match:
                    domain = match.group(1) or match.group(2)
        except:
            pass
    else:
        domain = match.group(1) or match.group(2)

    if domain:
        folder = os.path.join(dest, domain)
        os.makedirs(folder, exist_ok=True)
        shutil.move(path, os.path.join(folder, name))
        print(f"Moved: {name} → {domain}")
    else:
        print(f"No domain found in: {name}")
