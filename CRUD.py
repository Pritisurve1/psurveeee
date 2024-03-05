def create_record(records):
    name = input("Enter student name: ")
    age = int(input("Enter student age: "))
    grade = input("Enter student grade: ")
    record = {'name': name, 'age': age, 'grade': grade}
    records.append(record)
    print("Record created successfully!")

# Function to read all records
def read_records(records):
    if not records:
        print("No records found!")
    else:
        print("Student Records:")
        for index, record in enumerate(records, start=1):
            print(f"{index}. Name: {record['name']}, Age: {record['age']}, Grade: {record['grade']}")

# Function to update a record
def update_record(records):
    if not records:
        print("No records found!")
        return

    index = int(input("Enter index of record to update: ")) - 1
    if 0 <= index < len(records):
        name = input("Enter new name: ")
        age = int(input("Enter new age: "))
        grade = input("Enter new grade: ")
        records[index] = {'name': name, 'age': age, 'grade': grade}
        print("Record updated successfully!")
    else:
        print("Invalid index!")

# Function to delete a record
def delete_record(records):
    if not records:
        print("No records found!")
        return

    index = int(input("Enter index of record to delete: ")) - 1
    if 0 <= index < len(records):
        del records[index]
        print("Record deleted successfully!")
    else:
        print("Invalid index!")

# Main function
def main():
    student_records = []
    while True:
        print("\n1. Create Record")
        print("2. Read Records")
        print("3. Update Record")
        print("4. Delete Record")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            create_record(student_records)
        elif choice == '2':
            read_records(student_records)
        elif choice == '3':
            update_record(student_records)
        elif choice == '4':
            delete_record(student_records)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
