#!/usr/bin/env python3

"""
Functions file
"""

import os

def scan_folder(FOLDERS, scan_me):
    """ Scans a selected folder, only list # of folders and files """

    nr_of_folders = 0
    nr_of_files = 0
    folderPath = FOLDERS[scan_me]
    structure = []

    if scan_me not in ("baseFolder", "unsortedFolder"):
        folderPath = FOLDERS["baseFolder"] + "/" + FOLDERS[scan_me]

    for dirname, dirnames, filenames in os.walk(folderPath):
        for subdirname in dirnames:
            structure.append(os.path.join(dirname, subdirname))
            nr_of_folders += 1

        for filename in filenames:
            structure.append(os.path.join(dirname, filename))
            nr_of_files += 1

    print("Folder '" + folderPath + "' contains", str(nr_of_folders), "subfolders and", str(nr_of_files), "files.")

    print_structure = input("View structure? [y/N] ").lower()

    if print_structure in ("y", "yes"):
        print(*structure, sep="\n")
