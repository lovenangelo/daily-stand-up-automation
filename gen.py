from shutil import copyfile
from datetime import datetime
from os import path, stat
from sys import exit

def replace_date_in_file(source_path, destination_path):
    try:
        current_date = datetime.now().strftime("%Y-%m-%d")

        # Copy the file from source to destination
        copyfile(source_path, destination_path)

        # Replace '<date>' with current_date in the copied file
        with open(destination_path, "r", encoding='utf-8' ) as file:
            content = file.read()
        content = content.replace("<Date>", current_date)
        with open(destination_path, "w", encoding="utf-8") as file:
            file.write(content)

        print(f"File copied and date replaced successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    source_file = "template.txt"
    current_date = datetime.now().strftime("%m%d%Y")
    if path.exists(f"{current_date}.txt"):
      if stat(f"{current_date}.txt").st_size > 0:
        print(f"File already exists and not empty")
        exit()
    with open(f"{current_date}.txt", 'w') as f:
      f.write('')
    destination_file = f"{current_date}.txt"
    replace_date_in_file(source_file, destination_file) 
