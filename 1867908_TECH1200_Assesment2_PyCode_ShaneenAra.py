
# IT Service Desk Ticketing System
# Created by: SHANEEN ARA
#purpose: Handling customers from regarding Network Support System

import random
import datetime

ticket_list = [] #Here, i am creating 1 list which Stores all tickets
index_by_id = {}# a dict --> quick index for searching by ID





def generate_ticket_id():
    now = datetime.datetime.now()#using datetime to get the unique value
    time_part = now.strftime("%Y%m%d%H%M%S")
    number = random.randint(1000, 9999)       #this will assign random 4 values
    ticket_id = "T" + time_part + str(number)
    return ticket_id


# Here, I am Creating calculate_priority Function to determine priority level and score
def calculate_priority(ur,  affected_users):
    ur = ur.upper()


#Now, Priority logic based on urgency and user impact
    if ur == "HIGH" and affected_users > 5:
        return "P1", 3  # score is 3, so highest priority
    elif ur == "HIGH" and affected_users <= 5:
        return "P2", 2
    elif ur == "MEDIUM":
        return "P2", 2
    else:
        return "P3", 1  # score is 1, so lowest priority



#*********************************-------user-friendly-input-option-------**************************************
def submit_ticket():


    categories=["downtime",  "slow",  "config","wifi","vpn", "dns","email"]

    urgencies = ["low", "medium", "high"]

    max = 10000
    large = 1000
    retry = 3 #one user can try max 3 times



    #First of all user should give a valid category otherwise, submission will be not created
    category = ""
    attempts = 0
    while category == "" and attempts < retry:
        print("\nAvailable categories:")
        for i in range(len(categories)):
            print(i+1,  ".",  categories[i])

        # for each category there will be one num
        raw = input("ENTER CATEGORY [Name/Number]: ").lower()

        # if user enters number
        if raw.isdigit():#i am using isdigit(), as it will make sure if it is number, if not
            num = int(raw)#making sure to typecast int

            if num >= 1 and  num <= len(categories):
                category=categories[num-1]

            else:
                print("OOPS!!INVALID NUMBER!PLEASE TRY AGAIN!!")
        else:
            # checking if input isletter only
            c = ""
            for ch in raw:
                if 'a' <= ch.lower() <= 'z': #condition for making sure each char is lower
                    c=c + ch

            # exact match
            if c in categories:
                category = c

            else:
                # suggest category by checking first 3 letters
                suggested = ""
                if len(c) >= 3:
                    for c in categories:
                        if raw[:3] == c[:3]:
                            suggested = c
                            break

                if suggested != "":
                    yn = input("Did you mean '" + suggested + "'? (Y/N): ").lower()
                    if yn == "y":
                        category = suggested
                    else:
                        print("INVALID NUMBER!PLEASE TRY AGAIN")
                else:

                    print("INVALID NUMBER!PLEASE TRY AGAIN")
        attempts = attempts + 1

    if category == "":
        print("Too many invalid attempts. Returning to menu.")
        return


    ur = ""
    attempts = 0
    while ur == "" and attempts < retry:
        r2 = input("Enter urgency (Low/Medium/High): ").lower() #all input should be converted to lower
        if r2 in urgencies:
            ur = r2
        else:
            print("OOPS!!Invalid urgency. Try again.")
        attempts = attempts + 1

    if ur == "":
        print("OOPS!!Too many invalid attempts. Returning to menu.")
        return


    affected_users = 0
    attempts = 0
    while True:
        user=input(  "Enter number of affected users: ")
        if user.isdigit() and int(user) > 0:

            affected_users = int(user)
            break
        attempts += 1
        if attempts >= retry:#i set retry=3
            break #so, user can only try 3times

        # check if digits
        if user.isdigit():
            n = int(user)
            if n < 1: #negative value is not allowed
                print("OOPS!!Number must be at least 1.")

            elif n > max:# i set max = 10,000
                print("OOPS!!Number is too large. Try again.")

            elif n > large:
                confirm =  input("YOU HAVE ENTERED "  +  str(n) + ". Confirm? (Y/N): ").lower()
                if confirm=="y":
                    affected_users = n

                else:
                    print("Not confirmed. Re-enter.")
            else:
                affected_users = n
        else:
            print("PLEASE ENTER ONLY DIGITS.")
        attempts = attempts + 1

    if affected_users == 0:
        print("Too many invalid attempts. Returning to menu.")
        return
