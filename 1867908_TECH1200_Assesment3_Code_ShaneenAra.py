#Name: Shaneen Ara
#ID: 1867908
#Purpose: Creating Employee Management System

import csv
import os
import random



class Employee:


    def __init__(shaneen, id, name, age, loc, department, position, salary, joining_date):
        #Public
        shaneen.id = id
        shaneen.loc = loc
        shaneen.department = department
        shaneen.joining_date = joining_date

        #Private using __
        shaneen.__name = name
        shaneen.__age = age
        shaneen.__position = position
        shaneen.__salary = salary

    def get_name(shaneen):
        return shaneen.__name

    def get_age(shaneen):
        return shaneen.__age

    def get_position(shaneen):
        return shaneen.__position

    def get_salary(shaneen):
        return shaneen.__salary


    def set_name(shaneen, new_name):
        if new_name.replace(" ", "").isalpha(): #using isalpha() checking if input is any number or not
            shaneen.__name = new_name
        else:
            print("Invalid name! Name must only contain letters.")

    def set_age(shaneen, new_age):
        def set_age(shaneen, new_age):
            try:
                new_age = int(new_age)  # Converting to integer
                if new_age <= 0:  # Rejecting 0 and negative numbers\

                    print("Age must be greater than 0.")
                    return
                shaneen.__age = new_age  # Saving valid age
            except:
                print("Age must be a valid number.")

    def set_position(shaneen, new_position):
        valid_positions = ["Analyst", "Assistant", "Consultant", "Developer", "Executive", "Manager"]
        if new_position in valid_positions:
            shaneen.__position = new_position
        else:
            print("Invalid position! Please choose from the list.")

    def set_salary(shaneen, new_salary):
        try:
            new_salary = float(new_salary)
            if new_salary >= 0:
                shaneen.__salary = new_salary
            else:
                print("Salary cannot be negative.")
        except:
            print("Invalid salary! Please enter a number.")


    def sha_get_details(shaneen):
        # here, returning private and public data together
        return [shaneen.id, shaneen.__name, shaneen.__age, shaneen.loc,
                shaneen.department, shaneen.__position, shaneen.__salary, shaneen.joining_date]


    @staticmethod
    def sha_generate_id(existing_ids):
        # I am using random module so that it can create random ID that does not already exist
        while True:
            emp_id = str(random.randint(100, 9999))
            if emp_id not in existing_ids:
                return emp_id
f = "Current_Employee.csv"



def sha_read_employees():
    employees = []

    if os.path.exists(f):#here its checking if the employee file is already there or not

        with open(f, "r") as file: #the file has been open in the read mode
            # Reading all lines from the file
            lines = file.readlines()
            #as the first row is header avoiding that one
            for line in lines[1:]:
                row = line.strip().split(",")  #every line is being seperated by comma

                # As other cells are empty in dataset, Skipping the incomplete or empty lines
                if len(row) < 8:
                    continue

                employees.append(row)
    return employees


def sha_write_employees(employees, append=False):


    try:
        # Decide how to open the file
        if append:   #adds new employees

            mode = "a"   # add new data to the end

        else:  #overwrites entire file

            mode = "w"   # create new file or overwrite old data

        with open(f, mode) as file:
            # Writing header only if overwriting
            #not for appending
            if not append:
                file.write("Employee_ID,Employee_Name,Age,Location,Department,Position,Salary,Joining_Date\n")

            # Write each employee record as a comma-separated line
            for emp in employees:
                line = ",".join(map(str, emp))
                file.write(line + "\n")

        

    except PermissionError:
        print("Please close the CSV file — it may be open in Excel.")
    except Exception as e:
        print("Error while saving:", e)



