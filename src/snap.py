#/****************************************************************/ 
# Program:  DierectorySnapshot
# Version:  2.0
# Date:     05/31/2014
# Website:  http://www.HumairAhmed.com
#
# Developer(s):   Humair Ahmed 
#
#
# Program allows you to take a detailed inventory or snapshot of a directory and 
# automatically stores the information or tree hierarchy to a ".snap" file. It 
# then allows you to compare several '.snap' files and display any differences in 
# terms of added or removed sub-directories or files. Below is example output when 
# the program is started.
#
#
# Ex:
#
#    --------------------------------------------------
#    Please select a number and press enter:
#    
#    1. Create directory snapshot
#    2, List directory snapshot files
#    3. Compare directory snapshot files
#    4. Settings
#    5. Help
#    6. Exit
#    --------------------------------------------------
#
# Selecting #4 above leads you to another submenu where you can setup FTP, so, upon 
# creation, '.snap' files are uploaded to a FTP server. Below is the submenu.
#
#   --------------------------------------------------
#    Please select a number and press enter:
#    
#    1. Change local folder to automatically save '.snap' files to
#    2. Setup FTP to automatically upload '.snap' files to FTP server
#    3. Disable FTP upload (will delete all saved FTP information)
#    4. Return to main menu
#    --------------------------------------------------
#  
# License:
# 
# Open source software being distributed under GPL license. For more information see here:
# http://www.gnu.org/copyleft/gpl.html. 
# 
# Can edit and redistribute code as long as above reference of authorship is kept within the code.
#/****************************************************************/

import os, snaphelper

global programDir

#menu function
def createMenu():
    os.system('clear')
    print('''
    --------------------------------------------------
    Please select a number and press enter:
    
    1. Create directory snapshot
    2, List directory snapshot files
    3. Compare directory snapshot files
    4. Settings
    5. Help
    6. Exit
    --------------------------------------------------''')
    
    action = input("\t")
    
    return action


def createSubmenu():
    os.system('clear')
    print('''
    --------------------------------------------------
    Please select a number and press enter:
    
    1. Change local folder to automatically save '.snap' files to
    2. Setup FTP to automatically upload '.snap' files to FTP server
    3. Disable FTP upload (will delete all saved FTP information)
    4. Return to main menu
    --------------------------------------------------''')
    
    action = input("\t")
    
    return action


def main():
    programDir = os.getcwd()
    
    
    menu_selection = ""
    
    while menu_selection != "6":
        menu_selection = createMenu()
        
        if (menu_selection == "1"):
            os.system('clear')
            
            snap_directory = input("Enter directory path of the directory to take a snapshot of: ")
            snap_filename =  input("Enter name of directory snapshot file to create: ")
            
            snaphelper.createSnap(snap_directory, snap_filename)
            
        elif (menu_selection == "2"):
            os.system('clear')
            snaphelper.listSnaps()
            
        elif (menu_selection == "3"):
            os.system('clear')
            file1 = input("Enter the filename of snapshot 1: ")
            file2 = input("Enter the filename of snapshot 2: ")
            
            snaphelper.compareSnaps(file1, file2)
            
        elif (menu_selection == "4"):
            submenu_selection = ""
            
            while (submenu_selection != "4"):
                submenu_selection = createSubmenu()
                
                if (submenu_selection == "1"):
                    print("This feature has not yet been implemented!")
                    input("\nPress [Enter] to continue...")
                    
                elif (submenu_selection == "2"):
                    os.system('clear')
                    snaphelper.setupFTP(programDir)
                    
                elif (submenu_selection == "3"):
                    os.system('clear')
                    snaphelper.disableFTP(programDir)
                    
                else:
                    if menu_selection != "4":
                        snaphelper.invalidMenuOperation()
            
        elif menu_selection == "5":
            snaphelper.helpMe()
            
        else:
            if menu_selection != "6":
                snaphelper.invalidMenuOperation()
            
    
if __name__ == "__main__":
    main()
