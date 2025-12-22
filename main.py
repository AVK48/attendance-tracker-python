print("RUNNING FILE:", __file__)

import csv

STUDENTS_FILE = "data/students.csv"


def student_exists(roll_no):
    with open(STUDENTS_FILE, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["roll_no"] == roll_no:
                return True
    return False


def add_student():
    roll_no = input("Enter roll number: ").strip()
    name = input("Enter student name: ").strip()

    if not roll_no or not name:
        print("Invalid input")
        return

    with open(STUDENTS_FILE, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["roll_no"] == roll_no:
                print("Roll number already exists")
                return

    with open(STUDENTS_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([roll_no, name])

    print("Student added successfully")

from datetime import date

ATTENDANCE_FILE = "data/attendance.csv"



def mark_attendance():
    today = date.today().isoformat()
    roll_no = input("Enter roll number: ").strip()
    if not student_exists(roll_no):
       print("Roll number not found.")
       return
    status = input("Enter status (P/A):").strip().upper()

    
    
    if status not in ("P","A"):
        print("Invalid status.Use P or A.")
        return
    with open(STUDENTS_FILE, "r", newline="") as file:
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


def view_attendance_summary():
    roll_no = input("Enter roll number: ").strip()

    if not student_exists(roll_no):
        print("Roll number not found.")
        return
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

from datetime import datetime

def view_attendance_date_range():
    roll_no = input("Enter roll number: ").strip()
    if not student_exists(roll_no):
       print("Roll number not found.")
       return
    from_date = input("From date (YYYY-MM-DD): ").strip()
    to_date = input("To date (YYYY-MM-DD): ").strip()


    try:
        start = datetime.strptime(from_date, "%Y-%m-%d").date()
        end = datetime.strptime(to_date, "%Y-%m-%d").date()
    except ValueError as e:
        print("Invalid date format:", e)
        return

    if start > end:
        print("From date cannot be after To date.")
        return

    total_days = 0
    present_days = 0

    with open(ATTENDANCE_FILE, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["roll_no"] != roll_no:
                continue

            record_date = datetime.strptime(row["date"], "%Y-%m-%d").date()

            if start <= record_date <= end:
                total_days += 1
                if row["status"] == "P":
                    present_days += 1

    if total_days == 0:
        print("No attendance records in this range.")
        return

    percentage = (present_days / total_days) * 100

    print(f"From         : {from_date}")
    print(f"To           : {to_date}")
    print(f"Total Days   : {total_days}")
    print(f"Present Days : {present_days}")
    print(f"Attendance % : {percentage:.2f}")




def main():
    while True:
        print("\n1. Add Student")
        print("2. Mark Attendance.")
        print("3. View Attendance")
        print("4. View Attendance (Data Range)")
        print("5. Exit")
        choice = input("Choose option: ")

        if choice == "1":
            add_student()
        elif choice == "2":
            mark_attendance()
        elif choice == "3":
            view_attendance_summary()
        elif choice == "4":
            view_attendance_date_range()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()