def sha_add_employee():
    employees = sha_read_employees()
    try:
        # Using the static method from Employee class fr creating id
        existing_ids = []
        for emp in employees:
            #adding id to another list
            existing_ids.append(emp[0])#taking the first value in each record (emp[0])

        emp_id = Employee.sha_generate_id(existing_ids)
        print("Assigned Employee ID:", emp_id)


        name = input("Enter Employee Name[(No Number, No Space)]: ").strip()
        if name == "":
            print("Oops!!INVALID NAME! Name cannot be blank.")
            return
        try:
            float(name)
            print("Oops!!INVALID NAME!Name cannot be a number.")
            return
        except:
            pass

        age = input("ENTER AGE: ").strip()
        try:
            int(age)
        except:
            print("AGE MUST BE A NUMBER!")
            return

        loc = input("Enter Location[Australia, Brazil, Canada, France, Germany, India, Japan, Mexico, UK, USA]: ").strip()
        dept = input("Enter Department[Engineering, Finance, HR, Marketing, Sales, Support]: ").strip()
        pos = input("Enter Position[Analyst, Assistant, Consultant, Developer, Executive, Manager]: ").strip()

        salary = input("ENTER SALARY: ").strip()
        date = input("ENTER JOINING DATE: ").strip()
        print("Please don't make any typo otherwise it will be saved in the dataset.")
        print("If you make any typo in the position or department you can use Update Employee Details. Thank you." )

        # Creating new Employee object
        new_emp = Employee(emp_id, name, age, loc, dept, pos, salary, date)

        # Using setters for private fields to validate
        new_emp.set_name(name)
        new_emp.set_age(age)
        new_emp.set_position(pos)
        new_emp.set_salary(salary)


        for emp in employees:#Using this loop tp chk each employee details of the datset

            if emp[1].lower() == name.lower():#checking if input value is in the list or not
                print("Employee with same name already exists!")#if matched any item
                return

        # new employee's data in a list format, so preparing for that
        new_record = [new_emp.sha_get_details()]

        # at the end, it will save  the new employee to the CSV file by adding (appending) it
        sha_write_employees(new_record, append=True)

        print("EMPLOYEE INFORMATION HAS BEEN SAVED SUCCESSFULLY!")


    except Exception as e:
        print("SOMETHING WRONG:", e)

def sha_view_employees():
    try:
        employees = sha_read_employees()
        if len(employees) == 0:
            print("No employees found.")
            return

        print("\n__________ALL EMPLOYEES_________")
        for emp in employees:

            if len(emp) < 8:  # Here Skipping incomplete rows safely
                continue

            try:
                print("ID:", emp[0], "[] Name:", emp[1], "[] Age:", emp[2], "[] Location:", emp[3], "[] Department:", emp[4],
                      "[] Position:", emp[5], "[] Salary:", emp[6],   "[] Joining Date:", emp[7])
            except IndexError:
                # if one row's data is empty it will give index error msg to the user
                print("Incomplete record found and skipped.")

    except FileNotFoundError:
        print("FILE NOT FOUND!!! Please make sure the employee file exists.")
    except Exception as e:
        print("SOMETHING WENT WRONG WHILE VIEWING DATA:", e)



def sha_update_employee():
    employees = sha_read_employees()
    emp_id = input("PLEASE ENTER EMPLOYEE ID TO UPDATE: ").strip()
    found = False

    for emp in employees:
        if emp[0] == emp_id:
            found = True
            print("WHICH ONE YOU WANT TO UPDATE!?")
            print("1. Name  2. Age  3. Location  4. Department  5. Position  6. Salary  7. Joining Date")
            choice = input("ENTER NUMBER: ")

            if choice=="1":
                emp[1]= input("Enter new Name: ")

            elif choice=="2":
                emp[2] = input("Enter new Age: ")

            elif choice=="3":
                emp[3] =input("Enter new Location: ")
            elif choice=="4":

                emp[4]=input("Enter new Department: ")

            elif choice=="5":
                emp[5] = input("Enter new Position: ")

            elif choice=="6":
                emp[6] = input("Enter new Salary: ")

            elif choice =="7":
                emp[7] = input("Enter new Joining Date: ")
            else:
                print("Invalid choice.")
                return

            sha_write_employees(employees)
            print("EMPLOYEE INFORMATION HAS BEEN SAVED !")
            break

    if not found:
        print("UNFORTUNATELY EMPLOYEE NOT FOUND!")


