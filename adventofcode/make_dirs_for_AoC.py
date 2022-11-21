"""This code check if you are ready for Advent of Code. In case, you have no day folders (eg. 01, 02, ..)
in current year folder (eg. 2022/) created, it gives you an option to do so."""

import os
import datetime

YEAR = '2021'#datetime.datetime.today().strftime('%Y')
PATH = os.path.abspath(os.getcwd())
FILE_TYPE = '.py'


def get_path_with_year(current_year=YEAR, current_path=PATH):
    year_path = f'{current_path}\\{current_year}'
    return year_path


def check_folder(path=get_path_with_year(), create_folders=False, create_data_files=False, create_code_files=False):
    flag = True
    new_folders = []
    for folder in range(1, 26):
        if folder < 10:
            new_folders.append("0" + str(folder))
        else:
            new_folders.append(str(folder))

    for new_folder in new_folders:
        new_path = f'{path}\\{new_folder}\\'
        if not os.path.exists(new_path):
            print(
                "Folder does not exist: "
                + new_path
                + " -> lets create one to get ready for AoC"
            )
            flag = False
            if create_folders: # to get folders
                os.makedirs(new_path)
                print(
                    new_path + "-> WAS CREATED.",
                )
        elif not create_data_files or not create_code_files:
            print("Folder exists: " + new_path + " -> no need to make a new one.")
        if create_data_files:
            try:
                with open(f"{new_path}data.txt", "x") as data_file: data_file.write('')
                print(f"{new_path}data.txt -> WAS CREATED.")
            except:
                print(f"{new_path}data.txt -> WAS NOT CREATED.")
        if create_code_files:
            try:
                with open(f"{new_path}{new_folder}{FILE_TYPE}", "x") as code_file: code_file.write('')
                print(f"{new_path}{new_folder}{FILE_TYPE} -> WAS CREATED.")
            except:
                print(f"{new_path}{new_folder}{FILE_TYPE} -> WAS NOT CREATED.")


    return flag


if __name__ == "__main__":
    all_folders_created = check_folder()
    if all_folders_created:
        print("Your folders are ready for AoC!")
    elif (input("Do you want to create the folders? ('F' for create Folders)\n> ").upper().strip() == "F"):
        check_folder(create_folders=True)
    all_folders_created = check_folder()
    if all_folders_created:
        if (input(f"Do you want to create the 01{FILE_TYPE} an so on files in folders? ('C' for create Code)\n> ").upper().strip() == "C"):
            check_folder(create_code_files=True)
        if (input("Do you want to create the data.txt files in folders? ('D' for create Data)\n> ").upper().strip() == "D"):
            check_folder(create_data_files=True)

