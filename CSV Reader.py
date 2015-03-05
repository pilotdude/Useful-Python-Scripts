__author__ = 'Charlie'

# The Goal of this script is to read from a CSV file and
# produce a double nested list

import csv # don't forget your import statement

def readCSV(filelocation):
    '''filelocation should be the directory of a file that
        you want to read inputted as a string. If the file
        is in the same direcotry then you can just input
        the filename.
    '''

    #try to convert the filename to a string, in case it wasn't already
    try:
        filelocation = str(filelocation)
    except:
        return print('please pass in a valid file location string')

    #The following is a slightly modifyied version of the code in HW4 skeleton
    f = open(filelocation)
    reader = csv.reader(f)

    #read in data, convert to ints where possible, leave as strings otherwise
    data = []
    for i in reader:
        temp = []
        for j in i:
            try:
                j = int(j)
                temp.append(j)
            except:
                temp.append(j)
        data.append(temp)

    return data
