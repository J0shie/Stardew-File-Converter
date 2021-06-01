import os
import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory

def changeDirectory():
    root = tk.Tk()
    root.withdraw()
    directory = askdirectory()
    directoryTxtFile = open("directories.txt", "w")
    directoryTxtFile.write(directory)
    directoryTxtFile.close()
    xd = int(input("\nWould you like to convert a file now?\nChoose 1 to convert.\nChoose 2 to close.\n"))
    if xd == 1:
        mainScript()
    else:
        exit()

def mainScript():
    root = tk.Tk()
    root.withdraw()
    filename = askopenfilename()
    
    with open(filename, 'r') as save:
            saveData = save.read()

    # switch save
    if '<gameVersion>1.5.4.1' in saveData:
        saveData = saveData.replace('<gameVersion>1.5.4.1', '<gameVersion>1.5.4')
        with open("directories.txt", 'r') as file:
            directory = file.read()
            try:
                newFile = open(directory + "/" + os.path.basename(filename), "x")
                newFile.write(saveData)
                newFile.close()
                print('\nData has been converted from Switch to PC!')
                os.system("pause")
            except FileExistsError:
                print("\nThere is already a file in this location!\n")
                startingSequence()
    # pc save
    elif '<gameVersion>1.5.4' in saveData:
        saveData = saveData.replace('<gameVersion>1.5.4', '<gameVersion>1.5.4.1')
        with open("directories.txt", 'r') as file:
            directory = file.read()
            try:
                newFile = open(directory + "/" + os.path.basename(filename), "x")
                newFile.write(saveData)
                newFile.close()
                print('\nData has been converted from PC to Switch!')
                os.system("pause")
            except FileExistsError:
                print("\nThere is already a file in this location!\n")
                startingSequence()                
        
    else:
        print('\nThat is not a valid Stardew Valley save file.')
        os.system("pause")
        
def startingSequence():
    x = int(input("Choose 1 to convert your file.\nChoose 2 to change/create your save path.\n"))

    if x == 1:
        mainScript()
    elif x == 2:
        changeDirectory()
    else:
        print("\nThat is not a valid choice.")
        os.system("pause")

startingSequence()
