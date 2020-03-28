def login():
    correct = False
    print("Welcome to Module Attendance Records")
    print("====================================")
    while not correct:
        Lname = input("Please provide your login name...")
        Lpassw = input("Please provide you user password...")
        correct = login_check(Lname, Lpassw)
    MainMenu(Lname)


def login_check(NameV, Password):
    correct = False
    for line in open("Login_data.txt","r").readlines():
        login_info = line.split(",")
        if NameV == login_info[0] and Password == login_info[1]:
            print("Valid credentials! Directing you to the main menu")
            correct = True
    if not correct:
        print("Invalid credentials, please try again")
        return False
    else: return True


def MainMenu(Lname):
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

def main():
    login()

main()