import csv

DATA_FILE = "data/students.csv"

def add_student():
    roll_no = input("Enter roll number: ").strip()
    name = input("Enter student name: ").strip()

    if not roll_no or not name:
        print("Invalid input")
        return

    with open(DATA_FILE, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["roll_no"] == roll_no:
                print("Roll number already exists")
                return

    with open(DATA_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([roll_no, name])

    print("Student added successfully")

from datetime import date

ATTENDANCE_FILE = "data/attendance.csv"

def mark_attendance():
    roll_no = input("Enter roll number: ").strip()
    status = input("Enter status (P/A):").strip().upper()
    
    if status not in ("P","A"):
        print("Invalid status.Use P or A.")
        return
    with open(DATA_FILE, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["roll_no"] == roll_no:
                today = date.today().isoformat()

                with open(ATTENDANCE_FILE, "a", newline="") as afile:
                    writer = csv.writer(afile)
                    writer.writerow([roll_no, today, status])

                print("Attendance marked.")
                return

    print("Roll number not found.")   
def view_attendance():
    roll_no = input("Enter roll number: ").strip()
    total_days = 0
    present_days =0
   
    with open(ATTENDANCE_FILE, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["roll_no"] == roll_no:
                total_days +=1
                if row["status"] == "P":
                   present_days +=1
    if total_days == 0:
        print("No attendance records found")
        return

    percentage = (present_days/total_days) * 100
    print(f"Total days : {total_days}")
    print(f"Present days : {present_days}")
    print(f"Attendance %: {percentage:.2f}")


def main():
    while True:
        print("\n1. Add Student")
        print("2. Mark Attendance.")
        print("3. View Attendance")
        print("4. Exit")
        choice = input("Choose option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            mark_attendance()
        elif choice == "3":
            view_attendance()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()


