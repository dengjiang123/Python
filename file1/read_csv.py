import csv

csv_name="56038.csv"
with open(csv_name) as csvfile:
    rows=csv.reader(csvfile)
    for row in rows:
        for i in row:
            print(i,end=" ")
        print()