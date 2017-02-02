import os
def rename_file():
    file_list = os.listdir(r"C:\Users\Администратор\Downloads\alphabet")
    saved_path = os.getcwd()
    print ("CWD is" + saved_path)
    os.chdir(r"C:\Users\Администратор\Downloads\alphabet")
    for file_name in file_list:
        print("Old name -" + file_name)
        print("New name -" + file_name.translate(None,"0123456789"))
        os.rename(file_name, file_name.translate(None,"0123456789"))
    os.chdir(saved_path)

rename_file()
