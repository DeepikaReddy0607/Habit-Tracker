import os
import datetime
import project  

DB_FILE = "habits.json"

def reset_db():
    if os.path.exists(DB_FILE):
        os.remove(DB_FILE)

def test_add_habit():
    reset_db()
    hid1 = project.add_habit("Exercise")
    hid2 = project.add_habit("Reading")
    assert hid1 == 1, "First habit ID should be 1"
    assert hid2 == 2, "Second habit ID should be 2"
    data = project.load_data()
    assert len(data["habits"]) == 2, "There should be 2 habits in DB"
    assert data["habits"][0]["name"] == "Exercise"
    assert data["habits"][1]["name"] == "Reading"

def test_record_completion_and_streak():
    reset_db()
    hid = project.add_habit("Meditation")
    today = str(datetime.date.today())
    project.record_completion(hid)
    streak, longest = project.compute_streak(hid)
    assert streak == 1, "Streak should be 1 after first completion"
    assert longest == 1, "Longest streak should be 1 after first completion"
    data = project.load_data()
    assert today in data["completions"][str(hid)], "Today's completion should be recorded"

def test_edit_and_delete_habit():
    reset_db()
    hid = project.add_habit("Sleep Early")
    project.edit_habit_name(hid, "Sleep Well")
    data = project.load_data()
    assert data["habits"][0]["name"] == "Sleep Well", "Habit name should be updated"
    
    project.delete_habit(hid)
    data = project.load_data()
    assert len(data["habits"]) == 0, "Habit should be deleted"
    assert str(hid) not in data["completions"], "Completions should be deleted too"

def test_success_rate_and_weekly_summary():
    reset_db()
    hid = project.add_habit("Walk")
    project.record_completion(hid)

    rate = project.success_rate(hid)
    assert rate > 0, "Success rate should be greater than 0"
    
    done, total = project.weekly_summary(hid)
    assert done == 1, "Weekly summary done count should be 1"

def test_export_csv():
    reset_db()
    hid1 = project.add_habit("Yoga")
    hid2 = project.add_habit("Coding")
    project.record_completion(hid1)
    project.export_csv("test_habits.csv")
    assert os.path.exists("test_habits.csv"), "CSV file should exist after export"

if __name__ == "__main__":
    test_add_habit()
    test_record_completion_and_streak()
    test_edit_and_delete_habit()
    test_success_rate_and_weekly_summary()
    test_export_csv()
    print("All tests passed successfully!")
