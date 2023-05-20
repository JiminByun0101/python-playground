import sqlite3
import sys
from generate_csv import generate_csv
# from modules import generate_csv

# adding modules to the path
# sys.path.insert(0, '/home/jade/src/python-playground/modules')


'''
CREATE TABLE data (
    id INTEGER AUTO_INCREMENT,
    time datetime DEFAULT current_timestamp,
    name char(100),
    kor INTEGER,
    eng INTEGER,
    math INTEGER,
    grade char(1),
    PRIMARY KEY (id)
)
'''

# Name of the SQLite database File
DB_FILE = 'grade.db'

# Connect to the SQLite database
conn = sqlite3.connect(DB_FILE)

# Create a cursor object to execute SQL commands
cur = conn.cursor()

# Create a table
try:     
    cur.execute("DROP TABLE IF EXISTS grades")
    cur.execute('''CREATE TABLE grades (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        time datetime DEFAULT current_timestamp,
        name char(100),
        kor INTEGER,
        eng INTEGER,
        math INTEGER,
        grade char(1)
        )''')
    # Commit the changes to the database
    conn.commit()
except:
    conn.rollback()
    conn.close()
    sys.exit('Failed to create table')

num_rows = 100
generate_csv(num_rows, "kor", "eng", "math")

with open("generated_csv_100_rows.csv", "r", encoding="utf-8") as f:
    if not f:
        conn.close()
        sys.exit('Failed to open the generated CSV file')
    # print(f.readlines())
    print(f.readline())

    for line in f:
        line = line.strip()
        name, kor, eng, math, grade = line.split(',')
        print(name, kor, eng, math, grade)
        try:
            cur.execute("INSERT INTO grades (name, kor, eng, math, grade) VALUES (?,?,?,?,?)", (name, kor, eng, math, grade))
        except:
            conn.rollback()
            conn.close()
            sys.exit('Failed inserting data')

conn.commit()

try: 
    # cur.execute("SELECT * FROM grades WHERE grade = 'A' and kor > 90 and math > 90")
    cur.execute("SELECT * FROM grades WHERE grade = 'F'")
    # cur.execute("SELECT * FROM grades")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    
    print("All rows with grade 'A' and Korea and Math greater than 90: ", len(rows))
    print(rows)
except:
    conn.rollback()
    conn.close()
    sys.exit('Failed selecting data')
    
conn.close()
print('Done')
    
    
