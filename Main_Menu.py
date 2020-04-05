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
        record_attendance()
    elif choice == 2:
        generate_statistics()
    elif choice == 3:
        print("Good bye")
        exit()

def record_attendance():
    print("Record attendance")

def generate_statistics():
    print("Generate Statistics")
