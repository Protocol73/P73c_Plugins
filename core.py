import os

def termClear(): #clear the Screen
    os.system('cls' if os.name=='nt' else 'clear')