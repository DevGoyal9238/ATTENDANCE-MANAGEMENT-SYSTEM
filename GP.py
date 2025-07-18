import csv
from datetime import datetime

def mark_attendance(name):
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H:%M:%S")

    with open('attendance.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, date_str, time_str])
    print(f"[✓] Attendance marked for {name} at {time_str} on {date_str}")

def show_attendance():
    try:
        with open('attendance.csv', 'r') as file:
            reader = csv.reader(file)
            print("\n--- Attendance Records ---")
            for row in reader:
                print(f"Name: {row[0]}, Date: {row[1]}, Time: {row[2]}")
    except FileNotFoundError:
        print("No attendance records found yet.")

def main():
    while True:
        print("\n--- Attendance System ---")
        print("1. Mark Attendance")
        print("2. Show Attendance")
        print("3. Exit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            name = input("Enter your name: ").strip()
            if name:
                mark_attendance(name)
            else:
                print("Name cannot be empty!")
        elif choice == '2':
            show_attendance()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
