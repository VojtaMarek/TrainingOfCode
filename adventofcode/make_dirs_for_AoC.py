"""This code check if you are ready for Advent of Code. In case, you have no day folders (eg. 01, 02, ..)
in current year folder (eg. 2022/) created, it gives you an option to do so."""

import os
import datetime

YEAR = datetime.datetime.today().strftime('%Y')
PATH = os.path.abspath(os.getcwd())


def get_path_with_year(current_year=YEAR, current_path=PATH):
    year_path = f'{current_path}\\{current_year}'
    return year_path


def check_folder(path=get_path_with_year(), create_folders=False):
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
            if create_folders:
                os.makedirs(new_path)
                print(
                    new_path + "-> WAS CREATED.",
                )
        else:
            print("Folder exists: " + new_path + " -> no need to make a new one.")

    return flag


if __name__ == "__main__":
    all_folders_created = check_folder()
    if all_folders_created:
        print("You are ready for AoC!")
    elif (input("Do you want to create the folders? (C for create)\n> ").upper().strip() == "C"):
        check_folder(create_folders=True)