def sha_delete_employee():
    employees = sha_read_employees()
    emp_id = input("KINDLY ENTER EMPLOYEE ID TO DELETE: ").strip()

    # Here i am creating an empty list to store remaining employees
    new_employees = []
    # I am using a flag so that it can check if the employee was found and deleted
    deleted = False


    for emp in employees:
        # If the employee ID matches the one we want to delete
        if emp[0] == emp_id:
            deleted = True
            continue
        # else, just keeping the record in the new list
        new_employees.append(emp)

    # If a matching record was found and deleted
    if deleted:

        # Writing the updated list
        sha_write_employees(new_employees)
        print("EMPLOYEE RECORD HAS BEEN DELETED SUCCESSFULLY!")
    else:
        # If no record is FOUND
        print("Employee not found.")




def sha_search_employee_by_id():
    employees=sha_read_employees()
    emp_id=input("Enter employee ID to search: ").strip()
    found=False


    for emp in employees:
        if emp[0] == emp_id:#if given input from the user matches with existing detail
            print("ID:", emp[0], "[] Name:", emp[1], "[] Age:", emp[2],  "[] Location:", emp[3], "[] Department:", emp[4],
                  "[] Position:", emp[5], "[] Salary:", emp[6],"[] Joining Date:", emp[7])
            found = True

    if not found: #otherwise
        print("No employee found with that ID.")



def sha_sort_employees():
    employees = sha_read_employees()  # first read employee data
    if len(employees) == 0:
        print("No records to sort.")
        return

    print("Sort by:")
    print("1. Salary")
    print("2. Position")
    choice = input("ENTER YOUR CHOICE BETWEEN 1 AND 2: ")

    print("Sort order:")
    print("1. Ascending")
    print("2. Descending")
    order = input("ENTER YOUR CHOICE BETWEEN 1 AND 2: ")

    # WHEN the user enters "2", sorting will be in descending order
    reverse_order = True if order == "2" else False

    # helper functions for sorting
    def get_salary(emp):
        try:
            return float(emp[6])
        except:
            return 0.0

    def get_position(emp):
        return emp[5].lower()

    # sorting logic
    if choice == "1":
        employees.sort(key=get_salary, reverse=reverse_order)
    elif choice == "2":
        employees.sort(key=get_position, reverse=reverse_order)
    else:
        print("Invalid choice.")
        return

    print("\n--- Sorted Employees ---")
    for emp in employees:
        print(emp[0], "|", emp[1], "|", emp[5], "|", emp[6])


# creating 4 default employees and save them
def initialize_default_employees():
    # If the file already exists, delete it to start fresh
    if os.path.exists(f):
        os.remove(f)


    # Create 4 default employees using the constructor
    emp1 = Employee("101", "Hasan", 28, "Japan", "Sales", "Manager", 85000, "10/07/2022")
    emp2 = Employee("102", "Rafi", 25, "India", "HR", "Executive", 72000, "15/09/2022")
    emp3 = Employee("103", "Rifat", 30, "USA", "Engineering", "Developer", 95000, "22/08/2022")
    emp4 = Employee("104", "Anisha", 27, "UK", "Marketing", "Analyst", 68000, "05/01/2024")

    # Converting all employee data into a list
    employees = [
        emp1.sha_get_details(),
        emp2.sha_get_details(),
        emp3.sha_get_details(),
        emp4.sha_get_details()
    ]

    # Writing new data into the file (creates file if it doesn't exist)
    sha_write_employees(employees)



def main():
    while True:
        print("\n---------EMPLOYEE MANAGEMENT SYSTEM---------")
        print("\n                                  ~Created by:Shaneen")
        print("[1] Add Employee")
        print("[2] View All Employees")
        print("[3] Update Employee Details")
        print("[4] Delete Employee")
        print("[5] Search Employee")
        print("[6] Sort Employees")
        print("[7] Exit")

        choice = input("ENTER YOUR CHOICE: ")

        if choice == "1":
            sha_add_employee()
        elif choice == "2":
            sha_view_employees()
        elif choice == "3":
            sha_update_employee()
        elif choice == "4":
            sha_delete_employee()
        elif choice == "5":
            sha_search_employee_by_id()
        elif choice == "6":
            sha_sort_employees()
        elif choice == "7":
            print("ALL GOOD! Have a great one! Thank you for using this program.")
            break
        else:
            print("Oops! INVALID CHOICE! KINDLY CHOOSE AN OPTION FROM 1 to 7.")


if __name__ == "__main__":
    initialize_default_employees()
    main()
