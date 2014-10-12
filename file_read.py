"""
These are some methods for reading and parsing files.
"""

def manage_line(line) :
    splitline = line.split()
    if int(splitline[1]) > int(splitline[2]) :
       print line
       return line

def funcread(fname) :
    #create a file handle so i can read the file
    f = open(fname, 'r')
    for line in f :
        #Here's where I do stuff...
        manage_line(line)

funcread('data1.txt')
