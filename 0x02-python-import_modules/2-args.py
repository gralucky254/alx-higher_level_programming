#!/usr/bin/python3

import sys

if __name__ == "__main__":
    num_args = len(sys.argv) - 1
    
    if num_args == 0:
        print("Number of argument(s): 0.")
    elif num_args == 1:
        print("Number of argument(s): 1. Argument: {}.".format(sys.argv[1]))
    else:
        print("Number of argument(s): {}. Arguments:".format(num_args))
        for i, arg in enumerate(sys.argv[1:], start=1):
            print("{}. {}".format(i, arg))
