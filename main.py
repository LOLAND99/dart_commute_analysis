# Python to read CSV

import csv

file_name = "data/commute.csv"

commutes = []

with open(file_name, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for row in reader:

        row["delay_minutes"] = int(row["delay_minutes"])
        row["travel_time"] = int(row["travel_time"])

        commutes.append(row)
        
print(commutes)

# Python executes SQL using sqlite3

import sqlite3

conn = sqlite3.connect("data/commute.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS commutes (

    date TEXT,
    scheduled_time TEXT,
    actual_time TEXT,
    delay_minutes INTEGER,
    weather TEXT,
    got_set TEXT,
    travel_time INTEGER,
    arrival_time TEXT

)
""")

for commute in commutes:
    cursor.execute("""
    INSERT INTO commutes (
        date,
        scheduled_time,
        actual_time,
        delay_minutes,
        weather,
        got_set,
        travel_time,
        arrival_time
    )
    
    VALUES (?,?,?,?,?,?,?,?,?)
    """, (
        
        commute["date"],
        commute["scheduled_time"],
        commute["actual_time"],
        commute["delay_minutes"],
        commute["weather"],
        commute["got_set"],
        commute["travel_time"],
        commute["arrival_time"]
    ))

conn.commit()
