import Record_Attendance
import Generate_Statistics

def main_menu(Lname):
    print("Main Menu")
    print("====================================")
    print("Welcome "+Lname)
    print("Module Record System - Options")
    print("------------------------------------")
    menu = "Please choose from the list of options" \
           "\n\t1: Record Attendance" \
           "\n\t2: Generate Statistics" \
           "\n\t3: Exit" \
           "\n==> "
    # create valid input variables to make sure you get the right choice
    SELECT = (1, 2, 3)
    # while loop to prompt until the correct choice is made
    while True:
        choice = int(input(menu))
        if choice in SELECT:
            break
        else:
            print("Not a valid choice, Please try a number and press enter")
    if choice == 1:
        Record_Attendance.record_attendance(Lname)
    elif choice == 2:
        Generate_Statistics.generate_statistics(Lname)
    elif choice == 3:
        print("Good bye")
        exit()



