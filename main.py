import os
import time

os.system("clear")

# ==========| INSTALLER CUSTOMIZATION/SETTINGS |==========

global pkgName
pkgName = "Twoblade-Chatbot"

# Here, you add all the URLS of the files that need to be downloaded.
fileurls = ["https://raw.githubusercontent.com/emexos/ai_bot/refs/heads/main/index.js", "https://raw.githubusercontent.com/emexos/ai_bot/refs/heads/main/Bot/ai.js", "https://raw.githubusercontent.com/emexos/ai_bot/refs/heads/main/Bot/bot.js"]

# And here, you add the folders that each file should go into. If they should stay in the current directory, just put "./". (The position of the item in this list corresponds to the position of the item in the list above.)
folders = ["./", "./bot/", "./bot/"]


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
        os.system(f'curl --progress-bar -o "{folders[fileCount - 1]}/$(basename {file})" "{file}"')
        time.sleep(0.5)

installPrereqs()
