#!/usr/bin/python
import pymysql
con = pymysql.connect('webvrdev.pro.izobretarium.ru', 'energo','zPMoL8HB', 'energo')

cur = con.cursor()
cur.execute("SELECT * FROM objects")

for row in rows:
        print(str(row[0])+"\t"+str(row[1])+"\t"+str(row[2])+"\t"+str(row[3])+"\t"+str(row[4])+"\t"+str(row[5])+"\t"+str(row[6])+"\t"+str(row[7])+"\t"+str(row[8]))
