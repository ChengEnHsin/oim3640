# Read entire file
with open('data.txt', "r") as f:
    #text = f.read()
    text = f.readlines()  # returns a list of lines
print(text)

# Read line by line (best for large files)
with open('data.txt', "r") as f:
    for line in f:
        print(line.strip())  # strip() removes \n

# Write to file ('w' = overwrite, 'a' = append)
with open('data/s20_output.txt', 'w') as f:
    f.write('Hello, World!\n')

    import csv

# Read CSV (each row becomes a dict)
with open('students.csv') as f:
    for row in csv.DictReader(f):
        print(f"{row['name']}: {row['grade']}")

# Write CSV
data = [{'name': 'Alice', 'grade': 95},
        {'name': 'Bob', 'grade': 87}]
with open('output.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['name', 'grade'])
    writer.writeheader()
    writer.writerows(data)

    import requests, json

# 1. Fetch from API
data = requests.get('https://oim.108122.xyz/mass').json()

# 2. Save to file (no API call needed next time!)
with open('mass.json', 'w') as f:
    json.dump(data, f, indent=2)

# 3. Load from file
with open('mass.json') as f:
    loaded = json.load(f)
print(loaded['governor'])  # 'Maura Healey'

import sqlite3

conn = sqlite3.connect('towns.db')
conn.execute('''CREATE TABLE IF NOT EXISTS towns
                (name TEXT, county TEXT, pop INTEGER)''')
conn.execute('INSERT INTO towns VALUES (?, ?, ?)',
             ('Boston', 'Suffolk', 675647))
conn.commit()

for row in conn.execute('SELECT * FROM towns'):
    print(row)  # ('Boston', 'Suffolk', 675647)