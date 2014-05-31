#/****************************************************************/ 
# Program:  DierectorySnapshot
# Version:  1.0
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
#    4. Help
#    5. Exit
#    --------------------------------------------------
#
#  
# License:
# 
# Open source software being distributed under GPL license. For more information see here:
# http://www.gnu.org/copyleft/gpl.html. 
# 
# Can edit and redistribute code as long as above reference of authorship is kept within the code.
#/****************************************************************/

import os, sys, pickle, difflib



def printList(snap_list):
    index = 1
    
    if len(snap_list) > 20:
        for item in snap_list:
            print("\t\t" + item)
            
            if (index % 3 == 0):
                print("\n")
            index = index + 1
    else:
        for item in snap_list:
            print("\t" + item)
    return


def invalidMenuOperation():
    sys.stderr.write("INVLALID MENU CHOICE; PLEASE SELECT A VALID OPERATION!")
    input("Press [Enter] to continue...")
    return


def helpMe():
    os.system('clear')
    print('''
    --------------------------------------------------
    This tool enables you to create a directory snapshot which 
    will store the names of all the files and directories under
    specified directory.
    
    Run the program and select one of the following menu items:
    1. Create directory snapshot
    2, List directory snapshot files
    3. Compare directory snapshot files
    4. Help
    5. Exit
    ''')
    
    input("Press [Enter] to continue...")
    return


def snapshotDirExists():
        cwd = os.getcwd()
        folderExists = cwd.find("snapshots")
        
        folderExists2 = os.path.exists("snapshots")
        
        if (folderExists != -1 or folderExists2 == True):
            return True
        else:
            return False


def changeToSnapshotDir():
        cwd = os.getcwd()
        snapshot_dir = os.path.join(cwd, "snapshots")
    
        if(snapshotDirExists() == False):
            os.mkdir("snapshots")
            os.chdir(snapshot_dir)
        else:
            folderExists = cwd.find("snapshots")
            if(folderExists == -1):
                os.chdir(snapshot_dir)
            else:
                return

        return


def compareSnaps(filename1, filename2):
    
    filename1 = filename1 + ".snap"
    filename2 = filename2 + ".snap"
        
    added_dirs = []
    removed_dirs = []
    added_files = []
    removed_files = []
    
    try:
        changeToSnapshotDir()
        
        file1 = open(filename1, 'rb')
        dirs1 = pickle.load(file1)
        files1 = pickle.load(file1)
        file1.close()
        
        file2 = open(filename2, 'rb')
        dirs2 = pickle.load(file2)
        files2 = pickle.load(file2)
        file2.close()
        
    except:
        print("Errors encountered on accessing directory snapshot files!")
        input("Press [Enter] to continue...")
        return
    
    dirs_diff = list(difflib.unified_diff(dirs1, dirs2))
    files_diff = list(difflib.unified_diff(files1, files2))
    
    for file in files_diff:
        if file.find("\n") == -1:
            if file.startswith("+"):
                file = file.strip("+")
                added_files.append(file)
            elif file.startswith("-"):
                file = file.strip("-")
                removed_files.append(file)
                
    for file in dirs_diff:
        if file.find("\n") == -1:
            if file.startswith("+"):
                file = file.strip("+")
                added_dirs.append(file)
            elif file.startswith("-"):
                file = file.strip("-")
                removed_dirs.append(file)
                
    print("\n\nAdded Directories:\n")
    printList(added_dirs)
    
    print("\n\nAdded Files:\n")
    printList(added_files)
    
    print("\n\nRemoved Directories:\n")
    printList(removed_dirs)
    
    print("\n\nRemoved Files:\n")
    printList(removed_files)
    
    input("Press [Enter] to continue...")
    return
    

def createSnap(directory, filename):
    all_dirs = []
    all_files = []
    
    for root, dirs, files in os.walk(directory):
        all_dirs = all_dirs + dirs
        all_files = all_files + files
        
    try:
        if(snapshotDirExists() == False):
            os.mkdir("snapshots")
            
        changeToSnapshotDir()
        
        snapFile = open(filename, 'wb')
        pickle.dump(all_dirs, snapFile, -1)
        pickle.dump(all_files, snapFile, -1)
        snapFile.close()
        
    except:
        print("Errors on attempting to save directory snapshot file!")
        
    
    input("Press [Enter] to continue...")
    return


def listSnaps():
    try:            
        changeToSnapshotDir()
    
        snap_list = []
        file_list = os.listdir(os.curdir)
    
        for item in file_list:
            if item.find(".snap") != -1:
                snap_list.append(item)
            
        print('''
    Directory Snapshot List:
    --------------------------------------------------
    ''')
            
        printList(snap_list)
    
    except:
        print("Errors encountered on accessing directory snapshot files!")
        input("Press [Enter] to continue...")
        return

    input("\nPress [Enter] to continue...")
    return






