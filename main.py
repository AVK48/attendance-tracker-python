print("RUNNING FILE:", __file__)

import csv
from datetime import datetime, date


STUDENTS_FILE = "data/students.csv"
ATTENDANCE_FILE = "data/attendance.csv"


def filter_records_by_date(records, start, end):
    filtered = []
    for row in records:
        record_date = datetime.strptime(row["date"], "%Y-%m-%d").date()
        if start <= record_date <= end:
            filtered.append(row)
    return filtered


def sort_records_date(records):
    return sorted(records, key = lambda row: row["date"])




def student_exists(roll_no):
    with open(STUDENTS_FILE, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["roll_no"] == roll_no:
                return True
    return False

def read_records():
    with open(ATTENDANCE_FILE, "r", newline="") as file:
        return list(csv.DictReader(file))

def get_records(records, roll_no):
    return [row for row in records if row["roll_no"]== roll_no]
    
    
def present_streak(records):
    current = 0
    maximum = 0

    for row in records:
        if row["status"] == "P":
            current += 1
            maximum = max(maximum, current)
        else:
            current = 0

    return maximum




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
    records = read_records()
    student_records = get_records(records, roll_no)
    ordered_records = sort_records_date(student_records)

    streak = present_streak(ordered_records)


    percentage = (present_days/total_days) * 100
    consistency_score = streak/total_days
    print(f"Total days : {total_days}")
    print(f"Present days : {present_days}")
    print(f"Attendance %: {percentage:.2f}")
    print(f"Consistency score: {consistency_score:.2f}")



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

def validate_dataset(row):
    if row["total_days"] <= 0:
        return False
    if row["present_days"] > row["total_days"]:
        return False
    if not (0 <= row["percentage"] <= 100):
        return False
    if not (0 <= row["consistency_score"] <= 1):
        return False
    if row["longest_streak"] > row["total_days"]:
        return False
    return True

    


def generate_dataset():
    from_date = input("From date (YYYY-MM-DD): ").strip()
    to_date = input("To date (YYYY-MM-DD): ").strip()

    try:
        start = datetime.strptime(from_date, "%Y-%m-%d").date()
        end = datetime.strptime(to_date, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date format.")
        return

    all_records = read_records()
    date_filtered_records = filter_records_by_date(all_records, start, end)

    with open("data/student_features.csv", "w", newline="") as file:
        writer = csv.writer(file)


        # header
        writer.writerow([
            "roll_no",
            "from_date",
            "to_date",
            "total_days",
            "present_days",
            "attendance_pct",
            "longest_streak",
            "consistency"
        ])

        # loop over students
        with open(STUDENTS_FILE, "r", newline="") as sfile:
            reader = csv.DictReader(sfile)

            for student in reader:
                roll_no = student["roll_no"]

                student_records = get_records(date_filtered_records, roll_no)
                if not student_records:
                    continue

                ordered_records = sort_records_date(student_records)

                total_days = len(ordered_records)
                present_days = sum(1 for r in ordered_records if r["status"] == "P")

                attendance_pct = (present_days / total_days) * 100
                longest_streak = present_streak(ordered_records)
                consistency = longest_streak / total_days
                
                
                row = {
                "total_days": total_days,
                "present_days": present_days,
                "attendance_pct": attendance_pct,
                "longest_streak": longest_streak,
                "consistency": consistency
                }

                if not validate_dataset(row):
                   continue


                writer.writerow([
                    roll_no,
                    from_date,
                    to_date,
                    total_days,
                    present_days,
                    round(attendance_pct, 2),
                    longest_streak,
                    round(consistency, 2)
                ])

    print("Student feature dataset generated successfully.")


def main():
    while True:
        print("\n1. Add Student")
        print("2. Mark Attendance.")
        print("3. View Attendance")
        print("4. View Attendance (Data Range)")
        print("5.Generate the Dataset")
        print("6. Exit")
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
            generate_dataset()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice")



if __name__ == "__main__":
    main()


