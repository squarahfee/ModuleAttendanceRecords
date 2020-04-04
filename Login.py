from lpass_check import pass_check

def login():
    print("Welcome to Module Attendance Records")
    print("====================================")
    Lname = input("Please provide your login name...")
    Lpassw = input("Please provide you user password...")
    pass_check(Lname, Lpassw)

# the same as login(), but used when a login/pass is incorrect
# Doesn't have the welcome greeting
def login_two():
    Lname = input("Please provide your login name...")
    Lpassw = input("Please provide you user password...")
    lpass_check.pass_check(Lname, Lpassw)



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