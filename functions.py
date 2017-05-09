#!/usr/bin/env python3

"""
Functions file
"""

import os
from PIL import Image
import re
# from PythonMagick import Image

# from PIL.ExifTags import TAGS
import imghdr
import magic

MONTHS = {
    "01": "Januari",
    "02": "Februari",
    "03": "Mars",
    "04": "April",
    "05": "Maj",
    "06": "Juni",
    "07": "Juli",
    "08": "Augusti",
    "09": "September",
    "10": "Oktober",
    "11": "November",
    "12": "December",
}

def presentFolders(FOLDERS):

    """ Presents folders to scan """

    sortedFolders = dict()

    for i, x in enumerate(sorted(FOLDERS.keys())):
        sortedFolders[str(i)] = x
        print(str(i) + ")", x)

    while True:
        try:
            scan_me = input("Folder to scan: ")
            scan_folder(FOLDERS, sortedFolders[scan_me])
            break
        except ValueError:
            print("Not a number. Try again.")
        except KeyError:
            print("Number not available. Choose another.")





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


def get_exif(fn):
    created = {"year": "NA", "month": "NA"}
    try:
        match = re.search("([0-9]*):([0-9]*)", Image.open(fn)._getexif()[306])
        created["year"] = match.group(1)
        created["month"] = MONTHS[match.group(2)]

    except TypeError:
        pass

    return created


def startSort(FOLDERS):
    """ Initiates the sort """
    images = []
    videos = []
    mime = magic.Magic(mime=True)

    if not os.listdir(FOLDERS["unsortedFolder"]):
        print("empty!")
    else:
        for dirname, dirnames, filenames in os.walk(FOLDERS["unsortedFolder"]):
            for filename in filenames:
                if "image" in mime.from_file(os.path.join(dirname, filename)):
                    images.append({
                            "image": os.path.join(dirname, filename),
                            "created": get_exif(os.path.join(dirname, filename))
                        })
                if "video" in mime.from_file(os.path.join(dirname, filename)):
                    videos.append({"video": os.path.join(dirname, filename)})

    print(images)
    print(videos)
