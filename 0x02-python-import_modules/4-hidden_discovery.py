#!usr/bin/python3
if __name__ == "__main__":
    from hidden_4 import *

a = dir()
for i in range(0, len(a)):
    if a[i][0:1] != "_":
        print("{}".format(a[i]))
