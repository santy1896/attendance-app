import datetime

# Create an empty dictionary to store attendance records
attendance = {}

# Function to record attendance
def record_attendance():
    name = input("Enter name: ")
    time_in = datetime.datetime.now()
    time_out = ""
    if name in attendance:
        print("Attendance already recorded for today!")
    else:
        attendance[name] = {"Time in": time_in, "Time out": time_out}
        print("Attendance recorded successfully!")

# Function to mark time out
def mark_time_out():
    name = input("Enter name: ")
    if name not in attendance:
        print("Attendance not recorded for today!")
    else:
        attendance[name]["Time out"] = datetime.datetime.now()
        print("Time out marked successfully!")

# Function to display attendance records
def display_attendance():
    print("Attendance Records:")
    print("{:<15} {:<25} {:<25}".format("Name", "Time in", "Time out"))
    for name, times in attendance.items():
        time_in = times["Time in"].strftime("%Y-%m-%d %H:%M:%S")
        time_out = times["Time out"].strftime("%Y-%m-%d %H:%M:%S") if times["Time out"] else ""
        print("{:<15} {:<25} {:<25}".format(name, time_in, time_out))

# Main loop
while True:
    print("Menu:")
    print("1. Record attendance")
    print("2. Mark time out")
    print("3. Display attendance")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        record_attendance()
    elif choice == "2":
        mark_time_out()
    elif choice == "3":
        display_attendance()
    elif choice == "4":
        break
    else:
        print("Invalid choice!")

