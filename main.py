# Import CSV module
import csv

file_name = "data/commute.csv"

# Create an empty list to store commute records
commutes = []

# Open and read the CSV file
with open(file_name, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)

    for row in reader:

        # Change numeric values from strings to integers

        row["delay_minutes"] = int(row["delay_minutes"])
        row["travel_time"] = int(row["travel_time"])

        commutes.append(row)

# for temporary debugging, print the commutes list to verify the data was read correctly        
# print(commutes)

# Import SQLite module
import sqlite3

# Create and connect to the SQLite database
conn = sqlite3.connect("data/commute.db")

# Create a cursor to execute SQL commands
cursor = conn.cursor()

# create the commutes table if not exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS commutes (

    date TEXT,
    scheduled_time TEXT,
    actual_time TEXT,
    delay_minutes INTEGER,
    weather TEXT,
    got_seat TEXT,
    travel_time INTEGER,
    arrival_time TEXT

)
""")

# clear posible old records in the commutes table before inserting csv data
cursor.execute("DELETE FROM commutes")

# Insert each commute record into database
for commute in commutes:
    cursor.execute("""
    INSERT INTO commutes (
        date,
        scheduled_time,
        actual_time,
        delay_minutes,
        weather,
        got_seat,
        travel_time,
        arrival_time
    )
    
    VALUES (?,?,?,?,?,?,?,?)
    """, (
        
        commute["date"],
        commute["scheduled_time"],
        commute["actual_time"],
        commute["delay_minutes"],
        commute["weather"],
        commute["got_seat"],
        commute["travel_time"],
        commute["arrival_time"]
    ))

conn.commit()

# Get records from commutes table
cursor.execute("SELECT * FROM commutes")

rows = cursor.fetchall()

# display to verify the records were inserted correctly from the CSV file
for row in rows:
    print(row)

#Calculate the average delay
cursor.execute("SELECT AVG(delay_minutes) FROM commutes")

average_delay = cursor.fetchone()

print("Average delay time:" , average_delay[0])


# Calculate the average delay for each weather condition
cursor.execute("""
SELECT weather, AVG(delay_minutes) AS average_delay
FROM commutes
GROUP BY weather
""")

weather_results = cursor.fetchall()

for row in weather_results:
    print(row)

# Import Pandas module
import pandas as pd

df = pd.read_sql("SELECT * FROM commutes", conn)

print(df)

# Calculate the average delay minutes using pandas
print(df["delay_minutes"].mean())

# Calculate the average delay for each weather condition using pandas
print(df.groupby("weather")["delay_minutes"].mean())
# the frist 2 calculation is for check if the pandas gets same results as SQL

# Find the maximun delay minutes
print("Maximum delay:", df["delay_minutes"].max())

#Find the longest travelling time 
print("Longest travel time is:" , df["travel_time"].max())

# Find the shortest travel time
print("Shortest travel time:", df["travel_time"].min())

# Count journeys with and without a seat
print(df["got_seat"].value_counts())

# Close the database connection
conn.close()


# Import matplotlib module
import matplotlib.pyplot as plt


# Test code for the charts
# The final versions are used in the functions below.
#----------------------------------------------------

# # create line chart to show dart delay by date
# plt.plot(df["date"] , df["delay_minutes"],marker="o")

# # Add labels and title
# plt.xlabel("Date")
# plt.ylabel("Delay (minutes)")
# plt.title("DART Delay by Date")

# # Rotate
# plt.xticks(rotation=45)

# # Automatic layout and formatting
# plt.tight_layout()
# plt.show()


# # Calculate average delay for each weather condition 
# # connected to df.groupby("weather")["delay_minutes"].mean() at line 122
# weather_avg = df.groupby("weather")["delay_minutes"].mean()

# # Create a bar chart
# weather_avg.plot(kind="bar")

# plt.xlabel("Weather")
# plt.ylabel("Average delay (minutes)")
# plt.title("Average DART Delay by Weather")

# plt.tight_layout()
# plt.show()


# # Create a scatter plot toshow the relationship between delay and travel time
# plt.scatter(df["delay_minutes"], df["travel_time"])

# plt.xlabel("Delay (minutes)")
# plt.ylabel("Travel time (minutes)")
# plt.title("Delay vs Travel Time")

# plt.tight_layout()
# plt.show()

#----------------------------------------------------

# Function to show delay by date
def show_delay_chart():

    plt.plot(df["date"], df["delay_minutes"], marker="o")

    plt.xlabel("Date")
    plt.ylabel("Delay (minutes)")
    plt.title("DART Delay by Date")

    plt.xticks(rotation=45)
    plt.tight_layout()

    plt.show()


# Function to show average delay by weather
def show_weather_chart():

    weather_avg = df.groupby("weather")["delay_minutes"].mean()

    weather_avg.plot(kind="bar")

    plt.xlabel("Weather")
    plt.ylabel("Average delay (minutes)")
    plt.title("Average DART Delay by Weather")

    plt.tight_layout()

    plt.show()


# Function to show the relationship between delay and travel time
def show_scatter_chart():

    plt.scatter(df["delay_minutes"], df["travel_time"])

    plt.xlabel("Delay (minutes)")
    plt.ylabel("Travel time (minutes)")
    plt.title("Delay vs Travel Time")

    plt.tight_layout()

    plt.show()

# Main Menu
while True:

    print()
    print(" Dart Commute Analysis ")
    print("1. Show delay by date")
    print("2. Show average delay by weather")
    print("3. Show delay vs travel time")
    print("4. Quit")

    choice = input("Enter your choice: ")

    if choice == "1":
        show_delay_chart()

    elif choice == "2":
        show_weather_chart()

    elif choice == "3":
        show_scatter_chart()

    elif choice == "4":
        print("Program closed.")
        break

    else:
        print("Invalid choice. Please try again.")