# Author: Brian McKiernan
# Netid: bbm30
# Date 101217
# Project 3
import sys
import subprocess
import re



# Calls the R system specifying that commands come from file commands.R
# The commands.R provided with this assignment will read the file named
# data and will output a histogram of that data to the file pageshist.pdf
def runR( ):
    res = subprocess.call(['R', '-f', 'commands.R'])

# log2hist analyzes a log file to calculate the total number of pages
# printed by each user during the period represented by this log file,
# and uses R to produce a pdf file pageshist.pdf showing a histogram
# of these totals.  logfilename is a string which is the name of the
# log file to analyze.
#

# My log2hist function also prints out the users and pages to the terminal in
# alphabetical order
def log2hist(logfilename):
    dict = { }
    f = open(logfilename, 'r')
    for line in f:
        match = re.search(r'user:\s+(\w+)\s', line)
        if match:
            match2 = re.search(r'pages:\s+(\d+)\s', line)
            if match2:
                if match.group(1) in dict:
                    dict[match.group(1)] = (dict.get(match.group(1)) + int(match2.group(1)))
                else:
                    dict[match.group(1)] = int(match2.group(1))
            else:
                continue
        else:
            continue
    f.close()
    fd = open('data', 'w')
    for key in sorted(dict.keys()):
        print 'User:', key, 'printed', dict[key], 'pages.'
        output_string = (str(dict[key]) + '\n')
        fd.write(output_string)
    fd.close()
    runR()
    return

if __name__ == '__main__':
    log2hist(sys.argv[1])   # get the log file name from command line

# line above may be changed to log2hist("log") to make the file name
#    always be log
