import os 
from prettytable import PrettyTable

def main():
    # get a directory as user input
    directory = getDirectory()

    # create a dictionary to store folder and displayname
    dictionary = getFolderDisplayName(directory)

    table = makeTable(dictionary)
    print(table)

def getDirectory():
    directory = None
    while not directory:
        directory = input("Enter ReportName.Report directory path: ")
        if not isDirectory(directory):
            directory = None
    directory += "/definition/pages/"
    return directory

def isDirectory(directory):
    if not os.path.exists(directory):
        print("Invalid directory path")
        return False
    return True

def getFolderDisplayName(directory):
    dictionary = {}
    for folder in os.listdir(directory):
        if os.path.isdir(directory + folder):
            dictionary[folder] = getDisplayName(directory + folder)
    return dictionary

def getDisplayName(folder):
    # get displayName from page.json in the folder
    displayName = ""
    try:
        with open(folder + "/page.json") as file:
            data = file.read()
            displayName = data.split('"displayName":')[1].split(',')[0].strip().strip('"')
    except:
        pass
    return displayName

def makeTable(dictionary):
    table = PrettyTable()
    table.field_names = ["Folder", "Display Name"]
    for folder in dictionary:
        table.add_row([folder, dictionary[folder]])
    return table

if __name__ == "__main__":
    main()


