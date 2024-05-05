import re
import os
from pystyle import *

def deobfuscate_baum1810(con):
    return re.sub(r'%[^%]*%', '', con)

def deobfuscate_moom825(con):
    return con[8:]

def read_file(fn):
    try:
        with open(fn, 'r') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error reading file: {fn}")
        return None

def write_file(of, cc):
    try:
        with open(of, 'w') as file:
            file.write(cc)
    except IOError:
        print(f"Error writing to file: {of}")

def MM():
    os.system("cls")
    ascii = """
    ____        __       __    ____             __    ____
   / __ )____ _/ /______/ /_  / __ \___  ____  / /_  / __/ - github.com/ltcflip
  / __  / __ `/ __/ ___/ __ \/ / / / _ \/ __ \/ __ \/ /_   
 / /_/ / /_/ / /_/ /__/ / / / /_/ /  __/ /_/ / /_/ / __/  
/_____/\__,_/\__/\___/_/ /_/_____/\___/\____/_.___/_/     
                                                          
"""
    print(Colorate.Vertical(Colors.blue_to_cyan, ascii))
    cool = """
1. Baum1810 Deobfasuctor
2. Chinese Letters & Certutil & Moom825 & DeadCode\n
    """
    print(Colorate.Vertical(Colors.blue_to_cyan, cool))

def ho(opt):
    fn = input("> Enter filename: ")
    con = read_file(fn)
    if con is None:
        return True

    if opt == 1:
        cc = deobfuscate_baum1810(con)
        of = "deobfuscated_baum1810.txt"
    elif opt == 2:
        cc = deobfuscate_moom825(con)
        of = "deobfuscated_moom825.txt"
    else:
        print("Invalid option. Please try again.")
        return True

    write_file(of, cc)
    print(f"Deobfuscated content saved to {of}")
    return True

def main():
    while True:
        MM()
        opt = int(input("> Enter your choice: "))
        if not ho(opt):
            break

if __name__ == "__main__":
    main()
