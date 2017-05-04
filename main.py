#!/usr/bin/env python3

"""
Main file.
Collect information, setup folderstructure and starts script
"""

import setup, os
import functions

# onlyfiles = next(os.walk(dir)) #dir is your directory path as string
# print (len(onlyfiles))

FOLDERS = {
    "baseFolder": "Result",
    "finishedFolder": "Finished",
    "unfinishedFolder": "Unfinished",
    "videoFolder": "Video",
    "unsortedFolder": "Unsorted"
}



def menu():
    """ The main menu """
    print("""
    ##################################
    Welcome to the image sorter!
    ##################################

    Default foldernames: (Final will be, for example: Result/Finished, Result/Videos)
    ----------------------------------
    Base folder:            Result/
    Finished images:        Finished/
    Unfinished images:      Unfinished/
    Videos:                 Videos/
    Unsorted images:        Unsorted/
    """)

    print("1) Setup folders. Press Enter for default")
    print("2) View default FOLDER")
    print("3) Scan folder")
    print("4) Start the magic!")
    print("R) Remove baseFolder")
    print("q) Quit program")



def main():
    """ Main loop """

    while True:
        menu()
        choice = input("--> ")

        if choice == "q":
            print("Bye.")
            return

        elif choice == "1":
            setup.setup_folders(FOLDERS)

        elif choice == "2":
            for i in sorted(FOLDERS.keys()):
                print(i, "=", FOLDERS[i])

        elif choice == "3":
            print("\n### Available folders ###\n")
            functions.presentFolders(FOLDERS)

        elif choice == "4":
            # print("\n### Available folders ###\n")
            functions.startSort(FOLDERS)

        elif choice == "R":
            setup.remove_folder(FOLDERS["baseFolder"])


        else:
            print("Try again.")

        input("\nPress enter to continue...")

if __name__ == "__main__":
    main()
