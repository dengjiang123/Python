import csv

str_name="56038.txt"
csv_name=str_name[:-3]+"csv"
csvfile=open(csv_name,"w",newline="")
writer=csv.writer(csvfile)

with open("56038.txt") as f:
    for i in f:
        x=(i.strip("\n").split())
        writer.writerow(x)

csvfile.close()