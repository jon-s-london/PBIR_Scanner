import os 
from prettytable import PrettyTable

def main():

    # get a directory as user input
    directory = None
    while not directory:
        directory = get_directory()
        # check if the directory exists
        if os.path.exists(directory):
            print("The directory exists!")
        else:
            print("The directory does not exist!")
            directory = None
    directory += "/definition/pages/"

    # create a dictionary to store folder and displayname
    dictionary = {}

    # Iterate into each folder in the directory, open page.json and get displayName from json object
    for folder in os.listdir(directory):
        if os.path.isdir(directory + folder):
            with open(directory + folder + "/page.json") as f:
                data = f.read()
                # add folder and diasplayname to the dictionary
                dictionary[folder] = data.split('"displayName": "')[1].split('"')[0]

    # create a table with folder and displayname using PrettyTable
    table = PrettyTable()
    table.field_names = ["Folder", "DisplayName"]
    for key, value in dictionary.items():
        table.add_row([key, value])

    print(table)

def get_directory():
    return input("Enter ReportName.Report directory path: ")

if __name__ == "__main__":
    main()


