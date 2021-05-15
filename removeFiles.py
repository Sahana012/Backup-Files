import os
import datetime
import shutil

path = input("What path would you like to clear: ")
days = int(input("What is the day limit: "))

exist = os.path.exists(path)

if(exist == False):
    print("Please provide a valid path")
    path = input("What path would you like to clear: ")

if(os.path.isfile(path)):
    print("Please provide path of a directory")
    path = input("What path would you like to clear: ")


for root, dirs, files in os.walk(path, topdown=False):
    for file in files:
        fullPath = os.path.join(root, file)
        presentTime = datetime.datetime.now()
        file_cre_time = datetime.datetime.fromtimestamp(os.path.getctime(fullPath))
        no_of_days = (presentTime - file_cre_time).days
        if(no_of_days >= days):
            os.remove(fullPath)
            print("Your computer is now clean without any unwanted files!!")
    for i in dirs:
        fol_path = os.path.join(root, i)
        if len(os.listdir(fol_path)) == 0:
            shutil.rmtree(fol_path)
            print("Your computer is now clean without any unwanted files!!")