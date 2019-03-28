import json
import sys
import os
import shutil
import fnmatch

def check4Folders(listed, fltype):
    folderList = []
    for item in os.listdir('.'):
        if os.path.isdir(item):
            folderList.append(item)
    for folder in folderList:
        if folder not in listed:
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
        listed[name]['actions'] = {}
        listed[name]['directories'] = {}
        f = open('folders.json', 'w')
        json.dump(data, f, indent = 4)
        f.close()
    if foldertype == 'sub':
        ''
        




f = open('folders.json')
data = json.load(f)
f.close()
type(data)


print("Thank you for downloading Neeko's All-Purpose Manager\nif you have any issues that you'd like to report, please post them to the github. \n\nThank you!")
while True:
    print('checking for new folders')
    Folders = data['Folders']
    check4Folders(Folders, 'game')
    decide = input(f"\nWhich Main? [Enter nothing to check for new folders]\n\n" + ', '.join(Folders) + '\n\n')
    if decide in Folders:
        while decide != '':
            Folders = data['Folders'][decide]
            check4Folders(Folders, 'sub')



