import json
import sys
import os
import shutil
import fnmatch



def check4Folders(listed, fltype, MFolder = ''):


    if fltype == 'game':
        #Checks for if the folder created is a main folder - if it is then it continues lmoa that's what an if statement does hope that helps 
        folderList = []
        #This is for debugging purposes
        #print(listed)
        for item in os.listdir('.'):
            #checks for folder in the folder the script you ran is in.
            if os.path.isdir(item):
                folderList.append(item)
        folderList.remove('Configuration')
        #removes the configuration folder as that isn't for games lmao
        try:
            #This is here so that It's easier for me to use...
            folderList.remove('.git')
        except FileNotFoundError:
            ''#print("you aren't the creator, my bad!")
        for folder in folderList:
            if folder not in listed:
                #this checks for if it is in the .json file, if it is, then it's accepted as normal, if it isn't it will ask you to set it up and what you want it to do.
                print(f"found new folder {folder}")
                makeFolder(fltype, folder, listed)




    elif fltype == 'sub':
        #Checks for if the folder is a desginated "sub folder", if it is, it continues, as that's what if statements do.
        subfolders = listed['subs']
        folderList = []
        #print(listed) Debug stuff
        for item in os.listdir(f'./{MFolder}'):
            #runs this while there are "items" in the "main folder", or "MFolder", for short!
            #print(item) Debug stuff
            if os.path.isdir(f'./{MFolder}/{item}'):
                folderList.append(item)
        #print(folderList) Debug Stuff
        for folder in folderList:
            if folder not in subfolders:
                #if the folder isn't listed in the json, it asks you to set it up!
                print(f"found new folder {folder}")
                makeFolder(fltype, folder, listed)

def makeFolder(foldertype, name, listed):
    # This is for making the folder for when the function up above this comment is triggered.
    if foldertype == 'game':
        listed[name] = {}  #This variable is made for creating the folder
        direct = input(f"please enter the directory for {name}\n")
        while not os.path.isdir(direct):
            #this is a check for actually submitting a directory.
            print("That is not a valid directory.\n")
            direct = input(f"please enter the directory for {name}\n")
        
        ## All the things down here are set-up for sub-folders, nothing more, nothing less
        listed[name]['directory'] = direct
        listed[name]['subs'] = []
        listed[name]['actions'] = {}
        listed[name]['directories'] = {}


        f = open('folders.json', 'w')
        json.dump(data, f, indent = 4)
        f.close()
        ##Opens the JSON file to dump the new information and then dumps it immedietly 

    if foldertype == 'sub':
        #creation of subfolders
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
            #"foldreplacement" replaces items with items of the same name when moving stuff to the directory that is requested.
        elif action == '2':
            action = 'fileMove'
            #"filemove" just moves an item permanantly
        #print(listed) debug stuff

        #making items for the JSON
        listed['directories'][name] = direct
        listed['actions'][name] = action
        listed['subs'].append(name)


        f = open('folders.json', 'w')
        json.dump(data, f, indent = 4)
        f.close()
        #dumps new information inside the JSON for safe keeping!

def actionComplete(action, dest, selection):
    #this function is used when you actually do something with something already created.

     #"foldreplacement" replaces items with items of the same name when moving stuff to the directory that is requested.
    if action == 'foldReplacement':
        itemList = os.listdir(selection)
        for file in itemList:
            if os.path.exists(f"{dest}\\{file}"):
                os.remove(f"{dest}\\{file}")
            shutil.copy2(f"{selection}\\{file}", f"{dest}\\{file}")

    #"filemove" just moves an item permanantly
    elif action == 'fileMove':
        shutil.copy2(f"{selection}", f"{dest}")
        


f = open('./Configuration/folders.json')
data = json.load(f)
f.close()
type(data)


print("Thank you for downloading Neeko's All-Purpose Manager\nif you have any issues that you'd like to report, please post them to the github. \n\nThank you!")
