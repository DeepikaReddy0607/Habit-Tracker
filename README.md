# Habit Tracker
#### Video Demo: https://youtu.be/your_video_link_here
#### Description:

The **Habit Tracker** is a Python-based command-line application designed to help users build and maintain positive habits through daily tracking and progress monitoring.

This project allows users to:
- **Add new habits** they want to track (e.g., Exercise, Reading, Meditation).
- **Mark habits as completed** for the current day.
- **View progress**, including current and longest streaks for each habit.
- **Edit or delete existing habits.**
- **Export data** to a JSON or CSV file for external viewing or backup.

The app stores all data persistently in a JSON file (`habits.json`), ensuring users never lose their progress between sessions.  

It also includes a test file (`test_project.py`) that uses Python’s `assert` statements to validate the correctness of core functions such as:
- Adding habits  
- Recording completions  
- Computing streaks  

#### Files in the project:
- `project.py` — Main program file containing all functionality.
- `test_project.py` — Contains test cases for validation.
- `habits.json` — Stores habit and completion data (auto-generated).
- `README.md` — Description file (this one).

#### Technologies Used:
- Python 3
- JSON for data storage
- Pytest for testing

#### How to Run:
1. Open a terminal in the project folder.
2. Run the program with:
   ```bash
   python project.py
