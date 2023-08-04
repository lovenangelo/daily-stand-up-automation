from shutil import copyfile
from datetime import datetime
from os import path, stat
from sys import exit
import questionary

def add_task(category, task, file):
    try:
      with open(suc_file, 'r', encoding='utf-8') as file:
          content = file.read();
      content = content.replace(f"<{category}>", f"{task}\n- <{category}>")
      with open(suc_file, 'w', encoding='utf-8') as file:
          file.write(content)
      print(f"New task successfully added in {category}")    
    except Exception as e:
      print(f"An error occurred: {e}")
      
   

if __name__ == "__main__":
    current_date = datetime.now().strftime("%m%d%Y")
    # get current suc
    suc_file = f"{current_date}.txt"
    # check if file is empty
    if path.exists(f"{current_date}.txt"):
        if stat(f"{current_date}.txt").st_size == 0:
            print(f"File is empty, generate from template first.")
            exit()
        category = questionary.select(
        "Select task category: ",
        choices = [
          'feature',
          'debugging',
          'refactoring',
          'upskilling',
          'do-next',
          'roadblocks' 
        ]).ask()
        task = questionary.text("Enter new task completed").ask()
    else:
        print(f"File doesn't exist, generate from template first.")
        exit()

    add_task(category, task, suc_file) 

