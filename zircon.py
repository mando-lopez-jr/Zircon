#!/usr/bin/env python3

import os
import sys

def main():
    lenargv = len(sys.argv)

    match sys.argv[1]:
        case 'install':
            install(lenargv)
        case other:
            print("Error: Invalid Input")
    

def install(length):
    for i in range(2, length):
        print("copying " + sys.argv[i])
        os.system("cp ~/dev/sample_repo/" + sys.argv[i] + " ~/dev/sample_bin")

main()