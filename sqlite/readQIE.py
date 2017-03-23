import sqlite3 as lite
import pandas as pd

con = lite.connect('qieCalibrationParameters_0x04000000_0xeacd8870.db')

qieID = 1
shunt = 2
capID = 0
range = 0

# print sqlite version and check connection
with con:
    
    cur = con.cursor()    
    cur.execute('SELECT SQLITE_VERSION()')
    
    data = cur.fetchone()
    
    print "SQLite version: %s" % data  

# print tables
cursor = con.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())

# dump all the tables
#with open('dump.sql', 'w') as f:
#    for line in con.iterdump():
#        f.write('%s\n' % line)

# CREATE TABLE qieshuntparams(id STRING, serial INT, qie INT, capID INT, range INT,
# shunt INT, directoryname STRING, date STRING    , slope REAL, offset REAL, 
#uncertainty REAL);

with con:    
    
    cur = con.cursor()    
    cur.execute("SELECT * FROM qieshuntparams")

    rows = cur.fetchall()

    for row in rows:
        
        #print row
        if qieID == row[2] and capID == row[3] and range == row[4] and shunt == row[5]:
            print row[8]
