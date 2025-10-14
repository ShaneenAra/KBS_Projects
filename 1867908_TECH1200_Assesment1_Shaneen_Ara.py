
#creating 1 empty list
student_list = []

while True: #until exit
    #for displaying menu, i am using just print
    print("\n=============== Student-Management-System ===============")
    print("1. Add Student")
    print("2. View Students Record")
    print("3. Edit Students Record")
    print("4. Delete Students")
    print("5. Exit")
    print("\n=========================================================")

    #choice will take user input
    choice = input("Enter your choice: ")

    #for going through each condition, using nested loop
    if choice == "1": #for adding student info
        while True:
            student_name = input("Enter Student Name:(or press 0 to stop): ")
            if student_name == "0":
                print("Successfully added student.")
                break
            grade = int(input("Enter GRADE: "))

            #using dictionary-->student = {"name": student_name, "grade": grade}
            student = (student_name, grade)
            student_list.append(student)

            print(f"Congratulations! You have successfully entered"  + " " + student_name + " " +  "grade")

    elif choice == "2":#for viewing the info from choice 1
        if not student_list:
            print("NO STUDENT FOUND!!\n") #if no info is found
        else:
            print("\n--- Student Records ---")
            for s in student_list:
                #print("Name:", s["name"], "Mark:", s["grade"])
                print("Name:", s[0], "Mark:", s[1]) #using tuple instead
                if s[1]  >= 85:
                    print("Grade: HD")
                elif s[1] >= 75:
                    print("Grade: D")
                elif s[1] >= 65:
                    print("Grade: C")
                elif s[1] >= 50:
                    print("Grade: P")
                else:
                    print("Grade: F")

    elif choice == "3": #for updating any previous info
        update_name = input("Enter the name of the student you want to update: ")
        found = False
        for student in student_list:#search for the name in each elemnt of the list
            if student[0] == update_name:
                updated_grade =int(input("Enter new grade: "))#take new grade from user
                student_list.remove(student)#remove old record
                student_list.append((update_name, updated_grade)) #update
                print("STUDENT INFORMATION HAS BEEN SUCCESSFULLY UPDATED!!\n")
                found = True
                break
        else:
                print("NO STUDENT FOUND!!\n")

    elif choice == "4":#for deleting info
        delete_name = input("Enter the name of the students: ")
        found = False
        for student in student_list:
            if student[0] == delete_name:
                student_list.remove(student)
                found = True
                break#using break otherwise it will continue its process
        else:
            print("NO STUDENT FPUND!!\n")



    elif choice == "5":
        print("EXITING FROM THE PROGRAM!!THANK YOU!")#a simple line to confirm that we are exiting
        break

    else:
        print("OOPS!Invalid choice, please try again. Thank you!")#if any other input is given in choice num, it will pop up
