#!/usr/bin/python3

#############################################################################################
#                               Program by Mohammed Faisal Khan                             #
#                               Email: faisalkhan91@outlook.com                             #
#                               Date: 09/11/2019                                            #
#############################################################################################

# Importing system module

import sys
import re
import sqlite3

import time
import datetime
import random

# Function Definitions


# Function to check if the filename was given, if not ask the user to input file(s)
def check_files(filename):

    if not filename:
        print("File name not specified.")
        filename = input("Please enter name of data file(s): ")
        file_list = filename.split()
        return file_list
    else:
        return filename


# Function to read in the file contents if the file exists
def read_file(filename=""):

    # File exist error handling - http://www.diveintopython.net/file_handling/index.html
    try:
        current_file = open(filename, "r", encoding="utf8")
    except IOError:
        print("File does not exist.")
        return "Nothing to print."

    # Split lines - http://stackoverflow.com/questions/15233340/getting-rid-of-n-when-using-readlines
#    content = current_file.read().splitlines()
    content = current_file.read()
    current_file.close()

    return content


def find_time_traveller(text_input):

    traveller = re.findall("Time Traveller", data)
    print(traveller)

    regex = re.compile(r"")

    newline = re.sub(regex, 'wordtoreplace', text_input)
    return traveller


def database(traveller_info):

    c.execute('CREATE TABLE IF NOT EXISTS travellerlogs(unix REAL, datestamp TEXT, location TEXT, who TEXT)')
    c.execute('INSERT INTO travellerlogs VALUES(24051991, "2016-01-01", "Manama", 1)')

    locations = ["London", "Berlin", "Zurich", "NewYork", "Moscow", "Vienna", "Boston", "Los Angeles", "Dubai", "Paris",
                 "Mumbai", "Melbourne"]

    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
    location = random.choice(locations)
    traveller = random.choice(traveller_info)

    c.execute("INSERT INTO travellerlogs (unix, datestamp, location, who) VALUES (?, ?, ?, ?)",
              (unix, date, location, traveller))

    conn.commit()


def read_from_db():

    c.execute('SELECT * FROM travellerlogs WHERE location == "London"')
    # data = c.fetchall()
    # print(data)
    for row in c.fetchall():
        print(row[0])

#############################################################################################

# Main Program

# Command line argument to take names of files as input
files = sys.argv[1:]

files = check_files(files)
# print("Files: ", files)

# Loop to process multiple files
for file in files:
    print("\n###################################", file, "###################################", end="\n")
    data = read_file(file)
#    print(data)

    # Connect to database
    # SQLlite type: REAL, INT, TEXT, BLOB, None/Null(?)
    conn = sqlite3.connect("Traveller.db")
    c = conn.cursor()

    time_traveller = find_time_traveller(data)
    read_from_db()

    # for i in range(10):
    #     database(time_traveller)
    #     # For time stamp to go up one sec
    #     time.sleep(1)

    # Close connection to database
    c.close()
    conn.close()

#############################################################################################
#                                       End of Program                                      #
#                                       Copyright 2019                                      #
#############################################################################################
