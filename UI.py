startfile = './Configuration/Grab.py'

import os
import sys
sys.path.append(os.path.dirname(os.path.expanduser(startfile)))
import Grab
from Grab import data


while True:
    print('checking for new folders')
    Folders = data['Folders']
    Grab.check4Folders(Folders, 'game')
    decide = input(f"\nWhich Main? [Enter nothing to check for new folders]\n\n" + ', '.join(Folders) + '\n\n')
    if decide in Folders:
        while decide != '':
            initialDecide = decide
            subdata = data['Folders'][decide]
            Folders = data['Folders'][decide]['subs']
            Grab.check4Folders(subdata, 'sub', decide)
            decide = input("I'm assuming you know what these do, so I'll display what I can see.\n[press ? to search for new folders]\n\n" + ', '.join(Folders) + '\n\n')
            if decide in Folders:
                selection = None
                selectionlist = os.listdir(f'./{initialDecide}/{decide}')
                while selection not in selectionlist:
                    selection = input("Please select a skintype\n\n" + ", ".join(selectionlist) + "\n\n")
                destination = data['Folders'][initialDecide]['directory'] + subdata['directories'][decide]
                Grab.actionComplete(subdata['actions'][decide], destination, f'./{initialDecide}/{decide}/{selection}')
                print("Alrighty! Done! Going back to main.")
                decide = initialDecide
                break
            else:
                decide = initialDecide