def main():
    print("Attendance Tracker - Version 1")

if __name__ == "__main__":
    main()
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
    print("student added successfully")

def main():
    print("Attendance Tracker - Version 1")
    while True:
        print("\n1.Add student")
        print(2.Exit")
        choice = input("choose option:")

        if choice == "1":
            add_student()
        elif choice == "2":
            print("Exiting..")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
            

   

  
