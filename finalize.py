from datetime import datetime
import pyperclip as pc

def copy_to_clipboard(file_name):
    with open(file_name, 'r', encoding='utf-8') as f:
        text = f.read()
        pc.copy(text)

if __name__ == "__main__":
    current_date = datetime.now().strftime("%m%d%Y")
    # get current suc
    suc_file = f"{current_date}.txt"
    try:
      with open(suc_file, 'r', encoding='utf-8') as file:
           lines = file.readlines();
      choices = [
           '- <feature>',
           '- <debugging>',
           '- <refactoring>',
           '- <upskilling>',
           '- <do-next>',
           '- <roadblocks>' 
           ]
      with open(suc_file, 'w', encoding='utf-8') as file:
           for line in lines:
             if line.strip() not in choices:
               file.write(line)
    except Exception as e:
      print(e)

    copy_to_clipboard(suc_file)

    print(f"Finalized! File is copied to your clipboard and ready for submission")       
