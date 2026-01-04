Habit Tracker — CLI Productivity Tool

A lightweight Python command-line application to track daily habits, monitor streaks, and export progress data.

Tech Stack: Python · JSON · Pytest

🔹 Key Features

Create, edit, and delete habits

Mark habits as completed per day

Automatic calculation of current and longest streaks

Persistent storage using JSON (habits.json)

Export habit data to JSON or CSV

Unit testing of core logic using Pytest

🔹 Tech Stack
Layer	Technology
Application	Python 3
Storage	JSON
Testing	Pytest
🔹 Project Structure
habit-tracker/
├── project.py
├── test_project.py
├── habits.json
└── README.md

🔹 Setup & Run
git clone https://github.com/DeepikaReddy0607/habit-tracker.git
cd habit-tracker
python project.py


To run tests:

pytest test_project.py

🔹 Highlights

Designed modular functions for habit management and streak calculation

Implemented persistent data handling without external databases

Ensured correctness with automated unit tests

Focused on simplicity and reliability for daily CLI usage

🔹 Future Enhancements

Add date-range analytics and visual summaries

Support cloud backup or sync

Build a GUI or web interface

Add reminder notifications

🔹 Author

Rudru Deepika Reddy
B.Tech CSE Student
GitHub: https://github.com/DeepikaReddy0607