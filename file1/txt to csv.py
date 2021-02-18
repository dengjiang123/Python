import os
import csv
os.system("dir /a /b *.txt > temp.txt")

def to_csv(file):
    csv_name=file[:-3]+"csv"
    csvfile=open(csv_name,"w",newline="")
    writer=csv.writer(csvfile)
    x=[]
    with open(file) as f:
        for i in f:
            x=(i.strip("\n")).split()
            writer.writerow(x)
    csvfile.close()


with open("temp.txt","r") as file:
    for i in file:
        if ((i.strip("\n"))!="temp.txt"):
            to_csv(i.strip("\n"))



'''
import csv
file=csv.reader(open("test.csv"))
for i in file:
    print(i[0],i[1],i[2])
'''

'''
with open("test.csv") as f:
    for line in f:
        print(line.strip("\n"))
'''