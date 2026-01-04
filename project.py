import json
import os
import datetime
import csv

DB_FILE = "habits.json"

def load_data():
    if not os.path.exists(DB_FILE):
        return {"habits": [], "completions": {}}
    with open(DB_FILE, "r") as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            data = {"habits": [], "completions": {}}
    if "habits" not in data:
        data["habits"] = []
    if "completions" not in data:
        data["completions"] = {}
    return data

def save_data(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)

def add_habit(name):
    data = load_data()
    if data["habits"]:
        new_id = max(h["id"] for h in data["habits"]) + 1
    else:
        new_id = 1
    data["habits"].append({
        "id": new_id,
        "name": name,
        "created": str(datetime.date.today())
    })
    data["completions"][str(new_id)] = []
    save_data(data)
    return new_id

def list_habits():
    data = load_data()
    return data["habits"]

def record_completion(habit_id):
    data = load_data()
    if str(habit_id) not in data["completions"]:
        print("Habit ID not found.")
        return
    today = str(datetime.date.today())
    if today not in data["completions"].get(str(habit_id), []):
        data["completions"][str(habit_id)].append(today)
    save_data(data)

def delete_habit(habit_id):
    data = load_data()
    data["habits"] = [h for h in data["habits"] if h["id"] != habit_id]
    if str(habit_id) in data["completions"]:
        del data["completions"][str(habit_id)]
    save_data(data)

def edit_habit_name(habit_id, new_name):
    data = load_data()
    for h in data["habits"]:
        if h["id"] == habit_id:
            h["name"] = new_name
            break
    save_data(data)

def compute_streak(habit_id):
    data = load_data()
    dates = sorted(data["completions"].get(str(habit_id), []))
    if not dates:
        return 0, 0
    dates = [datetime.date.fromisoformat(d) for d in dates]

    longest, current = 0, 1
    for i in range(1, len(dates)):
        if (dates[i] - dates[i - 1]).days == 1:
            current += 1
        else:
            longest = max(longest, current)
            current = 1
    longest = max(longest, current)

    today = datetime.date.today()
    streak = 0
    day = today
    while day in dates:
        streak += 1
        day -= datetime.timedelta(days=1)
    return streak, longest

def success_rate(habit_id):
    data = load_data()
    habit = next((h for h in data["habits"] if h["id"] == habit_id), None)
    if not habit:
        return 0
    created_date = datetime.date.fromisoformat(habit["created"])
    days = (datetime.date.today() - created_date).days + 1
    if days <= 0:
        return 0
    completions = len(data["completions"].get(str(habit_id), []))
    return round((completions / days) * 100, 2)

def weekly_summary(habit_id):
    data = load_data()
    completions = [datetime.date.fromisoformat(d)
                   for d in data["completions"].get(str(habit_id), [])]
    today = datetime.date.today()
    last_week = [today - datetime.timedelta(days=i) for i in range(7)]
    count = sum(1 for d in completions if d in last_week)
    return count, 7

def export_csv(filename="habits_export.csv"):
    data = load_data()
    with open(filename, "w", newline="", encoding = "utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Habit ID", "Habit Name", "Completion Dates"])
        for h in data["habits"]:
            hid = str(h["id"])
            dates = ", ".join(data["completions"].get(hid, []))
            writer.writerow([h["id"], h["name"], dates])

def main():
    while True:
        print("\nHabit Tracker")
        print("1. Add habit")
        print("2. List habits")
        print("3. Mark habit done")
        print("4. Show streak")
        print("5. Delete habit")
        print("6. Edit habit name")
        print("7. Show success rate")
        print("8. Weekly summary")
        print("9. Export CSV")
        print("10. Exit")

        choice = input("Choose: ")
        if choice == "1":
            name = input("Habit name: ")
            hid = add_habit(name)
            print(f"Habit added with id {hid}")
        elif choice == "2":
            habits = list_habits()
            if not habits:
                print("No habits yet.")
            for h in habits:
                print(f'{h["id"]}: {h["name"]} (created {h["created"]})')
        elif choice == "3":
            hid = int(input("Habit id: "))
            record_completion(hid)
            print("Marked done for today!")
        elif choice == "4":
            hid = int(input("Habit id: "))
            streak, longest = compute_streak(hid)
            print(f"Current streak: {streak} days, Longest streak: {longest} days")
        elif choice == "5":
            hid = int(input("Habit id to delete: "))
            delete_habit(hid)
            print("Habit deleted.")
        elif choice == "6":
            hid = int(input("Habit id: "))
            new_name = input("New name: ")
            edit_habit_name(hid, new_name)
            print("Habit name updated.")
        elif choice == "7":
            hid = int(input("Habit id: "))
            rate = success_rate(hid)
            print(f"Success rate: {rate}%")
        elif choice == "8":
            hid = int(input("Habit id: "))
            done, total = weekly_summary(hid)
            print(f"Weekly summary: {done}/{total} days completed")
        elif choice == "9":
            export_csv()
            print("Exported habits to habits_export.csv")
        elif choice == "10":
            print("Exiting...")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
