# a program that imports data from a CSV spreadsheet
from sys import argv, exit
import csv


# check if a csv file has been specified
if len(argv) != 2:
    print("Usage: import.py csvfile.csv")
    exit(1)

# Open CSV file given in the command line
with open(argv[1], newline = '') as csvfile:
    reader = csv.DictReader(csvfile)
#Create a new csv file with names separated
    with open("new_students.csv", "w",newline="") as students_csv:
        writer = csv.writer(students_csv)
        # Headers
        writer.writerow(['first','middle','last','house','birth'])
        # For each row parse name
        for row in reader:
            
            name = row["name"].split()
            if len(name) == 2:
                name.insert(1, '')
            #Name is now a list with an empty string in the middle
            #Insert keys into name list
            Name_key = ['first','middle','last']
            Name_dict = zip(Name_key, name)
            #convert into a dictinary  
            FullName = dict(Name_dict)
            #print(FullName)
            
            # Remove name column reader and merge it with FullName
            del row["name"]
            row = {**FullName, **row}
               
            # Write each row
            writer.writerow([row['first'], row['middle'], row['last'], row['house'], row['birth']])

# Insert each student into the students table name of students.db
 
