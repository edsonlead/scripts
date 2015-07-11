#!/usr/bin/env python3
import re

filen = "Opt.180.com"

def convert_file(filen):
    try:
        filename = filen
        filename2 = filename[:-3]+"xyz"
        fopen = open(filename, 'r')
        fopen2 = open(filename2,'w')
        fread = fopen.read()
        regex = re.compile("[A-Z]  .*[0-9]")
        r2 = regex.findall(fread)
        result = len(r2)
        result = str(result)
        fopen2.write(result+"\n\n")
        for i in r2:
                fopen2.write(i+"\n")
        fopen2.write("\n")
        fopen.close()
        fopen2.close()
        return 1
    except IOError:
        print("ERROR! Could not open file >> \"{0}\" <<".format(filen))

convert_file(filen)
