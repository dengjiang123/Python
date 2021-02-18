import MySQLdb

db=MySQLdb.connect("localhost","root","111111","de")
cursor=db.cursor()
#cursor.execute("drop testdb;")
f=open("56167.txt","r")
x=[]
t=f.readline()
while t:
    b=t.split()
    a=[]
    a.append(b[0])
    a.append(b[1])
    a.append(b[2])
    a.append(b[3])
    a.append(b[4]+"-"+b[5]+"-"+b[6])
    a.append(b[7])
    a.append(b[8])
    a.append(b[9])
    a.append(b[10])
    a.append(b[11])
    a.append(b[12])
    x.append(a)
    t = f.readline()
sql_insertdb="""CREATE TABLE testdb1(
         id INT NOT NULL AUTO_INCREMENT,
         aa INT,
         ab INT,
         ac INT,
         ad INT,
         date_time  datetime NOT NULL DEFAULT CURRENT_TIMESTAMP(),
         ae INT,
         af INT,
         ag INT,
         ah INT,
         ai INT,
         aj INT,
         PRIMARY KEY(id))
        """
#cursor.execute(sql_insertdb)
insertsql="insert into testdb1(aa,ab,ac,ad,date_time,ae,af,ag,ah,ai,aj) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

for i in x:
    param=(str(i[0]),str(i[1]),str(i[2]),str(i[3]),str(i[4]),str(i[5]),str(i[6]),str(i[7]),str(i[8]),str(i[9]),str(i[10]))
    cursor.execute(insertsql,param)
cursor.execute("select * from testdb1;")
for i in cursor.fetchall():
    print(i)
db.commit()
db.close()
