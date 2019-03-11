#!/usr/bin/env python3

import os
import shutil
import helpers


"""
Setup functions, regarding folder structure
"""

def create_folders(path_to_folder):
    """ Creates the folders based on setup """
    try:
        if not os.path.exists(path_to_folder):
            os.makedirs(path_to_folder)
            print("Created folder:", path_to_folder)
        else:
            print("Folder --->", path_to_folder ,"<--- exists. Skipping.")

    except FileNotFoundError:
        print("File not found error. Try again.")



def setup_folders(FOLDERS):

    """ Change name on folders """

    for folder in sorted(FOLDERS.keys()):

        ff = helpers.remove_illegal_chars(input("Folder name for " + folder + "? (Enter for default) "))

        if ff is "":
            input("### Leaving " + folder + " folder as default. Press Enter. ###")
        else:
            FOLDERS[folder] = ff

        if folder == "baseFolder" or folder == "unsortedFolder":
            create_folders(FOLDERS[folder])
        else:
            create_folders(FOLDERS["baseFolder"] + "/" + FOLDERS[folder])

    input("------ Done creating folders. Press any key. -------")


def remove_folder(folder_to_remove):
    """ Deletes baseFolder """
    try:
        sure = input("Are you sure you want to delete the folder: '" + folder_to_remove + "'? [y/N] ").lower()
        if sure in ("y", "yes"):
            shutil.rmtree(folder_to_remove, ignore_errors=False, onerror=None)
        else:
            pass
    except FileNotFoundError:
        print("Folder: '" + folder_to_remove + "' is not created.")