#+++++++++++++++final confirmation for ensuring if user want to submit or not++++++++


    print("CATEGORY:", category)
    print("URGENCY:", ur)

    print("AFFECTED USERS:", affected_users)
    confirm = input("CONFIRM SUBMISSION? (Y/N): ").lower()
    if confirm != "y":
        print("Submission cancelled.")
        return


    if ur == "high" and affected_users > 5: #if more than 10 user facing same problem, priority is highest
        p = "P1"
        s = 3
    elif ur == "high":
        p = "P2"
        s = 2
    elif ur == "medium":
        p = "P2"
        s = 2
    else:
        p = "P3"
        s = 1


    ticket_id = generate_ticket_id()
    nonce = str(random.randint(100000, 999999)) + datetime.datetime.now().strftime("%f")

    description = input("What happened?Kindly describe your issue shortly: ")
    status = "Open"

    ticket_record = {
        "id": ticket_id,
        "nonce": nonce,
        "category": category,
        "description": description,
        "urgency": ur.upper(),
        "impact_users": affected_users,
        "status": status,
        "priority": p,
        "priority_score": s
    }

    ticket_list.append(ticket_record)

    index_by_id[ ticket_id]=  len(ticket_list)- 1


    print("\nYee!!Ticket submitted successfully!")
    print("Ticket ID:", ticket_id, "||| Priority:", p, "||| (Score:", s, ")")



def update_status():


    ticket_id = input("Enter your Ticket ID: ")
    found = False

    # Search for ticket by ID
    for ticket in ticket_list:
        if ticket["id"] == ticket_id:
            found = True
            print("Current Status:", ticket["status"])

            # Show status options
            status_choice = input("""\nPlease choose the new status:
             1. Mark as Open
             2. Mark as In Progress
             3. Mark as Closed
             4. Leave unchanged
             Enter your choice: """)

            # Updating based on user choice
            if status_choice == "1":
                ticket["status"] = "Open"

            elif status_choice == "2":
                ticket["status"] = "In Progress"

            elif status_choice == "3":
                ticket["status"] = "Closed"

            print("Updated Status:", ticket["status"])
            break

    if not found:
        print("OOPS!!Ticket not found! Please check your ID and try again.")



def view_unresolved():

    found = False
    for ticket in ticket_list:
        if ticket["status"] in ["Open", "In Progress"]:
            print(ticket)
            found = True

    if not found:
        print("No unresolved tickets found.")



def view_closed():
    found = False
    for ticket in ticket_list:
        if ticket["status"] == "Closed":
            print(ticket)
            found = True

    if not found:
        print("No closed tickets found.")



def view_all():

    if len(ticket_list) == 0:
        print("No tickets available.")
    else:
        for ticket in ticket_list:
            print(ticket)


def exit_system():
    print("\nThank you for using the IT Service Desk System. Goodbye!")



def show_menu():
    print("""
=============== IT Service Desk System ===============
Welcome to the Network Support Ticketing System

1. Submit New Ticket
2. Update Ticket Status
3. View Unresolved Tickets
4. View Closed Tickets
5. Check All Tickets
6. Exit
=======================================================

NOTE: If your issue is resolved, please update your ticket status 
using Option 2 with your Ticket ID. Thank you!
""")


while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        submit_ticket()
    elif choice == "2":
        update_status()
    elif choice == "3":
        view_unresolved()
    elif choice == "4":
        view_closed()
    elif choice == "5":
        view_all()
    elif choice == "6":
        exit_system()
        break
    else:
        print("OOPS!!Invalid choice! Please try again.")
