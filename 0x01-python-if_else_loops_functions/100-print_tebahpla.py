#!/usr/bin/python3

for j in range(90, 64, -1):
    if j % 2 == 1:
        print("{}".format(chr(j).upper()), end="")
    else:
        print("{}".format(chr(j).lower()), end="")
