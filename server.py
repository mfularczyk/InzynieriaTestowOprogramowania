#!/usr/bin/python3

CRED = '\033[91m'
CGREEN = '\033[32m'
CBLUE = '\033[34m'
CEND = '\033[0m'

def menu():
    print("#1 Check clients status")
    print("#2 Execute tests")
    input_number = input(CBLUE + "Choose option: " + CEND)
    
    try:
        val = int(input_number)
        if(val == 1):
            print(CGREEN + "Checking clients statuses..." + CEND)
        elif(val == 2):
            print(CGREEN + "Executing tests..." + CEND)
        else:
            print(CRED + "Unknown option. Please insert correct number!" + CEND)
    except ValueError:
        print(CRED + "Only digits allowed ;)" + CEND)

menu()
