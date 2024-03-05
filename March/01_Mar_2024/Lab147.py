# CSV file
import csv

with open("mydata.csv") as csvfile: #if we want to open file, no need to give "r" in syntax
    reader = csv.reader(csvfile) # reader will give you all rows
    for row in reader:
        print(row[0], row[1], row[2], sep="|")
