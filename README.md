# DART Commute Analysis

## Project Description

This project records and analyses my personal DART commute data.

The dataset is collected manually during my journeys. Each row represents one commute and records information such as the scheduled departure time, actual departure time, delay, weather, seat availability, total travel time and arrival time.

The aim of the project is to investigate patterns in my DART journeys and find out which factors may be related to delays and travel time.

---

## Research Questions

The project will investigate the following questions:

1. Is the DART usually more delayed during rainy weather?
2. How does the departure delay affect my total travel time?
3. Are there patterns in journey time and seat availability across different journeys?

---

## Data Dictionary

| Column | Type | Unit / Values | Description |
|---|---|---|---|
| date | Date | YYYY-MM-DD | Date of the journey |
| scheduled_time | Time | HH:MM | Scheduled DART departure time |
| actual_time | Time | HH:MM | Actual DART departure time |
| delay_minutes | Integer | minutes | Difference between scheduled and actual departure time |
| weather | Categorical | rain / cloudy / sunny / etc. | Weather observed during the journey |
| got_seat | Categorical | yes / no | Whether I was able to get a seat |
| travel_time | Integer | minutes | Total journey time |
| arrival_time | Time | HH:MM | Actual arrival time |

---

## Data Collection Method

The data is collected manually during my DART journeys.

For each journey I record the information on the same day rather than estimating it later.

The scheduled departure time is taken from the DART timetable information available at the time of travel.

The actual departure time and arrival time are recorded during the journey.

The delay in minutes is calculated as the difference between the scheduled departure time and the actual departure time.

Weather is recorded based on the conditions I observe during the journey.

Seat availability is recorded as either `yes` or `no`.

The dataset is stored in:

`data/commute.csv`

The CSV file will be updated regularly as new journeys are recorded.

---

## Project Structure

```text
dart_commute_analysis/
│
├── README.md
├── main.py
│
└── data/
    └── commute.csv
