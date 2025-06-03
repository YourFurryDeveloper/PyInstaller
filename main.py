import os
import time

os.system("clear")

# ==========| INSTALLER CUSTOMIZATION/SETTINGS |==========

global pkgName
pkgName = "Your Package Name"

# Here, you add all the URLS of the files that need to be downloaded.
fileurls = []

# And here, you add the folders that each file should go into. If they should stay in the current directory, just put "./". (The position of the item in this list corresponds to the position of the item in the list above.)
folders = []

sudoRequired = False

# ========================================================

def setLoadBar(loadprog):
    progLeft = 100 - loadprog
    print(f"{int(loadprog / 100 * 100)}% [{"#" * loadprog}{"-" * progLeft}]\n")

def installPrereqs():
    fileCount = 0
    setLoadBar(0)
    for file in fileurls:
        fileCount += 1
        os.system("clear")
        print(f"Installing {pkgName}\n")
        setLoadBar(int(100 / len(fileurls) * fileCount))
        print(f"\nGetting {file}...")
        os.makedirs(folders[fileCount - 1], exist_ok=True)
        if sudoRequired: os.system(f'sudo curl --progress-bar -o "{folders[fileCount - 1]}/$(basename {file})" "{file}"')
        else: os.system(f'curl --progress-bar -o "{folders[fileCount - 1]}/$(basename {file})" "{file}"')
        #time.sleep(0.5)
    print(f"\nFinished installation of {pkgName}.")

#input(f"Press enter to begin installation of {pkgName} > ")
installPrereqs()
