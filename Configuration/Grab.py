import json
import sys
import os
import shutil
import fnmatch

def check4Folders(listed, fltype, MFolder = ''):
    if fltype == 'game':
        folderList = []
        print(listed)
        for item in os.listdir('.'):
            if os.path.isdir(item):
                folderList.append(item)
        folderList.remove('Configuration')
        try:
            folderList.remove('.git')
        except FileNotFoundError:
            ''#print("you aren't the creator, my bad!")
        for folder in folderList:
            if folder not in listed:
                print(f"found new folder {folder}")
                makeFolder(fltype, folder, listed)
    elif fltype == 'sub':
        subfolders = listed['subs']
        folderList = []
        print(listed)
        for item in os.listdir(f'./{MFolder}'):
            print(item)
            if os.path.isdir(f'./{MFolder}/{item}'):
                folderList.append(item)
        print(folderList)
        for folder in folderList:
            if folder not in subfolders:
                print(f"found new folder {folder}")
                makeFolder(fltype, folder, listed)

def makeFolder(foldertype, name, listed):
    if foldertype == 'game':
        listed[name] = {}
        direct = input(f"please enter the directory for {name}\n")
        while not os.path.isdir(direct):
            print("That is not a valid directory.\n")
            direct = input(f"please enter the directory for {name}\n")
        
        listed[name]['directory'] = direct
        listed[name]['subs'] = []
        listed[name]['actions'] = {}
        listed[name]['directories'] = {}
        f = open('folders.json', 'w')
        json.dump(data, f, indent = 4)
        f.close()
    if foldertype == 'sub':
        print(f"found a new subfolder: {name}")
        direct = input("where does this go? [IN CONTEXT OF WHERE THE MAIN FOLDER GOES]\n\n")
        action = input("what type of action will be preformed in this folder?\n"
        "[1] Pack Replacement (entire folders will be moved and stored here) \n[2] File Replacement (Files will be moved and stored here)\n")
        while action != '1' and action != '2':
            print("please use the numbers by each type of action. \n\n")
            action = input("what type of action will be preformed in this folder?\n"
        "[1] Pack Replacement (entire folders will be moved and stored here) \n[2] fileMove (Files will be moved and stored here)\n")
        if action == '1':
            action = 'foldReplacement'
        elif action == '2':
            action = 'fileMove'
        print(listed)
        listed['directories'][name] = direct
        listed['actions'][name] = action
        listed['subs'].append(name)
        f = open('folders.json', 'w')
        json.dump(data, f, indent = 4)
        f.close()

def actionComplete(action, dest, selection):
    if action == 'foldReplacement':
        itemList = os.listdir(selection)
        for file in itemList:
            if os.path.exists(f"{dest}\\{file}"):
                os.remove(f"{dest}\\{file}")
            shutil.copy2(f"{selection}\\{file}", f"{dest}\\{file}")
    elif action == 'fileMove':
        shutil.copy2(f"{selection}", f"{dest}")
        


f = open('./Configuration/folders.json')
data = json.load(f)
f.close()
type(data)


print("Thank you for downloading Neeko's All-Purpose Manager\nif you have any issues that you'd like to report, please post them to the github. \n\nThank you!")